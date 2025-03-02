import os
import logging
import requests
import json
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from pytz import timezone
from flask import Flask, request

# Logging
logging.basicConfig(level=logging.DEBUG)

# Timezone WIB
WIB = timezone("Asia/Jakarta")

# API URL BINANCE with Proxy Server
api_url = "https://api1.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

# Webhook Endpoint
WEBHOOK_URL = os.getenv("RENDER_EXTERNAL_URL") + "/webhook"

app = Flask(__name__)

def autotrade_buy():
    logging.info("Running Autotrade Buy")
    current_time = datetime.now(WIB).strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Current Time: {current_time}")
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(api_url, headers=headers)
        data = response.json()
        if "price" in data:
            price = float(data['price'])
            logging.info(f"BTC Price: {price}")

            # Trigger Webhook
            webhook_data = {"price": price, "action": "buy"}
            logging.info(f"Sending Webhook to {WEBHOOK_URL}")
            webhook_response = requests.post(WEBHOOK_URL, json=webhook_data)
            logging.info(f"Webhook Response: {webhook_response.status_code}")
        else:
            logging.error("Key 'price' not found in API response")
            logging.error(f"API Response: {data}")

    except Exception as e:
        logging.error(f"Error: {e}")

scheduler = BackgroundScheduler()
scheduler.add_job(autotrade_buy, 'interval', minutes=1)
scheduler.start()

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    logging.info(f"Received Webhook Data: {data}")
    return {"message": "Webhook received"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
