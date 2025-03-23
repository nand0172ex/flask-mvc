import boto3
import json
import os
import sys

# Unbuffered output for real-time progress
sys.stdout.reconfigure(line_buffering=True)

# List of AWS regions to fetch pricing for
REGIONS = ["eu-central-1"]

def fetch_ec2_pricing(region):
    """Fetch EC2 pricing for a given AWS region and save it as a JSON file."""
    client = boto3.client('pricing', region_name='eu-central-1')  # Pricing API only in us-east-1

    all_data = []
    next_token = None
    batch_count = 0  # Track number of API calls

    print(f"🔄 Fetching pricing for region: {region}")

    while True:
        batch_count += 1
        if next_token:
            response = client.get_products(
                ServiceCode='AmazonEC2',
                Filters=[{'Type': 'TERM_MATCH', 'Field': 'regionCode', 'Value': region}],
                NextToken=next_token
            )
        else:
            response = client.get_products(
                ServiceCode='AmazonEC2',
                Filters=[{'Type': 'TERM_MATCH', 'Field': 'regionCode', 'Value': region}]
            )

        all_data.extend([json.loads(item) for item in response['PriceList']])
        
        # Print progress update
        print(f"✅ Batch {batch_count}: Fetched {len(response['PriceList'])} items (Total: {len(all_data)})")

        # Check if there's another page
        next_token = response.get('NextToken')
        if not next_token:
            break

    # Ensure the 'pricing_data' folder exists
    os.makedirs("app/models/aws/pricing_data", exist_ok=True)

    # Save data as region-specific JSON
    file_path = f"app/models/aws/pricing_data/{region}.json"
    with open(file_path, "w") as f:
        json.dump(all_data, f, indent=4)

    print(f"🎯 Pricing data saved: {file_path} ({len(all_data)} entries)")

# Fetch pricing for all regions
for region in REGIONS:
    fetch_ec2_pricing(region)
