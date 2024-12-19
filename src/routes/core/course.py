from flask import Blueprint, request
from src.infrastructure.controllers.course import CourseController

course_routes = Blueprint('core-course', __name__)


@course_routes.route('/get-all', methods=['GET'])
def get_all():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return CourseController.get_all_courses(page, per_page)

@course_routes.route('/get-by-id/<int:id>', methods=['GET'])
def get_by_id(id):
    return CourseController.get_course_by_id(id)

@course_routes.route('/get-by-branch-id/<int:branch_id>', methods=['GET'])
def get_by_branch_id(branch_id):
    return CourseController.get_course_by_branch_id(branch_id)
