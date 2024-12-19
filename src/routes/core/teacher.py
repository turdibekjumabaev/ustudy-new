from flask import Blueprint, request
from src.infrastructure.controllers.teacher import TeacherController

teacher_routes = Blueprint('core-teacher', __name__)


@teacher_routes.route('/get-last-eight', methods=['GET'])
def get_last_eight():
    return TeacherController.get_last_eight_teachers()


@teacher_routes.route('/get-all', methods=['GET'])
def get_all():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return TeacherController.get_all_teachers(page, per_page)


@teacher_routes.route('/get-by-id/<int:id>', methods=['GET'])
def get_by_id(id):
    return TeacherController.get_teacher_by_id(id)


@teacher_routes.route('/get-by-branch-id/<int:branch_id>', methods=['GET'])
def get_by_branch_id(branch_id):
    return TeacherController.get_teacher_by_branch_id(branch_id)
