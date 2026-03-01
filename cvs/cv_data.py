"""
Jefferson Gonzalez - Structured CV data extracted from jeffgonzalez_CV (1).pdf
"""

PERSONAL_INFO = {
    "name": "JEFFERSON GONZALEZ",
    "title_devops": "Senior Cloud & DevOps Architect",
    "title_data_ai": "Senior Cloud & AI Solutions Architect",
    "location": "Colombia",
    "email": "yefgon1@gmail.com",
    "phone": "+57 3177689848",
    "github": "https://github.com/jbernal62",
    "linkedin": "https://www.linkedin.com/in/jeffersongonzalez",
}

SUMMARY_DEVOPS = (
    "Experienced and certified Senior Solutions Architect with over 12 years in IT "
    "and more than 7 years focused on cloud solutions across AWS, Azure, and Google Cloud. "
    "I specialize in designing scalable, event-driven, and secure architectures with deep "
    "expertise in Infrastructure as Code, CI/CD pipelines, container orchestration, and "
    "multi-cloud migrations. Passionate about automation, DevOps, and platform engineering, "
    "I bring a collaborative mindset, deep technical skills, and a strong foundation in "
    "security and compliance. I hold multiple certifications across the three major cloud "
    "providers including AWS Solutions Architect Professional and Azure Solutions Architect Expert."
)

SUMMARY_DATA_AI = (
    "Experienced and certified Senior Solutions Architect with over 12 years in IT "
    "and more than 7 years focused on cloud solutions across AWS, Azure, and Google Cloud. "
    "I specialize in designing scalable data platforms, AI/ML infrastructure, and intelligent "
    "automation solutions. With hands-on experience in Azure OpenAI, generative AI, ML platform "
    "migrations, and serverless data pipelines, I bridge the gap between cloud architecture and "
    "modern AI/Data systems. I bring a collaborative mindset, deep technical skills, and a strong "
    "foundation in security and compliance. I hold certifications in Generative AI with LLMs, "
    "AWS Solutions Architect Professional, and Google Cloud Professional Architect."
)

SKILLS_DEVOPS = {
    "Cloud Platforms": "AWS (EC2, Lambda, S3, ECS, EKS, CloudFormation, Connect, Lex, DynamoDB, Aurora, Amplify, AppSync), Azure (AKS, Azure DevOps, Databricks, Data Factory, Machine Learning, Sentinel, Front Door, Policy), GCP (Cloud Run, App Engine, Cloud Build, IAP, Cloud CDN, Pub/Sub, GKE)",
    "Infrastructure as Code & Automation": "Terraform, AWS CloudFormation, ARM Templates, Ansible, Pulumi",
    "DevOps & CI/CD": "Jenkins, GitHub Actions, Azure DevOps, AWS CodePipeline, Cloud Build, GitOps",
    "Containers & Orchestration": "Docker, Kubernetes (EKS, AKS, GKE), Helm, Container Registry",
    "Serverless": "AWS Lambda, Azure Functions, Google Cloud Functions, Cloud Run, API Gateway, AppSync (GraphQL)",
    "Networking & Security": "VPN, VPC, IAM, RBAC, SCPs, Azure Policy, Identity-Aware Proxy, Cognito, WAF, Penetration Testing",
    "Monitoring & Observability": "CloudWatch, Azure Monitor, Azure Sentinel, Grafana, Loki, Datadog, New Relic, Splunk, Zabbix, Nagios",
    "Cloud Frameworks & Governance": "AWS Well-Architected, Azure Well-Architected, Cost Optimization (RI/SP/Graviton), Cloud Migrations (Lift-and-Shift, Refactor)",
    "Methodologies": "Agile, Scrum, DevSecOps, SRE Principles, ITIL",
}

