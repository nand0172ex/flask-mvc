from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/nifty-option-chain')
def get_option_chain():
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json",
        "Referer": "https://www.nseindia.com/",
        "Connection": "keep-alive"
    }
    response = requests.get(url, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
