from flask import Flask
from app.api.routes import api_bp  # Importa el blueprint de rutas de la API


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret_key'

    app.register_blueprint(api_bp)

    return app
