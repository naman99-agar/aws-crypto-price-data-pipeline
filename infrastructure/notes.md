# Infrastructure Notes — AWS Data Pipeline

This document explains the full backend infrastructure used in this project, including AWS services, IAM roles, S3 setup, local automation using cron, and how everything integrates into a functioning data pipeline.

---

## 1. Overview of Architecture

The project uses a hybrid infrastructure:

- **AWS S3** → storage for processed CSV outputs  
- **Local Python Script (`main.py`)** → collects data from CoinDesk  
- **Local Cron Job** → automates pipeline execution  
- **Dashboard (`dashboard.py`)** → downloads latest file from S3 and displays chart  
- **AWS IAM User** → provides programmatic access for uploads  
- **boto3 SDK** → communicates with AWS  

Flow:
```
Coingecko API → main.py → processed/prices.csv → uploaded to S3
↓
dashboard.py reads latest file
```

---

## 2. AWS S3 Setup

### 2.1 Bucket Used
- **Name:** `crypto-price-data-naman`
- **Region:** `ap-southeast-2`

### 2.2 Folder Structure Inside Bucket
```
crypto-price-data-naman
└── processed
└── prices.csv
```

### 2.3 Purpose
- Central storage for processed cryptocurrency price data  
- Ensures dashboard always loads the latest version  
- Accessible through `boto3`  

---

## 3. IAM Configuration

### 3.1 IAM User Created
- **Programmatic access only**
- Access Key + Secret Access Key generated

### 3.2 IAM Permissions
Attached policy:

- `AmazonS3FullAccess`  
  *(For learning; in production use a least-privilege custom policy.)*

### 3.3 AWS CLI Configuration

Command used:

`aws configure`

Inputs:

- Access Key

- Secret Key

- Region: `<your region>`

- Output format: json

---

## 4. Local Machine Setup
### 4.1 Python Virtual Environment

Created using:
```
python -m venv venv
source venv/bin/activate
```
### 4.2 Installing Project Dependencies

Inside backend/:

`pip install -r requirements.txt`

### 4.3 Important Libraries

- boto3 → Upload/download S3 files

- pandas → Data processing

- requests → Get API data

- dash + plotly → Web dashboard

---

## 5. Cron Job Automation
### 5.1 Pipeline Execution Every 5 Minutes
`*/5 * * * * /Users/namanagarwalla/Documents/Projects/aws-data-pipeline/backend/run_pipeline.sh >> /Users/namanagarwalla/Documents/Projects/aws-data-pipeline/backend/pipeline.log 2>&1`

### 5.2 Cleaning Script (Example)
`*/2 * * * * /Users/namanagarwalla/cleaner_test/scheduler.sh`

### 5.3 Why Cron?

- Automates recurring data fetching

- Ensures S3 is always updated

- Runs without user intervention

---

## 6. Pipeline Shell Script

`run_pipeline.sh` (executed by cron):

- Activates virtual environment

- Runs main.py

- Logs errors

- Ensures smooth automated pipeline execution

Example:
```
source /Users/namanagarwalla/Documents/Projects/aws-data-pipeline/backend/venv/bin/activate
python /Users/namanagarwalla/Documents/Projects/aws-data-pipeline/backend/main.py
```

---

## 7. Security Considerations

Do NOT commit AWS credentials to GitHub

- `.gitignore` must include:

  * `venv/`

  * `__pycache__/`

  * `.aws/credentials`

  * Local logs

- Use IAM least-privilege policies for production

- Rotate IAM access keys regularly

---

## 8. Future Expansion Options
### 8.1 Move Backend to AWS Lambda

- Run pipeline in the cloud

- Trigger via CloudWatch Events

- No cron + no local machine dependency

### 8.2 Use AWS Glue or AWS Step Functions

For large-scale workflows.

### 8.3 Add DynamoDB or RDS

To store long-term crypto price history.

### 8.4 Deploy Dashboard Online

Options:

- AWS EC2

- AWS Amplify

- GitHub Pages (static)

- Streamlit Cloud
