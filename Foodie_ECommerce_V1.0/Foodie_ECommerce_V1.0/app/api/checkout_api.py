from flask import Blueprint, request, jsonify

bp = Blueprint('checkout_api', __name__, url_prefix='/api/checkout')

@bp.route('/start', methods=['POST'])
def start_checkout():
    data = request.get_json()
    # validate order, call payment processor service, etc.
    return jsonify({"status":"started","data": data})
