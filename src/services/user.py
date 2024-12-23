from datetime import datetime
from flask_babel import _
from src.infrastructure.models import User, Role, RoleUser
from src.services.branch import BranchService
from src.common.utils import error_response
from src.database import db


class UserService:
    @staticmethod
    def get_all_users():
        users = User.query.all()
        users_data = [user.to_dict() for user in users]
        return users_data

    @staticmethod
    def get_user_by_id(id) -> User:
        user: User = User.query.get(id)
        if not user:
            return None
        return user.to_dict()
    
    @staticmethod
    def get_user_by_phone_number(phone_number) -> User:
        user: User = User.query.filter_by(phone_number=phone_number).first()
        if not user:
            return None
        return user
    
    @staticmethod
    def create_user(data: dict):
        branch_id = data.get('branch_id')
        phone_number=data.get('phone_number')
        branch = BranchService.get_branch_by_id(branch_id)
        if not branch:
            return None, error_response(404, _("Branch not found"))
        phone_number_exists = User.query.filter_by(phone_number=phone_number).first()
        if phone_number_exists:
            return None, error_response(400, _("Phone number already taken"))
        new_user = User(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            patronymic=data.get('patronymic'),
            phone_number=data.get('phone_number'),
            password=data.get('password'),
            avatar=data.get('avatar'),
            branch_id=branch_id
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict(), None
    
    @staticmethod
    def update_user(id, data: dict):
        user: User = User.query.get(id)
        if user:
            user.first_name = data.get('first_name', user.first_name)
            user.last_name = data.get('last_name', user.last_name)
            user.patronymic = data.get('patronymic', user.patronymic)
            user.phone_number = data.get('phone_number', user.phone_number)
            user.avatar = data.get('avatar', user.avatar)
            user.branch_id = data.get('branch_id', user.branch_id)
            user.updated_at = datetime.now()
            return user.to_dict()
        return None
    
    @staticmethod
    def delete_user(id):
        user: User = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
