from flask import Flask, request
from flask_babel import Babel
from src.routes import register_routes
from src.infrastructure.models import init_db
from src.common.babel import babel, get_locale


def create_app(env: str = 'development') -> Flask:
    app = Flask(__name__)
    app.config.from_object(f'src.common.configs.app.{env.capitalize()}Config')
    babel.init_app(app, locale_selector=get_locale)
    init_db(app)
    register_routes(app)

    return app
