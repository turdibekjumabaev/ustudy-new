import logging
import json
from flask import request
from flask_babel import _
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from src.database import db
from src.services.auth import AuthService
from src.services.user import UserService
from src.common.marshmallow import LoginSchema, UserSchema
from src.common.utils import success_response, error_response, validation_error_response

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AuthController:

    @staticmethod
    def login():
        try:
            logger.info('Logging in user')
            login_schema = LoginSchema()
            login_data = login_schema.load(request.get_json())
            login_dict = login_schema.dump(login_data)
            data, error = AuthService.login(login_dict)
            if error:
                return error
            return success_response(data=data)
        except ValidationError as e:
            return validation_error_response(message=_("Validation error"), errors=e.messages)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
        
    @staticmethod
    @jwt_required()
    def refresh():
        try:
            current_user_identity = get_jwt_identity()
            data, error = AuthService.refresh(current_user_identity)
            if error:
                return error
            return success_response(data=data)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
        
    @staticmethod
    def register():
        try:
            logger.info('Registering user')
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
    def get_me():
        try:
            current_user_identity = json.loads(get_jwt_identity())
            user_id = current_user_identity.get('user_id')
            user_data = UserService.get_user_by_id(user_id)
            if not user_data:
                return error_response(404, _('User not found'))
            return success_response(data=user_data)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
