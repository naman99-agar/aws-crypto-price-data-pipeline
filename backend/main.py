from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import boto3
import json
from datetime import datetime

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# S3 client
s3 = boto3.client("s3")
BUCKET_NAME = "crypto-price-data-naman"

# Coin mapping
COINGECKO_MAP = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "SOL": "solana",
    "DOGE": "dogecoin"
}

# Simple in-memory cache
CACHE = {}
CACHE_TIMESTAMP = None
CACHE_TTL = 10  # seconds


@app.get("/crypto-prices")
def get_crypto_prices():
    global CACHE, CACHE_TIMESTAMP
    now = datetime.utcnow()

    # Use cache if within TTL
    if CACHE and CACHE_TIMESTAMP and (now - CACHE_TIMESTAMP).seconds < CACHE_TTL:
        return CACHE

    ids = ",".join(COINGECKO_MAP.values())
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        # Return cached data if available on error
        if CACHE:
            return CACHE
        else:
            return {symbol: "N/A" for symbol in COINGECKO_MAP.keys()}

    result = {}
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    for symbol, cg_id in COINGECKO_MAP.items():
        price = data.get(cg_id, {}).get("usd")
        result[symbol] = price if price is not None else "N/A"

        # Save to S3
        file_name = f"crypto/{symbol}_{timestamp}.json"
        json_data = json.dumps({"symbol": symbol, "price": price, "timestamp": timestamp})
        try:
            s3.put_object(
                Bucket=BUCKET_NAME,
                Key=file_name,
                Body=json_data,
                ContentType="application/json"
            )
        except Exception as e:
            pass  # ignore S3 errors for now

    CACHE = result
    CACHE_TIMESTAMP = now
    return result
