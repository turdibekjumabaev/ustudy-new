from flask import Blueprint, request
from src.infrastructure.controllers.faq import FaqController
from src.common.utils import get_locale_from_headers


faq_routes = Blueprint('faq', __name__)


@faq_routes.route('/get-all', methods=['GET'])
def get_all_faqs():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    locale = get_locale_from_headers()
    return FaqController.get_all_faqs(page, per_page, locale)


@faq_routes.route('/get-by-id/<int:id>', methods=['GET'])
def get_faq_by_id(id):
    return FaqController.get_faq_by_id(id)