SKILLS_DATA_AI = {
    "AI & Machine Learning": "Azure OpenAI, Azure Machine Learning, AutoML, Responsible AI, Generative AI (LLMs), Salesforce Einstein, Amazon Lex, NLP, Model Interpretability",
    "Data Engineering & Services": "Azure Databricks, Azure Data Factory, DynamoDB, Aurora PostgreSQL (Babelfish), Google Pub/Sub, ETL/ELT Pipelines, S3 Data Lakes, Data Modeling, Serverless Data Processing",
    "Cloud Platforms": "AWS (Lambda, S3, DynamoDB, Aurora, Amplify, AppSync, Connect, Lex, SageMaker), Azure (Databricks, Data Factory, Machine Learning, OpenAI, DevOps, Sentinel), GCP (Cloud Run, Pub/Sub, BigQuery, Cloud Build)",
    "Serverless & Event-Driven": "AWS Lambda, API Gateway, AppSync (GraphQL), Cloud Run, Cloud Functions, EventBridge, S3 Event Triggers",
    "Infrastructure as Code": "Terraform, CloudFormation, ARM Templates, Ansible",
    "DevOps & CI/CD": "Jenkins, GitHub Actions, Azure DevOps, AWS CodePipeline, Cloud Build",
    "Containers & Orchestration": "Docker, Kubernetes (EKS, AKS, GKE), Helm",
    "Monitoring & Observability": "CloudWatch, Azure Monitor, Grafana, Datadog, New Relic",
    "Networking & Security": "VPN, VPC, IAM, RBAC, Cognito, Identity-Aware Proxy, Penetration Testing",
    "Methodologies": "Agile, Scrum, DevSecOps, MLOps, DataOps",
}

