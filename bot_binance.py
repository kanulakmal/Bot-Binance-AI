from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import os
import datetime
import pytz
import logging

logging.basicConfig(level=logging.DEBUG)
tz = pytz.timezone("Asia/Jakarta")
os.environ['TZ'] = 'Asia/Jakarta'
print("Timezone Set to Asia/Jakarta")

app = Flask(__name__)

# Fungsi Autotrade
def autotrade():
    print(f"[DEBUG] Autotrade Running at {datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')}")
    # Logic Autotrade Buy dan Sell disini

@app.route('/')
def home():
    return "Hello, Bot Binance AI is Online!"

# Jadwalin bot tiap 15 menit
scheduler = BackgroundScheduler()
scheduler.add_job(autotrade, 'interval', minutes=15)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Webhook Received: {data}")
    return jsonify({"message": "Webhook received"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))

    if not scheduler.running:
        scheduler.start()
        print("Scheduler is force started...")
    else:
        print("Scheduler already running...")

    print("Scheduler is running...")
    app.run(host='0.0.0.0', port=port)  # Fix port for Render
