from flask import Flask, Blueprint, request, jsonify, make_response
from ..utils.manage_cart import write_json, get_json
from ..observers.ui_observer import UIObserver
from flask_cors import CORS

order_service_api = Blueprint('order_service_api', __name__)

CORS(order_service_api)

ui_observer = UIObserver()

@order_service_api.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.json  # json from UI
    product_id = data.get('productId')
    product_brand = data.get('productBrand')
    product_name = data.get('productName')
    product_price = data.get('productPrice')

    

    # Perform validation
    if not product_id or not product_brand or not product_name or not product_price:
        return jsonify({'error': 'Invalid request'}), 400

    # Add product to cart (pseudocode)
    # cart.add_product(product_id, quantity)
    # Update database with new cart information
    write_json(data)
    ui_observer.update('Product added to cart successfully')
    response = make_response(jsonify({'message': 'Product added to cart successfully'}), 200)
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response


@order_service_api.route('/get_cart', methods=['GET'])
def get_cart_contents():
    cart = get_json()
    response = make_response(jsonify(cart))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@order_service_api.route('/test', methods=['GET'])
def test_endpoint():
    response = make_response(jsonify("endpoint test hit -- Eric"))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200