import aws_cdk as cdk
from infrastructure.job_scraper_stack import JobScraperStack

app = cdk.App()

env = cdk.Environment(account="474150619860", region="us-east-1")

JobScraperStack(app, "JobScraperStack", env=env)

app.synth()
