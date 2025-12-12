import boto3
import pandas as pd
import plotly.express as px

BUCKET = "crypto-price-data-naman"
KEY = "processed/prices.csv"

s3 = boto3.client("s3")

# Download CSV from S3
s3.download_file(BUCKET, KEY, "prices.csv")

# Read CSV
df = pd.read_csv("prices.csv")

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"], format="%Y-%m-%d_%H-%M-%S")

# Plot
fig = px.line(df, x="timestamp", y="price_usd", title="Bitcoin Price Over Time")
fig.show()
