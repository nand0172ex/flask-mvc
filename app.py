from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "NIFTY Option Chain API Running 🚀"

@app.route('/nifty-option-chain')
def get_option_chain():
    try:
        url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept": "application/json",
            "Referer": "https://www.nseindia.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
        }
        
        session = requests.Session()
        session.headers.update(headers)

        # Send a HEAD request to nseindia to set cookies
        session.get("https://www.nseindia.com", timeout=5)

        response = session.get(url, timeout=10)
        data = response.json()

        # Sirf current expiry date ka data nikalna
        current_expiry = data['records']['expiryDates'][0]
        filtered_data = []

        for record in data['records']['data']:
            if record['expiryDate'] == current_expiry:
                filtered_data.append(record)

        return jsonify(filtered_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
