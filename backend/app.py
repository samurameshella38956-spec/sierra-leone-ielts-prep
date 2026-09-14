import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from config import config, setup_logging

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_name=None):
    """Application factory pattern"""
    config_name = config_name or os.getenv("FLASK_CONFIG", "development")
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Logging
    setup_logging(app)

    # Register routes
    from routes import auth, exam, payment, scholarship
    app.register_blueprint(auth.bp)
    app.register_blueprint(exam.bp)
    app.register_blueprint(payment.bp)
    app.register_blueprint(scholarship.bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
