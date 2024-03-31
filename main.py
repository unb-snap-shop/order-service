from flask_cors import CORS
from src import create_app

order_service_app = create_app()
CORS(order_service_app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

if __name__ == "__main__":
    order_service_app.run(debug=True, port=5001)
