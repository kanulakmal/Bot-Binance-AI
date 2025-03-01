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
import os
from apscheduler.schedulers.background import BackgroundScheduler
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Bot Binance AI is Online!"

def autotrade():
    print("Running Autotrade...")

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(autotrade, 'interval', minutes=15)
    scheduler.start()
    
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
