# Foodie_ECommerce_V1.0/app/_init_.py

from flask import Flask


def create_app(secret_key):
    # Inicializa la aplicación Flask
    app = Flask(_name_)

    # Configuración de la aplicación
    app.config['SECRET_KEY'] = secret_key
    app.config['DEBUG'] = True  # Solo para desarrollo

    # --- Inicialización de Modelos y Servicios ---
    # Nota: No inicializamos la DB aquí directamente, sino dentro de services/

    # --- Registro de Blueprints (Controladores) ---

    # Rutas Principales
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Rutas de la API (JSON Endpoints)
    from .api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app