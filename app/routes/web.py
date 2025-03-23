from flask import Blueprint, render_template
from app.controllers.aws.price_controller import pricing_bp  # Import the pricing API blueprint

# Define Blueprint for web routes
web_bp = Blueprint("web", __name__)

# Register AWS pricing blueprint under '/aws' route
web_bp.register_blueprint(pricing_bp, url_prefix="/aws")

@web_bp.route("/pricing")
def pricing_ui():
    """
    Serves the AWS EC2 Pricing UI page.
    Accessible at: http://127.0.0.1:5000/pricing
    """
    return render_template("aws/pricing.html")

