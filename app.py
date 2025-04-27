import requests

def fetch_nifty_option_chain():
    session = requests.Session()

    # Common headers
    headers = {
        "Host": "www.nseindia.com",
        "Referer": "https://www.nseindia.com/option-chain",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    # Step 1: Access homepage to set cookies
    homepage_url = "https://www.nseindia.com"
    session.get(homepage_url, headers=headers, timeout=10)

    # Step 2: Now access option chain API
    option_chain_url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

    response = session.get(option_chain_url, headers=headers, timeout=10)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data", "status_code": response.status_code}

# Example usage
if __name__ == "__main__":
    data = fetch_nifty_option_chain()
    print(data)
