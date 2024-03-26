from flask import Flask
from flask_cors import CORS
from .order_service_api.routes import order_service_api




def create_app():
    # setup app
    order_service_app = Flask(__name__)

    order_service_app.register_blueprint(order_service_api)



    # configure cors
    # CORS(order_service_app, resources={r"/api/*": {
    #     "origins": "http://localhost:3000",
    #     "methods": ["GET", "POST", "PUT", "DELETE"],
    #     "allow_headers": ['Content-Type', 'Authorization'],
    #     "supports_credentials": True,
    #     "max_age": 3600,
    # }})


    return order_service_app