from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "NIFTY Option Chain API Running 🚀"

@app.route('/nifty-option-chain')
def get_option_chain():
    try:
        session = requests.Session()
        session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
        })

        # Pehle NSE ki main site hit karo cookies generate karne ke liye
        homepage = session.get("https://www.nseindia.com", timeout=10)
        
        if homepage.status_code != 200:
            return jsonify({"error": "Unable to fetch NSE homepage for session."}), 500

        # Ab actual API call karo
        api_url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
        api_response = session.get(api_url, timeout=10)

        if api_response.status_code != 200:
            return jsonify({"error": "Unable to fetch option chain data."}), 500

        data = api_response.json()

        # Sirf current expiry ka data filter karo
        current_expiry = data['records']['expiryDates'][0]
        filtered_data = []

        for record in data['records']['data']:
            if record['expiryDate'] == current_expiry:
                filtered_data.append(record)

        return jsonify(filtered_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