EXPERIENCE = [
    {
        "title": "Senior Data Engineer",
        "company": "Valtech",
        "location": "Bogota, Colombia (Remote)",
        "dates": "May 2025 - Present",
        "bullets_devops": [
            "Designed and implemented large-scale data pipelines in Azure Databricks, optimizing ETL processes for performance and scalability.",
            "Automated workflows using Azure Data Factory, integrating multiple sources into centralized data lakes.",
            "Ensured compliance, governance, and security across cloud data environments.",
            "Collaborated with cross-functional teams to define data models, improve data quality, and enable advanced analytics.",
            "Contributed to client projects by delivering actionable insights through efficient big data solutions.",
        ],
        "bullets_data_ai": [
            "Designed and implemented large-scale data pipelines in Azure Databricks, optimizing ETL processes for performance and scalability.",
            "Collaborated with cross-functional teams to define data models, improve data quality, and enable advanced analytics.",
            "Automated workflows using Azure Data Factory, integrating multiple sources into centralized data lakes.",
            "Ensured compliance, governance, and security across cloud data environments.",
            "Contributed to client projects by delivering actionable insights through efficient big data solutions.",
        ],
    },
    {
        "title": "GCP DevOps Architect",
        "company": "Decimal Studios",
        "location": "Remote",
        "dates": "Feb 2024 - Jun 2024",
        "is_freelance": True,
        "bullets_devops": [
            "Architected end-to-end CMS on GCP for a media-and-entertainment partner, defining service design, networking, security, and scaling patterns across Cloud Run, App Engine, IAP, and Cloud CDN.",
            "Led multi-environment migration from dev to staging/production using Terraform and Cloud Build, cutting deployment time by 30% and increasing release reliability.",
            "Containerized and deployed Strapi with Docker, leveraging Cloud Run and App Engine for modular, scalable backend services.",
            "Built CI/CD pipelines using Cloud Build and Deploy, automating build/test/deploy cycles for Node.js and React apps across multiple environments.",
            "Implemented secure authentication using Identity-Aware Proxy (IAP), enforcing identity-based access control to protect backend services.",
        ],
        "bullets_data_ai": [
            "Architected end-to-end CMS on GCP defining service design, networking, and scaling patterns across Cloud Run, App Engine, and Cloud CDN for media content delivery.",
            "Built CI/CD pipelines using Cloud Build, automating build/test/deploy cycles across multiple environments.",
            "Optimized infrastructure and cost-efficiency through strategic architecture reviews and rightsizing services.",
        ],
    },
    {
        "title": "Azure Cloud Architect",
        "company": "nearlyhuman.ai",
        "location": "Remote",
        "dates": "Nov 2023 - Dec 2023",
        "is_freelance": True,
        "bullets_devops": [
            "Architected and led migration of a mission-critical ML platform from AWS to Azure for a U.S. government client, ensuring full compliance with federal cloud security and governance standards.",
            "Developed infrastructure-as-code with ARM templates and integrated CI/CD pipelines via Azure DevOps, driving consistency, repeatability, and traceability.",
            "Enabled secure access and monitoring using Azure DevOps, Azure Monitor, Azure Security Center, and Azure Sentinel.",
        ],
        "bullets_data_ai": [
            "Architected and led migration of a mission-critical ML platform from AWS to Azure for a U.S. government client, ensuring full compliance with federal cloud security and governance standards.",
            "Designed secure, scalable Azure-native ML architecture, leveraging Azure Machine Learning, AutoML, and Azure OpenAI to support advanced model development and inferencing.",
            "Implemented Responsible AI best practices, including model interpretability, audit logging, and governance policies as per Azure Well-Architected guidelines.",
            "Presented architecture roadmap and estimates to technical and executive stakeholders, securing alignment and project approval.",
            "Developed infrastructure-as-code with ARM templates and integrated CI/CD pipelines via Azure DevOps for ML model deployment.",
        ],
    },
    {
        "title": "Senior DevOps Engineer",
        "company": "WayScript.com",
        "location": "Remote",
        "dates": "Aug 2022 - Apr 2023",
        "is_freelance": True,
        "bullets_devops": [
            "Led full migration of WayScript's core internal developer platform (IDP) from AWS to Azure, rearchitecting the system for multi-cloud resiliency and streamlined self-service deployment.",
            "Automated infrastructure provisioning with Terraform and AKS, enabling developers to spin up containerized, pre-configured development environments with a single click.",
            "Integrated observability via New Relic and Azure Monitor/Sentinel, delivering out-of-the-box monitoring across dev/staging/prod environments.",
            "Built CI/CD workflows using Azure DevOps and GitHub Actions, slashing release cycle times by ~40% and achieving consistent, repeatable deployments.",
            "Enhanced platform security and governance with Azure Policy, Kubernetes RBAC, and hardened AKS configurations.",
        ],
        "bullets_data_ai": [
            "Led full migration of WayScript's core internal developer platform from AWS to Azure, rearchitecting for multi-cloud resiliency.",
            "Automated infrastructure provisioning with Terraform and AKS for containerized development environments.",
            "Built CI/CD workflows using Azure DevOps and GitHub Actions, slashing release cycle times by ~40%.",
        ],
    },
    {
        "title": "AWS Cloud Engineer",
        "company": "SGS & Co",
        "location": "Remote",
        "dates": "Aug 2022 - Sep 2022",
        "is_freelance": True,
        "bullets_devops": [
            "Designed and delivered a GPU-accelerated pixel streaming platform on AWS, enabling media teams to interact with Unreal Engine-based environments via NICE DCV sessions.",
            "Built a fully serverless control plane using AWS Amplify, AppSync (GraphQL API), Lambda, DynamoDB, and Cognito.",
            "Automated lifecycle management using Lambda functions for stream registration, termination, and scheduled instance warm-up.",
        ],
        "bullets_data_ai": [
            "Designed and delivered a GPU-accelerated real-time streaming platform on AWS for interactive 3D media experiences.",
            "Built a fully serverless data control plane using AWS Amplify, AppSync (GraphQL API), Lambda, DynamoDB, and Cognito, supporting on-demand processing workflows.",
            "Configured centralized observability using Amazon CloudWatch for real-time logging and performance insights across serverless functions and backend services.",
        ],
    },
    {
        "title": "Senior Cloud Architect",
        "company": "Caylent",
        "location": "USA (Remote)",
        "dates": "Apr 2021 - Jan 2022",
        "bullets_devops": [
            "Led multi-cloud migrations, including transitioning Microsoft workloads and Azure environments to AWS using automated strategies across 25+ VMs with zero downtime.",
            "Architected AWS-based replacement infrastructure using EC2, ELB, IAM Identity Center, Managed AD, and VPN networking while preserving original security policies.",
            "Implemented Infrastructure as Code with Terraform and AWS CloudFormation to standardize deployments and accelerate migration.",
            "Designed and enforced Azure guardrails and RBAC policies, translating into AWS best practices with IAM roles, SCPs, and account structures.",
            "Modernized legacy databases, advising on migrating SQL Server workloads to Babelfish-enabled Aurora PostgreSQL, achieving ~40% performance improvement and ~50% licensing cost reduction.",
            "Automated CI/CD and DevOps processes using Jenkins, Terraform, Ansible, and AWS CodePipeline.",
        ],
        "bullets_data_ai": [
            "Modernized legacy databases, advising on migrating SQL Server workloads to Babelfish-enabled Aurora PostgreSQL, achieving ~40% performance improvement and ~50% licensing cost reduction.",
            "Led multi-cloud migrations across 25+ VMs with zero downtime, establishing data continuity patterns.",
            "Automated CI/CD and DevOps processes using Jenkins, Terraform, Ansible, and AWS CodePipeline.",
        ],
    },
    {
        "title": "Senior Cloud Architect",
        "company": "EPAM Systems",
        "location": "Remote",
        "dates": "Feb 2021 - Dec 2021",
        "bullets_devops": [
            "Managed multi-cloud infrastructure (Azure, AWS), designed SLAs and CI/CD pipelines.",
            "Built cost optimization plans using Reserved Instances, Savings Plans, and Graviton instances.",
            "Automated with Jenkins, Terraform, Ansible; set up observability with Grafana, Loki, and Datadog.",
        ],
        "bullets_data_ai": [
            "Managed multi-cloud infrastructure across Azure and AWS, designed SLAs and data pipeline architectures.",
            "Built cost optimization plans using Reserved Instances, Savings Plans, and Graviton instances.",
            "Set up observability with Grafana, Loki, and Datadog for monitoring data processing workloads.",
        ],
    },
    {
        "title": "Cloud Solutions Architect",
        "company": "Cloudbeach",
        "location": "Remote",
        "dates": "Dec 2018 - Dec 2020",
        "bullets_devops": [
            "Delivered cloud migrations using CI/CD with GKE, AKS, and Cloud Run.",
            "Designed ETL, serverless, and multi-cloud solutions for ISVs and startups.",
            "Integrated Pub/Sub-based real-time applications.",
        ],
        "bullets_data_ai": [
            "Designed ETL pipelines, serverless data processing, and multi-cloud solutions for ISVs and startups.",
            "Integrated Google Pub/Sub-based real-time data streaming applications.",
            "Delivered cloud migrations using CI/CD with GKE, AKS, and Cloud Run.",
        ],
    },
    {
        "title": "Solutions Engineer",
        "company": "NoventiQ Global",
        "location": "Remote",
        "dates": "Oct 2017 - Nov 2018",
        "bullets_devops": [
            "Led technical go-to-market strategies for cloud and security products.",
            "Worked across Azure Front Door, Sentinel, AKS, Application Gateway.",
            "Collaborated with global teams to build LATAM-focused managed services.",
        ],
        "bullets_data_ai": [
            "Led technical go-to-market strategies for cloud and security products.",
            "Collaborated with global teams to build LATAM-focused managed services.",
        ],
    },
    {
        "title": "Cloud Solutions Engineer",
        "company": "Licencias OnLine",
        "location": "Colombia",
        "dates": "May 2014 - Jun 2016",
        "bullets_devops": [
            "Developed go-to-market strategies and architectures for Azure/AWS.",
            "Enabled SaaS and virtualization offerings that increased partner revenue.",
        ],
        "bullets_data_ai": [
            "Developed go-to-market strategies and cloud architectures for Azure/AWS.",
            "Enabled SaaS and virtualization offerings that increased partner revenue.",
        ],
    },
    {
        "title": "Cloud Solutions Engineer",
        "company": "O4IT",
        "location": "Colombia",
        "dates": "Jan 2013 - Mar 2014",
        "bullets_devops": [
            "Monitored critical services using Zabbix, Splunk, PRTG, and Nagios.",
            "Strengthened infrastructure security with network policy enforcement and access controls.",
        ],
        "bullets_data_ai": [
            "Monitored critical services using Zabbix, Splunk, PRTG, and Nagios for data-driven operational insights.",
            "Strengthened infrastructure security with network policy enforcement and access controls.",
        ],
    },
]

EDUCATION = [
    {
        "degree": "MSc in IT Security Management",
        "institution": "Arden University, London, UK",
        "dates": "Oct 2018 - Jan 2021",
    },
    {
        "degree": "Advanced Diploma in Network Security",
        "institution": "TAFE NSW, Sydney, Australia",
        "dates": "June 2016 - July 2017",
    },
]

CERTIFICATIONS = [
    "AWS Certified Solutions Architect - Professional / Associate",
    "Generative AI with Large Language Models - DeepLearning.AI",
    "AWS Serverless Specialist",
    "Azure Solutions Architect Expert",
    "Azure Administrator Associate",
    "Microsoft Azure Fundamentals",
    "Google Cloud Professional Architect",
    "C)PTE - Certified Penetration Testing Engineer",
    "Red Hat Sales Specialist - IaaS",
    "Red Hat Middleware Solutions Specialist",
]

LANGUAGES = [
    ("Spanish", "Native"),
    ("English", "Proficient"),
]
