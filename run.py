# Foodie_ECommerce_V1.0/run.py

from app import create_app
from dotenv import load_dotenv
import os

# Carga las variables de entorno del archivo .env
load_dotenv()

# Obtiene el valor de la clave secreta
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')

# Crea la instancia de la aplicación Flask
app = create_app(secret_key=SECRET_KEY)

if _name_ == '_main_':
    # Ejecuta la aplicación en modo debug para desarrollo
    print("Iniciando Foodie E-Commerce...")
    app.run(debug=True)