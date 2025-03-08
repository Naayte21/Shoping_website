from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()  # Initialize SQLAlchemy once
migrate = Migrate()  # Initialize Flask-Migrate once

def create_app():
    app = Flask(__name__)

    # Database Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize Extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    from .routes import main
    app.register_blueprint(main)

    return app
