from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS
from app.controllers.aws.price_controller import pricing_bp


db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder=os.path.abspath('app/views'))  # Set correct template path
    CORS(app)
    app.config.from_object('config.Config')
    
    db.init_app(app)

    # Import and register Blueprints
    from app.controllers.auth.auth_controller import auth_bp
    from app.controllers.home.home_controller import home_bp
    # from app.controllers.aws.price_controller import price_bp
    
    app.register_blueprint(pricing_bp)
    # from app.routes.web import web_bp
   # Register Blueprints
    # app.register_blueprint(web_bp)
    # app.register_blueprint(price_bp)
    app.register_blueprint(home_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
