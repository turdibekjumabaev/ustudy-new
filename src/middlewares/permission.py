import json
from functools import wraps
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from flask_babel import _
from src.infrastructure.models import User
from src.common.utils import error_response


def has_permission(required_permission):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                verify_jwt_in_request()
                identity = json.loads(get_jwt_identity())
                user_id = identity.get('user_id')
                user: User = User.query.get(user_id)
                if not user:
                    return error_response(404, _('User not found'))
                
                if not user.has_permission(required_permission):
                    return error_response(403, _('Permission denied'))
            except Exception as e:
                return error_response(401, _("Invalid or missing token"))
            return fn(*args, **kwargs)
        return wrapper
    return decorator

def has_any_permissions(required_permissions):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                verify_jwt_in_request()
                identity = json.loads(get_jwt_identity())
                user_id = identity.get('user_id')
                user: User = User.query.get(user_id)
                if not user:
                    return error_response(404, _('User not found'))
                
                if not user.has_any_permissions(required_permissions):
                    return error_response(403, _('Permission denied'))
            except Exception as e:
                return error_response(401, _("Invalid or missing token"))
            return fn(*args, **kwargs)
        return wrapper
    return decorator
