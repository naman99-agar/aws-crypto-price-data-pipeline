# AWS Crypto Price Data Pipeline

## 🚀 Project Overview
This project is an **automated data pipeline** that fetches cryptocurrency prices, stores them in **AWS S3**, and visualizes them in a **dashboard**. It demonstrates end-to-end **data engineering skills**, including API integration, AWS services, automation, and Python development.

---

## 🛠 Features
- Fetch live cryptocurrency prices from **Coindesk API**
- Save processed data as CSV files
- Upload files to **AWS S3 bucket**
- Simple dashboard to visualize historical prices
- Automated pipeline execution using **cron jobs**
- Organized, modular Python code for backend

---

## 📂 Project Structure
```
aws-data-pipeline/
├── backend
│   ├── dashboard.py
│   ├── main.py
│   ├── README.md
│   ├── requirements.txt
│   └── run_pipeline.sh
├── cron_jobs
│   ├── cleaner.sh
│   ├── scheduler.sh
│   └── instructions.md
├── infrastructure
│   └── notes.md
├── .gitignore
└── README.md
```
---

## ⚡ Installation & Setup

1. **Clone the repo**
```
git clone https://github.com/naman99-agar/aws-crypto-price-data-pipeline.git
cd aws-crypto-price-data-pipeline/backend`
```
2. **Create and activate virtual environment**
```
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```
pip install -r requirements.txt
```
4. **AWS Setup**

- Create an S3 bucket and note the bucket name
- Configure AWS CLI:
  `aws configure`
- Provide your Access Key ID, Secret Access Key, Region, and output format.

---

## 🖥 Run the Pipeline

1. Fetch and Upload Data
```
python run_pipeline.sh
```
3. Start Dashboard
```
python dashboard.py
```
Then open your browser at `http://127.0.0.1:8050` (if using Dash).

---

## ⏱ Automation with Cron

Pipeline can run automatically every 5 minutes using cron:

`*/5 * * * * /path/to/run_pipeline.sh >> pipeline.log 2>&1`

---

## 🌟 Future Improvements

- Real-time dashboard using WebSockets or FastAPI streaming
- Cloud automation with AWS Lambda & CloudWatch
- Multi-coin support (Bitcoin, Ethereum, etc.)
- Containerization using Docker
- CI/CD deployment for production-ready pipeline

---

## 📌 Key Skills Demonstrated

- Python scripting & API integration
- AWS S3 & cloud storage management
- Data pipeline automation with cron jobs
- Dashboard creation & data visualization
- Git versioning & project organization

---

## 🔗 Demo Screenshot

<img width="1437" height="803" alt="Screenshot 2025-12-10 at 6 38 27 PM" src="https://github.com/user-attachments/assets/b5275a00-c720-48bc-bb0c-59ea294e692d" />


