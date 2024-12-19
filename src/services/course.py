from datetime import datetime
from flask_babel import _
from src.infrastructure.models import Course
from src.services.branch import BranchService
from src.common.utils import error_response
from src.database import db


class CourseService:

    @staticmethod
    def get_course_by_id(id):
        course: Course = Course.query.get(id)
        if not course:
            return None
        return course.to_dict()
    
    @staticmethod
    def get_all_courses(page, per_page):
        pagination = Course.query.order_by(Course.created_at.desc()).paginate(page=page, per_page=per_page)
        pagination_items = pagination.items
        courses = []

        for item in pagination_items:
            course = Course.query.filter_by(id=item.id).first()
            courses.append(course)
        
        courses_list = [course.to_dict() for course in courses]
        return {
            "items": courses_list,
            "total": pagination.total,
            "pages": pagination.pages,
            "current_page": pagination.page,
            "per_page": pagination.per_page
        }
    
    @staticmethod
    def get_all_courses_by_branch_id(branch_id):
        courses = Course.query.filter_by(branch_id=branch_id).all()
        courses_list = [course.to_dict() for course in courses]
        return courses_list
    
    @staticmethod
    def create_course(data):
        branch = BranchService.get_branch_by_id(data.get('branch_id'))
        if not branch:
            return error_response(_("Branch not found"), 404)
        
        course = Course(
            name=data.get('name'),
            description=data.get('description'),
            branch_id=data.get('branch_id'),
            created_at=datetime.now(),
        )
        db.session.add(course)
        db.session.commit()
        return course.to_dict()
    
    @staticmethod
    def update_course(id, data):
        course = Course.query.get(id)
        if not course:
            return error_response(_("Course not found"), 404)
        
        branch = BranchService.get_branch_by_id(data.get('branch_id'))
        if not branch:
            return error_response(_("Branch not found"), 404)
        
        course.name = data.get('name')
        course.description = data.get('description')
        course.branch_id = data.get('branch_id')
        db.session.commit()
        return course.to_dict()
    
    @staticmethod
    def delete_course(id):
        course = Course.query.get(id)
        if not course:
            return error_response(_("Course not found"), 404)
        
        db.session.delete(course)
        db.session.commit()
        return course.to_dict()
