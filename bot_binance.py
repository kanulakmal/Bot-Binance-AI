from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
import os
import datetime

app = Flask(__name__)

# Fungsi Autotrade
def autotrade():
    print(f"🔥 Running Autotrade... {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

@app.route('/')
def home():
    return "✅ Bot Binance AI is Online!"

@app.route('/webhook', methods=['POST'])
def webhook():
    print("⚡ Webhook Diterima:", request.json)
    return "Webhook OK!", 200

# Tambahin route manual buat test Autotrade
@app.route('/run-autotrade', methods=['GET'])
def run_autotrade():
    autotrade()
    return "Autotrade triggered!", 200

# Scheduler 15 Menit
scheduler = BackgroundScheduler()
scheduler.add_job(autotrade, 'interval', minutes=15)
scheduler.start()

print("Scheduler is running...")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
