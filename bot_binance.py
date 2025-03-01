from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
import os
import datetime
import logging
import threading

# Konfigurasi Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)

# Fungsi Autotrade
def autotrade():
    log_msg = f"🔥 Running Autotrade... {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    logging.info(log_msg)

@app.route('/')
def home():
    return "✅ Bot Binance AI is Online!"

@app.route('/webhook', methods=['POST'])
def webhook():
    logging.info(f"⚡ Webhook Diterima: {request.json}")
    return "Webhook OK!", 200

# Scheduler 15 Menit
scheduler = BackgroundScheduler()
scheduler.add_job(autotrade, 'interval', minutes=15)
logging.info("✅ Scheduler is running...")

# Jalankan scheduler di thread terpisah agar tidak bentrok dengan Flask
threading.Thread(target=scheduler.start, daemon=True).start()

# Jalankan autotrade pertama kali agar tidak perlu nunggu 15 menit pertama
autotrade()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
