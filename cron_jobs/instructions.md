# Cron Job Setup Instructions

This document explains how to schedule and manage cron jobs for the AWS Data Pipeline project. These jobs automate pipeline execution at fixed intervals.

---

## 1. What Cron Jobs Do

Cron jobs allow you to:
- Run the data pipeline every few minutes  
- Execute cleanup scripts  
- Append logs for monitoring  
- Trigger backend processes without manual intervention  

---

## 2. How to Open the Cron Editor

Use this command:

```
crontab -e
```
This opens the user's cron table in an editor (usually vim or nano).

---

## 3. Add Cron Jobs
### 3.1 Run Pipeline Every 5 Minutes
```
*/5 * * * * /Users/<your folder path>/Documents/Projects/aws-data-pipeline/backend/run_pipeline.sh >> /Users/<your folder path>/Documents/Projects/aws-data-pipeline/backend/pipeline.log 2>&1
```
### 3.2 Run Cleaner Script Every 2 Minutes
```
*/2 * * * * /Users/<your folder path>/cleaner_test/scheduler.sh
```
## 4. Cron Timing Format
```
┌───────────── minute (0 - 59)
│ ┌──────────── hour (0 - 23)
│ │ ┌────────── day of month (1 - 31)
│ │ │ ┌──────── month (1 - 12)
│ │ │ │ ┌────── day of week (0 - 6)
│ │ │ │ │
*  *  *  *  *  command_to_run
```
Examples:

- `*/5 * * * *` → every 5 minutes

- `0 * * * *` → every hour

- `0 0 * * *` → every day at midnight

---

## 5. Important Cron Requirements
### 5.1 Always Use Absolute Paths

Cron does not know your virtual environment paths automatically.

Example:

✔ `/Users/<your folder path>/Documents/...`

✘ `./backend/run_pipeline.sh`

### 5.2 Ensure Script is Executable
`chmod +x run_pipeline.sh`

### 5.3 Use the Correct Python Path

Find your Python:

`which python`

If needed, update your shell script accordingly.

---

## 6. Viewing Active Cron Jobs

Use:

`crontab -l`

---

## 7. How to Debug Cron Issues
### 7.1 Check the Log File

Look at pipeline logs:

`cat /Users/<your folder path>/Documents/Projects/aws-data-pipeline/backend/pipeline.log`

### 7.2 Add Debug Output Inside Script

Add this inside your shell script to verify environment:
```
echo "Cron started at $(date)" >> cron_debug.log
env >> cron_debug.log
```
### 7.3 Verify Your Script Runs Manually
`sh run_pipeline.sh`

If it fails manually → cron will also fail.

---

## 8. Removing a Cron Job

Open editor:

`crontab -e`
Delete the specific line, save, and exit.

