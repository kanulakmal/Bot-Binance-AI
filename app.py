from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Binance Bot AI!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Data Webhook:", data)
    return {"status": "success"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
