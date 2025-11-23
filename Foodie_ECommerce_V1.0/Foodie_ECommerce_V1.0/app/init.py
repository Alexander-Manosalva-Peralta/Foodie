from flask import Flask
from .routes import register_routes

def create_app(config_object=None):
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_mapping(
        SECRET_KEY="change-me",
        FIRESTORE_PROJECT="your-firestore-project-id",
    )
    if config_object:
        app.config.from_object(config_object)
    register_routes(app)
    return app
