from flask import Blueprint, jsonify
from src.infrastructure.controllers.user import UserController

user_routes = Blueprint('core-user', __name__)


@user_routes.route('/get-all', methods=['GET'])
def get_all_users():
    return UserController.get_all_users()

@user_routes.route('/get-by-id/<int:id>', methods=['GET'])
def get_by_id(id):
    return UserController.get_user_by_id(id)

@user_routes.route('/create', methods=['POST'])
def create_user():
    return UserController.create_user()

@user_routes.route('/update-by-id/<int:id>', methods=['PUT'])
def update_user_by_id(id):
    return UserController.update_user(id)

@user_routes.route('/delete-by-id/<int:id>', methods=['DELETE'])
def delete_user_by_id(id):
    return UserController.delete_user(id)

