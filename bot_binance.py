from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone
import os
import datetime

app = Flask(__name__)

# Fungsi Autotrade
def autotrade():
    print(f"Running Autotrade... {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

@app.route('/')
def home():
    return "Hello, Bot Binance AI is Online!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Webhook Received: {data}")
    return jsonify({"message": "Webhook received"}), 200

# Timezone WIB
WIB = timezone("Asia/Jakarta")

# Scheduler jalan tiap 15 menit
scheduler = BackgroundScheduler(timezone=WIB)
scheduler.add_job(autotrade, 'interval', minutes=15)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    scheduler.start()
    print("Scheduler is running...")
    app.run(host='0.0.0.0', port=port)
