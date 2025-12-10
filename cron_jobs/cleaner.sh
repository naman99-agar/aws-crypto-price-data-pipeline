# Deletes old log files (older than 7 days)
find /Users/<your folder path>/Documents/Projects/aws-data-pipeline/backend -name "*.log" -mtime +7 -delete

