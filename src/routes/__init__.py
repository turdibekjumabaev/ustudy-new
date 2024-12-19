from flask import Flask


def register_routes(app: Flask) -> None:
    from .core import index_routes
    from .core import user_routes

    app.register_blueprint(index_routes)
    app.register_blueprint(user_routes, url_prefix='/core/api/v1/user')
