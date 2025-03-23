import boto3
from flask import Blueprint, jsonify, json, request
from flask import Blueprint, jsonify, render_template
pricing_bp = Blueprint("pricing", __name__)

@pricing_bp.route("/aws/pricing/ec2", methods=["GET"])
def get_ec2_pricing():
    try:
        client = boto3.client("pricing", region_name="us-east-1")
        next_token = None
        ec2_prices = []
        limit = int(request.args.get("limit", 50))  # Default limit per page
        page = int(request.args.get("page", 1))  # Page number

        while len(ec2_prices) < limit * page:
            params = {"ServiceCode": "AmazonEC2"}
            if next_token:
                params["NextToken"] = next_token

            response = client.get_products(**params)

            for price in response["PriceList"]:
                data = json.loads(price)
                instance = {
                    "instanceType": data["product"]["attributes"].get("instanceType", "N/A"),
                    "vCPU": data["product"]["attributes"].get("vcpu", "N/A"),
                    "memory": data["product"]["attributes"].get("memory", "N/A"),
                    "OnDemand": extract_on_demand_price(data["terms"].get("OnDemand", {}))
                }
                ec2_prices.append(instance)

                if len(ec2_prices) >= limit * page:
                    break  # Stop once we reach the required data

            next_token = response.get("NextToken")
            if not next_token:
                break

        # Paginate results
        start_idx = (page - 1) * limit
        end_idx = page * limit
        paginated_prices = ec2_prices[start_idx:end_idx]

        return jsonify({
            "prices": paginated_prices,
            "total_instances": len(ec2_prices),
            "page": page,
            "limit": limit
        })

    except Exception as e:
        return jsonify({"error": str(e)})


def extract_on_demand_price(on_demand_data):
    """Extracts the On-Demand pricing value from AWS response."""
    if not on_demand_data:
        return "N/A"

    for term in on_demand_data.values():
        for price_dim in term["priceDimensions"].values():
            return f"${price_dim['pricePerUnit'].get('USD', '0.00')}"

    return "N/A"

@pricing_bp.route("/ui", methods=["GET"])
def pricing_ui():
    return render_template("aws/pricing.html")

# Manual mapping of AWS region codes to human-readable names
AWS_REGION_NAMES = {
    "us-east-1": "US East (N. Virginia)",
    "us-east-2": "US East (Ohio)",
    "us-west-1": "US West (N. California)",
    "us-west-2": "US West (Oregon)",
    "ap-south-1": "Asia Pacific (Mumbai)",
    "ap-northeast-1": "Asia Pacific (Tokyo)",
    "ap-northeast-2": "Asia Pacific (Seoul)",
    "ap-southeast-1": "Asia Pacific (Singapore)",
    "ap-southeast-2": "Asia Pacific (Sydney)",
    "ca-central-1": "Canada (Central)",
    "eu-central-1": "Europe (Frankfurt)",
    "eu-west-1": "Europe (Ireland)",
    "eu-west-2": "Europe (London)",
    "eu-west-3": "Europe (Paris)",
    "sa-east-1": "South America (São Paulo)"
}

@pricing_bp.route("/aws/regions", methods=["GET"])
def get_aws_regions():
    try:
        ec2 = boto3.client("ec2")
        regions = ec2.describe_regions()["Regions"]

        region_list = [
            {
                "code": r["RegionName"],
                "name": AWS_REGION_NAMES.get(r["RegionName"], r["RegionName"])  # Use manual mapping
            }
            for r in regions
        ]

        return jsonify({"regions": region_list})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@pricing_bp.route('/aws-pricing')
def aws_pricing():
    return render_template('aws/aws_pricing.html')