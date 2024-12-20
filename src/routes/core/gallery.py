from flask import Blueprint, request
from src.infrastructure.controllers.gallery import GalleryController

gallery_routes = Blueprint('core-gallery', __name__)


@gallery_routes.route('/get-all', methods=['GET'])
def get_all():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return GalleryController.get_all_galleries(page, per_page)


@gallery_routes.route('/get-by-id/<int:id>', methods=['GET'])
def get_by_id(id):
    return GalleryController.get_gallery_by_id(id)
