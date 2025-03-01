from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import os
import datetime

app = Flask(__name__)

# Fungsi Autotrade (Jalan tiap 15 menit)
def autotrade():
    print(f"Running Autotrade... {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    # Logic Autotrade Buy dan Sell disini

@app.route('/')
def home():
    return "Hello, Bot Binance AI is Online!"

# Endpoint Webhook buat TradingView
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Webhook Received: {data}")
    # Kodingan Buy/Sell disini
    return jsonify({"status": "Success", "message": "Signal Received"}), 200

# Scheduler 15 menit
scheduler = BackgroundScheduler()
scheduler.add_job(autotrade, 'interval', minutes=15)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    scheduler.start()
    print("Scheduler is running...")
    app.run(host='0.0.0.0', port=port)  # Fix port for Render


