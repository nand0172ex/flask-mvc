from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder=os.path.abspath('app/views'))  # Set correct template path
    app.config.from_object('config.Config')

    db.init_app(app)

    # Import and register Blueprints
    from app.controllers.auth.auth_controller import auth_bp
    from app.controllers.home.home_controller import home_bp

    app.register_blueprint(home_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
