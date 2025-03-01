from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Bot Binance AI is Online!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)  # Fix port for Render
    
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import os
import datetime

app = Flask(__name__)

scheduler = BackgroundScheduler()

@app.route('/')
def home():
    return "Hello, Bot Binance AI is Online!"

# Fungsi Autotrade
def autotrade():
    now = datetime.datetime.now()
    print(f"Running Autotrade... {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Jadwalin bot setiap 15 menit
scheduler.add_job(autotrade, 'interval', minutes=15)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    scheduler.start()
    print("Scheduler is running...")
    app.run(host='0.0.0.0', port=port)
