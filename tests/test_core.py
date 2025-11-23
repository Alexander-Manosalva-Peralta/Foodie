# Foodie_ECommerce_V1.0/tests/test_core.py

import unittest
from app.models import CartItem, Product
from app.models import Ingredient


class TestCoreLogic(unittest.TestCase):

    def setUp(self):
        # Crear un producto base para las pruebas
        self.base_product = Product(
            id='p100',
            name='Test Base Bowl',
            description='Base para pruebas',
            base_price=10.00,
            image_url='',
            is_customizable=True
        )

        # Crear ingredientes para pruebas
        self.ing_cheese = Ingredient(id='i01', name='Cheese', price=2.50, stock=50, category='Extra')
        self.ing_avocado = Ingredient(id='i02', name='Avocado', price=3.00, stock=20, category='Extra')

    def test_cart_item_total_calculation(self):
        """Verifica que el cálculo del total del item del carrito sea correcto."""

        # Caso 1: Item sin personalización, cantidad 1
        item1 = CartItem(
            product_id=self.base_product.id,
            name=self.base_product.name,
            unit_price=self.base_product.base_price,
            quantity=1
        )
        # 10.00 * 1 = 10.00
        self.assertEqual(item1.item_total, 10.00)

        # Caso 2: Item con personalización, cantidad 1
        item2 = CartItem(
            product_id=self.base_product.id,
            name=self.base_product.name,
            unit_price=self.base_product.base_price,
            quantity=1,
            customization_details=[self.ing_cheese, self.ing_avocado]
        )
        # (10.00 + 2.50 + 3.00) * 1 = 15.50
        self.assertEqual(item2.item_total, 15.50)

        # Caso 3: Item con personalización, cantidad 3
        item3 = CartItem(
            product_id=self.base_product.id,
            name=self.base_product.name,
            unit_price=self.base_product.base_price,
            quantity=3,
            customization_details=[self.ing_cheese]
        )
        # (10.00 + 2.50) * 3 = 37.50
        self.assertEqual(item3.item_total, 37.50)


if _name_ == '_main_':
    unittest.main()