import json
from functools import wraps
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from src.infrastructure.models import User, Role, RoleUser
from src.common.utils import error_response


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        identitiy = json.loads(get_jwt_identity())
        user_id = identitiy.get('user_id')
        user: User = User.query.get(user_id)
        if user is None:
            return error_response(code=404, message='User not found')
        
        if not user.has_roles(['SUPER_ADMIN', 'ADMIN']):
            return error_response(code=403, message='You are not authorized to perform this action')
        
        return fn(*args, **kwargs)
    return wrapper
