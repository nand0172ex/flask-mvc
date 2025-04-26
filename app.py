import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/nifty-option-chain', methods=['GET'])
def get_option_chain():
    try:
        url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': 'application/json,text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'https://www.nseindia.com/option-chain',
            'Connection': 'keep-alive',
            'Host': 'www.nseindia.com'
        }
        session = requests.Session()
        
        # Pehle homepage hit karte hain taaki cookies mil jaye
        session.get('https://www.nseindia.com', headers=headers, timeout=5)
        
        # Ab original API call karte hain with cookies
        response = session.get(url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Failed to fetch option chain", "status_code": response.status_code})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
