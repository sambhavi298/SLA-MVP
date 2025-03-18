from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from pymongo import MongoClient
import logging

def create_app():
    app = Flask(__name__)
    load_dotenv()

    # Load MongoDB URI from .env
    mongo_uri = os.getenv('MONGO_URI')
    app.config['DB'] = MongoClient(mongo_uri)['sla_db']

    CORS(app)

    # Register Blueprints
    from app.routes.health_routes import health_bp
    from app.routes.debug_routes import debug_bp
    from app.routes.optimize_routes import optimize_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(debug_bp)
    app.register_blueprint(optimize_bp)

    # Register error handlers
    from app.error_handlers import register_error_handlers
    register_error_handlers(app)

    # Logger setup
    logging.basicConfig(level=logging.INFO)
    app.logger.info('Application started successfully')

    return app