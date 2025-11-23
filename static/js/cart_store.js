// Foodie_ECommerce_V1.0/static/js/cart_store.js

/**
 * Gestión del estado del carrito en el lado del cliente (Frontend).
 * Se comunica con las APIs de Flask para persistir cambios.
 */

document.addEventListener('DOMContentLoaded', () => {
    updateCartDisplay();
});

/**
 * Llama a la API para obtener el estado actual del carrito y actualiza el contador.
 */
function updateCartDisplay() {
    fetch('/api/v1/cart')
        .then(response => response.json())
        .then(data => {
            const countElement = document.getElementById('cart-count');
            if (countElement && data.success) {
                // Suma las cantidades de todos los ítems para el contador
                const totalCount = data.cart_items.reduce((acc, item) => acc + item.quantity, 0);
                countElement.textContent = totalCount;
            }
        })
        .catch(error => console.error('Error al obtener el carrito:', error));
}

/**
 * Añade un ítem al carrito a través de la API.
 * @param {object} itemData - Datos del ítem: { product_id, quantity, customization: [...] }
 */
function addToCart(itemData) {
    fetch('/api/v1/cart/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(itemData),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            console.log('Producto añadido/actualizado:', data.message);
            updateCartDisplay();
        } else {
            alert('Error al añadir al carrito: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error de red al añadir al carrito:', error);
        alert('Ocurrió un error de conexión.');
    });
}