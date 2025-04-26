import requests
from flask import Flask, jsonify
from datetime import datetime
from time import sleep

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
        session.get('https://www.nseindia.com', headers=headers, timeout=15)
        
        # Retry logic to handle timeout error
        retries = 3
        for attempt in range(retries):
            try:
                # Fetch the option chain data
                response = session.get(url, headers=headers, timeout=15)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # Extract expiry dates and filter current expiry date
                    expiry_dates = data['records']['expiryDates']
                    today = datetime.today().date()

                    # Find the nearest expiry date (current expiry)
                    current_expiry = min(expiry_dates, key=lambda x: abs(datetime.strptime(x, '%d-%b-%Y').date() - today))

                    # Filter option chain data for the current expiry
                    option_data = data['records']['data']
                    current_expiry_data = None
                    for item in option_data:
                        if current_expiry in item['expiryDate']:
                            current_expiry_data = item
                            break

                    if current_expiry_data:
                        return jsonify(current_expiry_data)
                    else:
                        return jsonify({"error": "No data found for the current expiry."})

                else:
                    return jsonify({"error": "Failed to fetch option chain data", "status_code": response.status_code})
            except requests.exceptions.RequestException as e:
                if attempt < retries - 1:
                    sleep(5)  # Wait for 5 seconds before retry
                else:
                    return jsonify({"error": f"Request failed after {retries} attempts: {str(e)}"})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
