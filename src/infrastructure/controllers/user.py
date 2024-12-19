import logging
from flask import request
from flask_babel import _
from marshmallow import ValidationError
from src.services.user import UserService
from src.database import db
from src.common.marshmallow import UserSchema
from src.common.utils import success_response, error_response, validation_error_response, get_request_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class UserController:
    
    @staticmethod
    def get_all_users():
        try:
            users = UserService.get_all_users()
            return success_response(data=users)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))

    @staticmethod
    def get_user_by_id(id):
        try:
            user = UserService.get_user_by_id(id)
            if user is None:
                return error_response(404, _("User not found"))
            return success_response(data=user)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
    
    @staticmethod
    def create_user():
        try:
            user_schema = UserSchema(session=db.session)
            user_data = user_schema.load(request.get_json())
            user_dict = user_schema.dump(user_data)
            created_user_data, error = UserService.create_user(user_dict)
            if error:
                return error
            return success_response(data=created_user_data)
        except ValidationError as e:
            return validation_error_response(_('Validation error'), errors=e.messages)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
    
    @staticmethod
    def update_user(id):
        try:
            data = request.get_json()
            user_schema = UserSchema(partial=True, session=db.session)
            user_data = user_schema.load(data)
            user_dict = user_schema.dump(user_data)
            updated_user_data = UserService.update_user(id, user_dict)
            if updated_user_data is None:
                return error_response(404, _("User not found"))
            return success_response(data=updated_user_data)
            
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
        
    @staticmethod
    def delete_user(id):
        try:
            is_deleted = UserService.delete_user(id)
            if is_deleted:
                return success_response(204, _("User successfully deleted"))
            return error_response(404, _("User not found"))
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
