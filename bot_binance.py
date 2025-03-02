import os
import logging
import time
import requests
from datetime import datetime
from pytz import timezone
from apscheduler.schedulers.background import BackgroundScheduler

# Tambahin Timezone WIB
logging.basicConfig(level=logging.DEBUG)
os.environ['TZ'] = 'Asia/Jakarta'
print("Timezone Set to Asia/Jakarta")

# Fungsi untuk Autotrade Buy
def autotrade_buy():
    logging.info("Running Autotrade Buy")
    now = datetime.now()
    logging.info(f"Current Time: {now}")
    # Simulasi Buy
    try:
        webhook_url = os.getenv("WEBHOOK_URL", "http://localhost:8000/webhook")
        response = requests.post(webhook_url, json={"action": "buy"})
        logging.info(f"Webhook Response: {response.status_code} - {response.text}")
    except Exception as e:
        logging.error(f"Error: {e}")

# Setup Scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(autotrade_buy, 'interval', minutes=1)  # Setiap 1 menit
scheduler.start()

try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    logging.info("Scheduler stopped")
