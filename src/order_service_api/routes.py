from flask import Flask, Blueprint, request, jsonify
from ..utils.manage_cart import write_json
from ..observers.ui_observer import UIObserver

order_service_api = Blueprint('order_service_api', __name__)

ui_observer = UIObserver()

@order_service_api.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.json  # json from UI
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    # Perform validation
    if not product_id or not quantity:
        return jsonify({'error': 'Invalid request'}), 400

    # Add product to cart (pseudocode)
    # cart.add_product(product_id, quantity)
    # Update database with new cart information
    write_json(data)
    ui_observer.update('Product added to cart successfully')
    return jsonify({'message': 'Product added to cart successfully'}), 200

@order_service_api.route('/test', methods=['GET'])
def test_endpoint():
    return "endpoint test hit -- Eric", 200