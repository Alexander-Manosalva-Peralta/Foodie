# Model definitions (example using dataclasses)
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class User:
    id: str
    email: str
    name: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class Ingredient:
    id: str
    name: str
    icon: Optional[str] = None

@dataclass
class Product:
    id: str
    name: str
    description: str
    price_cents: int
    ingredients: List[Ingredient] = field(default_factory=list)

@dataclass
class Order:
    id: str
    user_id: str
    product_ids: List[str]
    total_cents: int
    created_at: datetime = field(default_factory=datetime.utcnow)
