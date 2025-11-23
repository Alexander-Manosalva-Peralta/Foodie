from flask import Blueprint, request, jsonify

bp = Blueprint('cart_api', __name__, url_prefix='/api/cart')

@bp.route('/add', methods=['POST'])
def add_to_cart():
    payload = request.get_json()
    # implement add logic
    return jsonify({"status":"ok","received": payload})

@bp.route('/remove', methods=['POST'])
def remove_from_cart():
    payload = request.get_json()
    return jsonify({"status":"ok","received": payload})
