# bot.py
import time
import datetime
import requests
import pandas as pd
from binance.client import Client
from binance.exceptions import BinanceAPIException

# Import konfigurasi dari file config
from config import API_KEY, API_SECRET, SYMBOL, INTERVAL, QUANTITY, SMA_SHORT, SMA_LONG

client = Client(API_KEY, API_SECRET)

def get_historical_data(symbol, interval, lookback):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=lookback)
    data = pd.DataFrame(klines, columns=[
        'time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume',
        'number_of_trades', 'taker_buy_base', 'taker_buy_quote', 'ignore'
    ])
    data['close'] = pd.to_numeric(data['close'])
    data['time'] = pd.to_datetime(data['time'], unit='ms')
    return data[['time', 'close']]

def calculate_sma(data, window):
    return data['close'].rolling(window=window).mean()

def place_order(side):
    try:
        order = client.create_order(
            symbol=SYMBOL,
            side=side,
            type='MARKET',
            quantity=QUANTITY
        )
        print(f"Order {side} executed: {order}")
    except BinanceAPIException as e:
        print(f"Binance API Exception: {e}")
    except Exception as e:
        print(f"Exception: {e}")

def trading_bot():
    print("Bot is running...")
    while True:
        data = get_historical_data(SYMBOL, INTERVAL, SMA_LONG)
        data['SMA_SHORT'] = calculate_sma(data, SMA_SHORT)
        data['SMA_LONG'] = calculate_sma(data, SMA_LONG)

        last_row = data.iloc[-1]
        previous_row = data.iloc[-2]

        if previous_row['SMA_SHORT'] < previous_row['SMA_LONG'] and last_row['SMA_SHORT'] > last_row['SMA_LONG']:
            print("Buy Signal")
            place_order('BUY')

        if previous_row['SMA_SHORT'] > previous_row['SMA_LONG'] and last_row['SMA_SHORT'] < last_row['SMA_LONG']:
            print("Sell Signal")
            place_order('SELL')

        time.sleep(900)  # 15 menit

if __name__ == '__main__':
    trading_bot()
