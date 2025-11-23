# Foodie_ECommerce_V1.0/app/api/checkout_api.py

from flask import request, jsonify, session
from app.api import api_blueprint
from services.payment_processor import process_payment_mock
from services.delivery_geo import calculate_delivery_cost
from app.models import Order
from services.db_firestore import save_order


@api_blueprint.route('/checkout/validate', methods=['POST'])
def validate_checkout():
    """Valida los datos de envío y calcula el costo final."""
    data = request.json
    cart = session.get('cart', [])

    if not cart:
        return jsonify({'success': False, 'message': 'El carrito está vacío.'}), 400

    address = data.get('address')
    # Lógica de validación de datos (email, teléfono, etc.)
    if not address or not data.get('user_email'):
        return jsonify({'success': False, 'message': 'Faltan datos de envío o contacto.'}), 400

    # 1. Calcular el subtotal del carrito
    subtotal = sum(item['item_total'] for item in cart)

    # 2. Calcular el costo de envío (usando el servicio mock)
    try:
        shipping_cost = calculate_delivery_cost(address['zip_code'])
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

    # 3. Calcular el total final
    total_amount = subtotal + shipping_cost

    return jsonify({
        'success': True,
        'subtotal': round(subtotal, 2),
        'shipping_cost': round(shipping_cost, 2),
        'total_amount': round(total_amount, 2),
        'message': 'Datos validados. Listo para pagar.'
    })


@api_blueprint.route('/checkout/confirm', methods=['POST'])
def confirm_order():
    """Procesa el pago y guarda la orden."""
    data = request.json
    cart = session.get('cart', [])
    user_id = session.get('user_id', 'guest_123')

    if not cart:
        return jsonify({'success': False, 'message': 'El carrito está vacío.'}), 400

    # 1. Obtener el monto total y datos de pago
    total_amount = data.get('total_amount')
    payment_token = data.get('payment_token')  # Token generado por Niubiz/MP en el Frontend

    if not payment_token:
        return jsonify({'success': False, 'message': 'Token de pago es requerido.'}), 400

    # 2. Procesar el pago (usando el servicio mock)
    payment_result = process_payment_mock(total_amount, payment_token)

    if payment_result['status'] == 'success':
        # 3. Crear el objeto de Orden
        new_order = Order(
            id='ORD_' + payment_result['transaction_id'],
            user_id=user_id,
            items=cart,
            # Esto debería ser una lista de objetos CartItem (usaremos el dict de la sesión por simplicidad)
            total_amount=total_amount,
            shipping_address=data.get('address'),
            payment_status='paid',
            delivery_status='new',
            created_at=payment_result['timestamp']
        )

        # 4. Guardar la orden en Firestore (usando el servicio mock/real)
        order_id = save_order(vars(new_order))

        # 5. Limpiar el carrito y notificar (simulado)
        session.pop('cart', None)
        # notification_manager.send_confirmation_email(new_order) # Llamada simulada

        return jsonify({
            'success': True,
            'message': 'Pago exitoso y orden confirmada.',
            'order_id': order_id
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Error en el procesamiento del pago.',
            'error_details': payment_result['error']
        }), 400
