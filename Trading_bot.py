import ccxt
import time
import logging
from config import BINANCE_API_KEY, BINANCE_API_SECRET, TRADE_PAIR, TIMEFRAME, TRADE_AMOUNT, STOP_LOSS, TAKE_PROFIT

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Inisialisasi Binance API
exchange = ccxt.binance({
    'apiKey': kAawOsaLo73u9OjG3sbGcyBCq5Gg8gSssUkiUZR4sM34qo3czcW99tob2G2BRwfK,
    'secret': x5ZbUVpI9¡Cj0yaROIVrm6YQ6LYovId3LZVYJCxMXQMQmf3BNUoZq&SOljc,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'spot',
    }
})

# Fungsi Fetch Candlestick Data
def fetch_candles():
    try:
        candles = exchange.fetch_ohlcv(TRADE_PAIR, TIMEFRAME, limit=50)
        return candles
    except Exception as e:
        logging.error(f"Error fetching candles: {e}")
        return None

# Fungsi Analisa Sederhana (Contoh Moving Average Cross)
def simple_strategy(candles):
    close_prices = [candle[4] for candle in candles]
    ma_10 = sum(close_prices[-10:]) / 10
    ma_20 = sum(close_prices[-20:]) / 20
    
    if ma_10 > ma_20:
        return 'BUY'
    elif ma_10 < ma_20:
        return 'SELL'
    else:
        return 'HOLD'

# Fungsi Eksekusi Order
def execute_order(order_type):
    try:
        if order_type == 'BUY':
            order = exchange.create_market_buy_order(TRADE_PAIR, TRADE_AMOUNT)
            logging.info(f"Buy Order Executed: {order}")
        elif order_type == 'SELL':
            order = exchange.create_market_sell_order(TRADE_PAIR, TRADE_AMOUNT)
            logging.info(f"Sell Order Executed: {order}")
    except Exception as e:
        logging.error(f"Error executing {order_type} order: {e}")

# Main Loop
def main():
    logging.info("Bot Started...")
    while True:
        candles = fetch_candles()
        if candles:
            signal = simple_strategy(candles)
            logging.info(f"Signal: {signal}")
            if signal in ['BUY', 'SELL']:
                execute_order(signal)
        time.sleep(60)  # Delay 1 Menit

if __name__ == '__main__':
    main()
