import time
import schedule
import requests
import boto3
from datetime import datetime

s3 = boto3.client("s3")
BUCKET_NAME = "crypto-price-data-naman"

def save_price():
    print("Collecting Bitcoin price...")
    
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    price = response.json()["bitcoin"]["usd"]

    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"bitcoin_price_{timestamp}.txt"

    with open(filename, "w") as f:
        f.write(f"Bitcoin Price: ${price}")

    s3.upload_file(filename, BUCKET_NAME, filename)
    print(f"Uploaded: {filename}")

# Schedule task every 1 minute
schedule.every(1).minutes.do(save_price)

print("Collector started...")

while True:
    schedule.run_pending()
    time.sleep(1)
