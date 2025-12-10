# Backend – AWS Data Pipeline
This directory contains all backend logic for running the data pipeline, exposing APIs, and integrating with cron jobs.

---

## 1. Overview

The backend has two major components:

### 1.1 FastAPI Service
- Serves the dashboard endpoint  
- Allows manual triggering of pipeline runs  
- Returns pipeline status/logs  

### 1.2 Python Pipeline Script
- Fetches data from source  
- Cleans/transforms it  
- Stores final output  
- Appends logs for monitoring  

---

## 2. Folder Structure
```
backend/
│── main.py # FastAPI server entrypoint
│── dashboard.py # Dashboard + API routes
│── run_pipeline.sh # Shell script for pipeline trigger
│── requirements.txt # Python dependencies
│── README.md # This file
```

---

## 3. How to Set Up Locally

### 3.1 Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3.1 Create a Virtual Environment
```bash
pip install -r requirements.txt
```
---

## 4. Running the FastAPI Backend
### 4.1 Start FastAPI Server
```
uvicorn main:app --reload
```
This launches the server at:
```bash
http://127.0.0.1:8000
```
### 4.2 API Endpoints
```
/dashboard
```
Returns dashboard data.
```
/pipeline/run
```
Manually triggers the pipeline.

---

## 5. Running the Pipeline Manually
### 5.1 Run via Python
```
python dashboard.py
```
### 5.2 Run via Shell Script
```
sh run_pipeline.sh
```
## 6. Integration With Cron Jobs

The pipeline can run automatically using macOS/Linux cron.

### 6.1 Adding a Cron Job

Open cron editor:
```
crontab -e
```
Example entry (runs every 5 minutes):
```
*/5 * * * * /path/to/backend/run_pipeline.sh >> /path/to/backend/pipeline.log 2>&1
```
### 6.2 Cron Debug Tips

- Ensure script has executable permissions

- Use full absolute paths in scripts

- Redirect logs for debugging

---

## 7. Logs

Pipeline logs are stored in:
```
backend/pipeline.log
```

They help in debugging:

- Runtime errors

- Cron failures

- API-triggered runs

## 8. Environment Variables (Optional)

If you include secrets later:

- Use .env file

- Never commit it

- Example usage:
```
export DATA_SOURCE_URL="https://example.com/data.json"
```
## 9. Future Enhancements
### 9.1 AWS Deployment

- S3 for storing data

- Lambda / Step Functions for automated runs

- DynamoDB/RDS for structured storage

- CloudWatch for monitoring

### 9.2 Add Authentication

Secure the dashboard with login.

### 9.3 Add Frontend UI

React/Vite dashboard to visualize results.
