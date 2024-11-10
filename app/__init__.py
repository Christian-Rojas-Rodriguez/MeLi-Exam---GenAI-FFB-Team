from flask import Flask
from app.api.routes import api_bp  # Importa el blueprint de rutas de la API


def create_app():
    # Inicializa la aplicación Flask
    app = Flask(__name__)

    # Configuraciones de la app (se pueden añadir más según sea necesario)
    app.config['SECRET_KEY'] = 'your_secret_key'  # Configuración de clave secreta (opcional)

    # Registro de blueprints
    app.register_blueprint(api_bp)

    # Configuración de base de datos u otros servicios (opcional)
    # Aquí puedes inicializar extensiones como SQLAlchemy si fuera necesario
    # Ejemplo: db.init_app(app) si tienes una base de datos

    return app
