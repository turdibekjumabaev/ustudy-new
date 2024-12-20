from flask import Flask


def register_routes(app: Flask) -> None:
    from .core import index_routes
    from .core import user_routes
    from .core import teacher_routes
    from .core import course_routes
    from .core import gallery_routes
    from .core import branch_routes

    app.register_blueprint(index_routes)
    app.register_blueprint(user_routes, url_prefix='/core/api/v1/user')
    app.register_blueprint(teacher_routes, url_prefix='/core/api/v1/teacher')
    app.register_blueprint(course_routes, url_prefix='/core/api/v1/course')
    app.register_blueprint(gallery_routes, url_prefix='/core/api/v1/gallery')
    app.register_blueprint(branch_routes, url_prefix='/core/api/v1/branch')
