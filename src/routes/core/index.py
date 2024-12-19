from flask import Blueprint, jsonify

index_routes = Blueprint('core-index', __name__, url_prefix='/')


@index_routes.route('/')
def index():
    return jsonify({'message':'Welcome'})
