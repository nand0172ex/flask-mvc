from flask import Blueprint, render_template

# Create a Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)

# Route for Login Page
@auth_bp.route('/login')
def login():
    return render_template('auth/login.html')

# Route for Signup Page
@auth_bp.route('/signup')
def signup():
    return render_template('auth/signup.html')
