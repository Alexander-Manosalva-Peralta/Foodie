# Foodie_ECommerce_V1.0/app/api/__init__.py

from flask import Blueprint

# Crea un Blueprint para todas las rutas de la API
api_blueprint = Blueprint('api', __name__)

# Importa y registra los controladores de la API
from .cart_api import *
from .checkout_api import *
