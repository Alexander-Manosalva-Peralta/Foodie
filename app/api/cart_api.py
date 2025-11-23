# Foodie_ECommerce_V1.0/app/api/cart_api.py

from flask import request, jsonify, session
from app.api import api_blueprint
from app.models import CartItem


# NOTA: En un entorno real, el carrito se persistiría en la DB o caché (Redis).
# Aquí se usa la sesión de Flask por simplicidad.

@api_blueprint.route('/cart/add', methods=['POST'])
def add_to_cart():
    """Añade un ítem al carrito o actualiza su cantidad."""
    data = request.json
    product_id = data.get('product_id')
    quantity = int(data.get('quantity', 1))

    if not product_id or quantity <= 0:
        return jsonify({'success': False, 'message': 'Datos inválidos.'}), 400

    # Lógica de obtención de producto real (simulación)
    item_data = {
        'product_id': product_id,
        'name': f'Item {product_id}',  # Nombre real obtenido de DB
        'unit_price': 20.00,  # Precio real obtenido de DB
        'quantity': quantity,
        'customization_details': data.get('customization', [])  # Si aplica
    }

    # Crea el objeto CartItem y calcula el total
    try:
        new_item = CartItem(**item_data)
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error al crear ítem: {e}'}), 400

    cart = session.get('cart', [])
    # Revisa si el producto ya está en el carrito (simplificación: no considera personalización para IDs iguales)
    found = False
    for item in cart:
        if item['product_id'] == product_id:
            item['quantity'] += quantity
            # Recalcular el total del ítem (no necesario si se recalcula en el post-init)
            found = True
            break

    if not found:
        cart.append(vars(new_item))  # Convierte el dataclass a dict para la sesión

    session['cart'] = cart
    # Recalcular el total general del carrito (lo haríamos en una función aparte en un proyecto grande)
    total_items = sum(item['quantity'] for item in cart)

    return jsonify({
        'success': True,
        'message': 'Producto añadido al carrito.',
        'cart_count': total_items
    })


@api_blueprint.route('/cart/remove/<string:product_id>', methods=['DELETE'])
def remove_from_cart(product_id):
    """Elimina un ítem del carrito."""
    cart = session.get('cart', [])
    # Filtrar el carrito para eliminar el producto
    new_cart = [item for item in cart if item['product_id'] != product_id]

    if len(new_cart) < len(cart):
        session['cart'] = new_cart
        total_items = sum(item['quantity'] for item in new_cart)
        return jsonify({
            'success': True,
            'message': 'Producto eliminado del carrito.',
            'cart_count': total_items
        })

    return jsonify({'success': False, 'message': 'Producto no encontrado en el carrito.'}), 404


@api_blueprint.route('/cart', methods=['GET'])
def get_cart():
    """Obtiene el contenido actual del carrito."""
    cart = session.get('cart', [])
    total = sum(item['item_total'] for item in cart)
    return jsonify({
        'success': True,
        'cart_items': cart,
        'cart_total': round(total, 2)
    })
