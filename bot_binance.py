
from flask import Flask
import ccxt
import pyngrok

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Bot Binance AI Running!'

if __name__ == '__main__':
    app.run(port=5000)
