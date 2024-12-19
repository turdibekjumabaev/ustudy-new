import logging
from flask import request
from flask_babel import _
from marshmallow import ValidationError
from src.services.teacher import TeacherService
from src.database import db
from src.common.marshmallow import UserSchema
from src.common.utils import success_response, error_response, validation_error_response, get_request_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TeacherController:
    
    @staticmethod
    def get_all_teachers(page, per_page):
        try:
            teachers = TeacherService.get_all_teachers(page=page, per_page=per_page)
            return success_response(data=teachers)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
        
    @staticmethod
    def get_last_eight_teachers():
        try:
            last_eight_teachers = TeacherService.get_last_eight_teachers()
            return success_response(data=last_eight_teachers)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))

    @staticmethod
    def get_teacher_by_id(id):
        try:
            teacher = TeacherService.get_teacher_by_id(id)
            if teacher is None:
                return error_response(404, _("Teacher not found"))
            return success_response(data=teacher)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
    
    @staticmethod
    def create_teacher():
        try:
            teacher_schema = UserSchema(session=db.session)
            teacher_data = teacher_schema.load(request.get_json())
            teacher_dict = teacher_schema.dump(teacher_data)
            created_teacher_data, error = TeacherService.create_teacher(teacher_dict)
            if error:
                return error
            return success_response(data=created_teacher_data)
        except ValidationError as e:
            return validation_error_response(_('Validation error'), errors=e.messages)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
    
    @staticmethod
    def update_teacher(id):
        try:
            data = request.get_json()
            teacher_schema = UserSchema(partial=True, session=db.session)
            teacher_data = teacher_schema.load(data)
            teacher_dict = teacher_schema.dump(teacher_data)
            updated_teacher_data = TeacherService.update_teacher(id, teacher_dict)
            if updated_teacher_data is None:
                return error_response(404, _("Teacher not found"))
            return success_response(data=updated_teacher_data)
            
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
        
    @staticmethod
    def delete_teacher(id):
        try:
            is_deleted = TeacherService.delete_teacher(id)
            if is_deleted:
                return success_response(204, _("Teacher successfully deleted"))
            return error_response(404, _("Teacher not found"))
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
