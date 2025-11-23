import os
from flask import Flask

def create_app(secret_key):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    app = Flask(
        __name__,
        template_folder=os.path.join(BASE_DIR, 'templates'),
        static_folder=os.path.join(BASE_DIR, 'static')
    )

    app.config['SECRET_KEY'] = secret_key
    app.config['DEBUG'] = True

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
