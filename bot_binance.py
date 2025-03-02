from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import logging
import time

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

API_URL = "https://api.binance.me/api/v3/ticker/price?symbol=BTCUSDT"

def autotrade_buy():
    logging.info("Running Autotrade Buy")
    try:
        response = requests.get(API_URL)
        data = response.json()
        
        if 'price' in data:
            price = float(data["price"])
            logging.info(f"Price BTC: {price}")
        else:
            logging.error("Key 'price' not found in API response")
            logging.error(f"API Response: {data}")
    except Exception as e:
        logging.error(f"Error Autotrade Buy: {e}")

@app.route("/")
def home():
    return "Bot Binance AI Running..."

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    autotrade_buy()
    return {"status": "Webhook Received"}

scheduler = BackgroundScheduler()
scheduler.add_job(autotrade_buy, "interval", minutes=1)
scheduler.start()

if __name__ == "__main__":
    logging.info("Starting Flask App")
    app.run(debug=True, host="0.0.0.0", port=5000)

    while True:
        time.sleep(1)
