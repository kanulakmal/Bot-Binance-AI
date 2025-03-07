# webhook.py
from flask import Flask, request, jsonify
from bot import place_order

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if not data:
        return jsonify({'error': 'No data received'}), 400

    signal = data.get('signal')
    if signal == 'BUY':
        place_order('BUY')
        return jsonify({'message': 'Buy order executed'}), 200
    elif signal == 'SELL':
        place_order('SELL')
        return jsonify({'message': 'Sell order executed'}), 200
    else:
        return jsonify({'error': 'Invalid signal'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
