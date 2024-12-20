from flask import Blueprint, request
from src.infrastructure.controllers.branch import BranchController
from src.common.utils import get_locale_from_headers


branch_routes = Blueprint('branch', __name__)


@branch_routes.route('/get-all', methods=['GET'])
def get_all_branches():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    locale = get_locale_from_headers()
    return BranchController.get_all_branches(page, per_page, locale)


@branch_routes.route('/get-by-id/<int:id>', methods=['GET'])
def get_branch_by_id(id):
    return BranchController.get_branch_by_id(id)
