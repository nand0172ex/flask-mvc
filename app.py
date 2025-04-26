from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "NIFTY Option Chain API Running 🚀"

@app.route('/nifty-option-chain')
def get_option_chain():
    try:
        # Session create
        session = requests.Session()

        # Headers set karo
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": "application/json",
            "Connection": "keep-alive",
            "Referer": "https://www.nseindia.com/",
            "Host": "www.nseindia.com"
        }

        session.headers.update(headers)

        # Pehle homepage hit karo cookies ke liye
        homepage = session.get("https://www.nseindia.com", timeout=10)

        if homepage.status_code != 200:
            return jsonify({"error": "Unable to load NSE homepage."}), 500

        # Ab option chain API hit karo with session
        api_url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
        response = session.get(api_url, timeout=10)

        if response.status_code != 200:
            return jsonify({"error": "Unable to fetch option chain data.", "status_code": response.status_code}), 500

        data = response.json()

        # Sirf current expiry ka data
        current_expiry = data['records']['expiryDates'][0]
        filtered_data = [
            record for record in data['records']['data']
            if record['expiryDate'] == current_expiry
        ]

        return jsonify(filtered_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
