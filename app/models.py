# Foodie_ECommerce_V1.0/app/models.py

from dataclasses import dataclass, field
from typing import List, Optional

# --- Definición de Modelos de Datos (Usando dataclasses para claridad) ---

@dataclass
class Ingredient:
    """Modelo para un ingrediente."""
    id: str
    name: str
    price: float
    stock: int
    category: str # e.g., 'Base', 'Proteína', 'Salsa'

@dataclass
class Product:
    """Modelo para un producto (plato predefinido o base)."""
    id: str
    name: str
    description: str
    base_price: float
    image_url: str
    is_customizable: bool

@dataclass
class User:
    """Modelo para un usuario."""
    id: str
    email: str
    name: str
    address: Optional[dict] = None
    phone: Optional[str] = None

@dataclass
class CartItem:
    """Modelo para un item dentro del carrito."""
    product_id: str
    name: str
    unit_price: float
    quantity: int
    customization_details: Optional[List[Ingredient]] = field(default_factory=list)
    item_total: float = 0.0

    def _post_init_(self):
        # Calcula el total del ítem (precio base + precio de ingredientes * cantidad)
        custom_price = sum(ing.price for ing in self.customization_details)
        self.item_total = (self.unit_price + custom_price) * self.quantity

@dataclass
class Order:
    """Modelo para una orden de compra."""
    id: str
    user_id: str
    items: List[CartItem]
    total_amount: float
    shipping_address: dict
    payment_status: str # 'pending', 'paid', 'failed'
    delivery_status: str # 'new', 'preparing', 'shipped', 'delivered'
    created_at: str # Timestamp

# --- Funciones Mock (Simulación de datos) ---

def get_mock_products() -> List[Product]:
    """Retorna una lista de productos mock para el catálogo."""
    return [
        Product(
            id='p001',
            name='Bowl de Salmón Oriental',
            description='Salmón fresco con arroz de sushi, aguacate y salsa teriyaki.',
            base_price=35.50,
            image_url='/static/assets/product_images/salmon_bowl.webp',
            is_customizable=True
        ),
        Product(
            id='p002',
            name='Pizza Artesanal Vegana',
            description='Masa madre, pesto, queso de almendra y vegetales de estación.',
            base_price=45.00,
            image_url='/static/assets/product_images/vegan_pizza.webp',
            is_customizable=False
        ),
        # Más productos...
    ]