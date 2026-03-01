from aws_cdk import (
    Stack,
    Duration,
    CfnOutput,
    aws_lambda as lambda_,
    aws_iam as iam,
    aws_events as events,
    aws_events_targets as targets,
    aws_secretsmanager as secretsmanager,
)
from constructs import Construct

ACCOUNT_ID = "474150619860"
REGION = "us-east-1"


class JobScraperStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Reference existing Google Sheets secret from invoice-tracker
        google_secret = secretsmanager.Secret.from_secret_name_v2(
            self, "GoogleSheetsCredentials",
            "invoice-tracker/google-sheets-credentials"
        )

        # IAM Role
        lambda_role = iam.Role(
            self, "JobScraperLambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            role_name="job-scraper-lambda-role",
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSLambdaBasicExecutionRole"
                )
            ],
        )
        google_secret.grant_read(lambda_role)

        # Lambda Layer
        deps_layer = lambda_.LayerVersion(
            self, "JobScraperDepsLayer",
            layer_version_name="job-scraper-deps",
            code=lambda_.Code.from_asset("lambda_layer/layer.zip"),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_12],
            description="requests, beautifulsoup4, gspread, google-auth, google-api-python-client",
        )

        # Lambda Function
        scraper_fn = lambda_.Function(
            self, "JobScraperFn",
            function_name="job-scraper-processor",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="handler.lambda_handler",
            code=lambda_.Code.from_asset("lambda"),
            role=lambda_role,
            layers=[deps_layer],
            timeout=Duration.seconds(300),
            memory_size=512,
            environment={
                "GOOGLE_SECRET_NAME": "invoice-tracker/google-sheets-credentials",
                "GOOGLE_SHEET_NAME": "LinkedIn Job Scraper",
            },
        )

        # EventBridge daily schedule at 08:00 UTC
        rule = events.Rule(
            self, "DailyJobScrapeRule",
            rule_name="daily-job-scrape",
            schedule=events.Schedule.cron(hour="8", minute="0"),
            description="Trigger LinkedIn job scraper daily at 08:00 UTC",
        )
        rule.add_target(targets.LambdaFunction(scraper_fn))

        # Outputs
        CfnOutput(self, "LambdaFunctionName",
                  value=scraper_fn.function_name,
                  description="Lambda function name for manual invocation")
        CfnOutput(self, "EventBridgeRule",
                  value=rule.rule_name,
                  description="EventBridge rule for daily schedule")
        CfnOutput(self, "ManualInvokeCommand",
                  value=f"aws lambda invoke --function-name {scraper_fn.function_name} --payload '{{}}' /dev/stdout --cli-binary-format raw-in-base64-out",
                  description="Command to manually trigger the scraper")
