from flask_babel import _
from src.services.user import UserService
from src.common.utils import error_response

import logging

class AuthService:

    @staticmethod
    def login(data: dict):
        phone_number = data.get('phone_number')
        password = data.get('password')
        user = UserService.get_user_by_phone_number(phone_number)
        logging.info(f"User: {user}")
        if not user:
            return None, error_response(404, _("User not found"))
        if not user.check_password(password):
            return None, error_response(400, _("Invalid password or phone number"))
        access_token = user.generate_access_token()
        refresh_token = user.generate_refresh_token()
        return {'access_token': access_token, 'refresh_token': refresh_token}, None

    @staticmethod
    def refresh(access_token: dict):
        user_id = access_token.get('user_id')
        user = UserService.get_user_by_id(user_id)
        if not user:
            return None, error_response(404, _("User not found"))
        access_token = user.generate_access_token()
        return {'access_token': access_token}, None
