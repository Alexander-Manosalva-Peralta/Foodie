# Foodie_ECommerce_V1.0/app/models.py
from dataclasses import dataclass, field
from typing import List, Optional
from . import db
from flask_login import UserMixin

# ----------------- MODELOS SQLALCHEMY -----------------
class ProductModel(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300))
    base_price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200))
    is_customizable = db.Column(db.Boolean, default=False)

class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100))
    password = db.Column(db.String(200))
    address = db.Column(db.JSON)
    phone = db.Column(db.String(50))

class OrderModel(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('users.id'))
    items = db.Column(db.JSON)
    total_amount = db.Column(db.Float)
    shipping_address = db.Column(db.JSON)
    payment_status = db.Column(db.String(50))
    delivery_status = db.Column(db.String(50))
    created_at = db.Column(db.String(50))

# ----------------- DATACLASS PARA MOCKS -----------------
@dataclass
class Ingredient:
    id: str
    name: str
    price: float
    stock: int
    category: str  # 'Base', 'Proteína', 'Salsa', etc.

@dataclass
class Product:
    id: str
    name: str
    description: str
    base_price: float
    image_url: str
    is_customizable: bool

@dataclass
class CartItem:
    product_id: str
    name: str
    unit_price: float
    quantity: int
    customization_details: Optional[List[Ingredient]] = field(default_factory=list)
    item_total: float = 0.0

    def __post_init__(self):
        """Calcula el total del ítem considerando personalización."""
        custom_price = sum(ing.price for ing in self.customization_details)
        self.item_total = (self.unit_price + custom_price) * self.quantity

@dataclass
class Order:
    id: str
    user_id: str
    items: List[CartItem]
    total_amount: float
    shipping_address: dict
    payment_status: str  # 'pending', 'paid', 'failed'
    delivery_status: str  # 'new', 'preparing', 'shipped', 'delivered'
    created_at: str  # Timestamp

# ----------------- FUNCIONES MOCK -----------------
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
    ]
