from datetime import datetime
from flask_babel import _
from src.infrastructure.models import User, Role, RoleUser
from src.services.branch import BranchService
from src.common.utils import error_response
from src.database import db


class TeacherService:

    @staticmethod
    def get_teacher_by_id(id):
        user: User = User.query.get(id)
        if not user:
            return None
        return user.to_dict()
    
    @staticmethod
    def get_all_teachers(page, per_page):
        teacher_role = Role.query.filter_by(name='TEACHER').first()
        pagination = RoleUser.query.filter_by(role_id=teacher_role.id).order_by(RoleUser.created_at.desc()).paginate(page=page, per_page=per_page)
        pagination_items = pagination.items
        teachers = []

        for item in pagination_items:
            teacher = User.query.filter_by(id=item.user_id).first()
            teachers.append(teacher)
        
        teachers_list = [teacher.to_dict() for teacher in teachers]
        return {
            "items": teachers_list,
            "total": pagination.total,
            "pages": pagination.pages,
            "current_page": pagination.page,
            "per_page": pagination.per_page
        }
    
    @staticmethod
    def get_last_eight_teachers():
        teacher_role = Role.query.filter_by(name='TEACHER').first()
        last_eight_role_user = RoleUser.query.filter_by(role_id=teacher_role.id).order_by(RoleUser.created_at.desc()).limit(8).all()
        teachers = []
        for role_user in last_eight_role_user:
            teacher = User.query.filter_by(id=role_user.user_id).first()
            teachers.append(teacher)
        
        teachers_list = [teacher.to_dict() for teacher in teachers]
        return teachers_list
    
    @staticmethod
    def get_teacher_by_branch_id(branch_id):
        teacher_role = Role.query.filter_by(name='TEACHER').first()
        role_users = RoleUser.query.filter_by(role_id=teacher_role.id).all()
        teachers = []
        for role_user in role_users:
            teacher = User.query.filter_by(id=role_user.user_id, branch_id=branch_id).first()
            if teacher:
                teachers.append(teacher)
        
        teachers_list = [teacher.to_dict() for teacher in teachers]
        return teachers_list
    
    @staticmethod
    def create_teacher(data: dict):
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
    def update_teacher(id, data: dict):
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
    def delete_teacher(id):
        user: User = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
