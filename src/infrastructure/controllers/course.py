import logging
from flask import request
from flask_babel import _
from marshmallow import ValidationError
from src.services.course import CourseService
from src.database import db
from src.common.marshmallow import CourseSchema
from src.common.utils import success_response, error_response, validation_error_response, get_request_data


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class CourseController:

    @staticmethod
    def get_all_courses(page, per_page):
        try:
            courses = CourseService.get_all_courses(page=page, per_page=per_page)
            return success_response(data=courses)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
        
    @staticmethod
    def get_course_by_id(id):
        try:
            course = CourseService.get_course_by_id(id)
            if course is None:
                return error_response(404, _("Course not found"))
            return success_response(data=course)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
        
    @staticmethod
    def get_course_by_branch_id(branch_id):
        try:
            courses = CourseService.get_all_courses_by_branch_id(branch_id)
            return success_response(data=courses)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
        
    @staticmethod
    def create_course():
        try:
            course_schema = CourseSchema(session=db.session)
            course_data = course_schema.load(request.get_json())
            course_dict = course_schema.dump(course_data)
            created_course_data, error = CourseService.create_course(course_dict)
            if error:
                return error_response(400, error)
            return success_response(data=created_course_data)
        except ValidationError as e:
            return validation_error_response(e)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
        
    @staticmethod
    def update_course(id):
        try:
            course_schema = CourseSchema(session=db.session)
            course_data = course_schema.load(request.get_json())
            course_dict = course_schema.dump(course_data)
            updated_course_data, error = CourseService.update_course(id, course_dict)
            if error:
                return error_response(400, error)
            return success_response(data=updated_course_data)
        except ValidationError as e:
            return validation_error_response(e)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
        
    @staticmethod
    def delete_course(id):
        try:
            CourseService.delete_course(id)
            return success_response()
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
