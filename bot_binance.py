from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
import logging
import os
import datetime

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger("Scheduler")

app = Flask(__name__)

# Fungsi Autotrade dengan Logging
def autotrade():
    log.info(f"🔥 Running Autotrade... {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

@app.route('/')
def home():
    return "✅ Bot Binance AI is Online!"

@app.route('/webhook', methods=['POST'])
def webhook():
    log.info(f"⚡ Webhook Diterima: {request.json}")
    return "Webhook OK!", 200

# Scheduler 15 Menit
scheduler = BackgroundScheduler()
scheduler.add_job(autotrade, 'interval', minutes=15)
scheduler.start()
log.info("✅ Scheduler is running...")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
