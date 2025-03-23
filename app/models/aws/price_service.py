import requests

def fetch_ec2_pricing():
    try:
        # Mock AWS pricing API response
        response = requests.get("https://pricing.api.example.com/aws/ec2")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch pricing: {str(e)}"}
