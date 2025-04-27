from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/nifty-option-chain', methods=['GET'])
def get_option_chain():
    session = requests.Session()

    headers = {
        "Host": "www.nseindia.com",
        "Referer": "https://www.nseindia.com/option-chain",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/90.0.4430.212 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    # Step 1: Access the NSE homepage to set cookies
    try:
        homepage_url = "https://www.nseindia.com"
        session.get(homepage_url, headers=headers, timeout=10)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to access NSE homepage", "details": str(e)}), 500

    # Step 2: Access the option chain API
    option_chain_url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    try:
        response = session.get(option_chain_url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch option chain data", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
