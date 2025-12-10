from fastapi import FastAPI
import requests
import boto3
import json
from datetime import datetime

app = FastAPI()

# Initialize S3 client
s3 = boto3.client("s3")

BUCKET_NAME = "your bucket name"   # <-- update this

@app.get("/crypto-price")
def get_crypto_price():
    # Fetch Bitcoin price
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()

    price = data["bitcoin"]["usd"]
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")

    # File name to store in S3
    file_name = f"crypto/bitcoin_{timestamp}.json"

    # Data to save
    json_data = json.dumps({
        "btc_price": price,
        "timestamp": timestamp
    })

    # Upload to S3
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=json_data,
        ContentType="application/json"
    )

    return {"price": price, "message": "Saved to S3!"}

import boto3
from datetime import datetime

s3 = boto3.client("s3")
BUCKET_NAME = "your bucket name"

@app.get("/store-price")
def store_price():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    price_data = response.json()
    price = price_data["bitcoin"]["usd"]

    # Create a filename with timestamp
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"bitcoin_price_{timestamp}.txt"

    # Write price locally
    with open(filename, "w") as f:
        f.write(f"Bitcoin Price: ${price}")

    # Upload to S3
    s3.upload_file(filename, BUCKET_NAME, filename)

    return {"message": "Price stored in S3", "filename": filename}
