from flask import Blueprint
from src.infrastructure.controllers.auth import AuthController
from src.middlewares import admin_required

auth_routes = Blueprint('admin-auth', __name__)


@auth_routes.route('/login', methods=['POST'])
def login():
    return AuthController.login()

@auth_routes.route('/refresh', methods=['POST'])
def refresh():
    return AuthController.refresh()

@auth_routes.route('/register', methods=['POST'])
@admin_required
def register():
    return AuthController.register()

# get me
@auth_routes.route('/get-me', methods=['GET'])
@admin_required
def get_me():
    return AuthController.get_me()