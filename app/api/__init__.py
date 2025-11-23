# Foodie_ECommerce_V1.0/app/api/_init_.py

from flask import Blueprint

# Crea un Blueprint para todas las rutas de la API
api_blueprint = Blueprint('api', _name_)

# Importa y registra los controladores de la API
from .cart_api import *
from .checkout_api import *