# Foodie_ECommerce_V1.0/app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_session import Session
from flask_cors import CORS

# Extensiones
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
sess = Session()

def create_app(secret_key="super_secret_key"):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    app = Flask(
        __name__,
        template_folder=os.path.join(BASE_DIR, 'templates'),
        static_folder=os.path.join(BASE_DIR, 'static')
    )

    # Configuraciones
    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SESSION_TYPE'] = 'filesystem'

    # Inicializa extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    sess.init_app(app)
    CORS(app)

    # Configura login_manager
    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info'

    from .models import UserModel

    @login_manager.user_loader
    def load_user(user_id):
        return UserModel.query.get(user_id)

    # Blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
