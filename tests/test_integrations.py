# Foodie_ECommerce_V1.0/tests/test_integrations.py

import unittest
import os
import sys

# Añadir el directorio raíz para importar app y services
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))

from app import create_app


class TestAPIIntegrations(unittest.TestCase):

    def setUp(self):
        # 1. Configurar la aplicación en modo testing
        self.app = create_app(secret_key='test-secret-key')
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        # 2. Inicializar la sesión de prueba (necesaria para el carrito)
        with self.client.session_transaction() as session:
            session['cart'] = []
            session['user_id'] = 'test_user'

    def test_home_page_status(self):
        """La página de inicio debe cargar correctamente."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Foodie Co.', response.data)

    def test_add_to_cart_success(self):
        """Añadir un producto al carrito debe retornar éxito."""
        response = self.client.post('/api/v1/cart/add', json={
            'product_id': 'p999',
            'quantity': 2
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['cart_count'], 2)

    def test_add_to_cart_invalid_data(self):
        """Añadir sin product_id debe retornar error 400."""
        response = self.client.post('/api/v1/cart/add', json={'quantity': 1})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertFalse(data['success'])

    def test_full_checkout_mock_success(self):
        """El proceso de pago completo simulado debe ser exitoso."""
        # 1. Asegurar que el carrito tiene ítems
        self.client.post('/api/v1/cart/add', json={
            'product_id': 'p998',
            'quantity': 1
        })

        # 2. Validar el checkout
        validation_response = self.client.post('/api/v1/checkout/validate', json={
            'user_email': 'test@foodie.com',
            'address': {'street': 'Av. Test', 'zip_code': '18000'}
        })
        self.assertEqual(validation_response.status_code, 200)
        validation_data = validation_response.get_json()
        self.assertTrue(validation_data['success'])
        total_amount = validation_data['total_amount']

        # 3. Confirmar la orden con token de pago simulado
        confirm_response = self.client.post('/api/v1/checkout/confirm', json={
            'total_amount': total_amount,
            'payment_token': 'SUCCESS_TOKEN_123',
            'address': {'street': 'Av. Test', 'zip_code': '18000'}
        })
        self.assertEqual(confirm_response.status_code, 200)
        confirm_data = confirm_response.get_json()
        self.assertTrue(confirm_data['success'])
        self.assertIn('ORD_', confirm_data['order_id'])


if _name_ == '_main_':
    unittest.main()