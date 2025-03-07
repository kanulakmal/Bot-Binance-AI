import os

# API Key & Secret dari Binance
BINANCE_API_KEY = os.getenv("kAawOsaLo73u9OjG3sbGcyBCq5Gg8gSssUkiUZR4sM34qo3czcW99tob2G2BRwfK", "your_api_key_here")
BINANCE_API_SECRET = os.getenv("x5ZbUVpI9¡Cj0yaROIVrm6YQ6LYovId3LZVYJCxMXQMQmf3BNUoZq&SOljc", "your_api_secret_here")

# Pair trading & timeframe
TRADE_PAIR = "BTCUSDT"
TIMEFRAME = "15m"

# Risk Management
TRADE_AMOUNT = 50  # Jumlah USDT per trade
STOP_LOSS = 0.02   # Stop loss 2%
TAKE_PROFIT = 0.05  # Take profit 5%
