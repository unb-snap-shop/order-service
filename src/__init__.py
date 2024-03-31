from flask import Flask
from flask_cors import CORS
from .order_service_api.routes import order_service_api


def create_app():
    # setup app
    order_service_app = Flask(__name__)

    order_service_app.register_blueprint(order_service_api)

    return order_service_app
