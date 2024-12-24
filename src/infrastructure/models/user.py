from datetime import timedelta
import json

from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import generate_password_hash, check_password_hash

from src.database import db
from src.infrastructure.models.role import Role
from src.infrastructure.models.permission import Permission
from src.common.configs.app import Config
from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    patronymic = db.Column(db.String(32))
    phone_number = db.Column(db.String(20))
    password = db.Column(db.String)
    avatar = db.Column(db.String)
    is_staff = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.id'))

    # Relationship with Role (many-to-many via Role_User)
    roles = db.relationship('Role', secondary='role_user', back_populates='users')

    # Relationship with Permission (many-to-many via Permission_User)
    permissions = db.relationship('Permission', secondary='permission_user', back_populates='users')

    def __init__(self, first_name=None, last_name=None, patronymic=None, phone_number=None, avatar=None, branch_id=None, password=None, is_staff=False, is_active=True):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.phone_number = phone_number
        self.avatar = avatar
        self.branch_id = branch_id
        self.password = generate_password_hash(password)
        self.is_staff = is_staff
        self.is_active = is_active

    def __repr__(self):
        return '<User %r>' % self.id
    
    def add_role(self, role):
        if role not in self.roles:
            self.roles.append(role)

    def remove_role(self, role):
        if role in self.roles:
            self.roles.remove(role)

    def add_permission(self, permission):
        if permission not in self.permissions:
            self.permissions.append(permission)

    def remove_permission(self, permission):
        if permission in self.permissions:
            self.permissions.remove(permission)

    def has_role(self, role_name):
        return any([role.name == role_name for role in self.roles])
    
    def has_permission(self, permission_name):
        user_permissions = {permission.name for permission in self.permissions}
        role_permissions = {permission.name for role in self.roles for permission in role.permissions}
        return permission_name in user_permissions or permission_name in role_permissions
    
    def has_roles(self, role_names):
        return any(role.name in role_names for role in self.roles)
    
    def has_any_permissions(self, permission_names):
        user_permissions = {permission.name for permission in self.permissions}
        role_permissions = {permission.name for role in self.roles for permission in role.permissions}
        return any(permission in user_permissions or permission in role_permissions for permission in permission_names)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def generate_access_token(self):
        user_data = {
            'user_id': self.id,
            'phone_number': self.phone_number,
        }
        return create_access_token(identity=json.dumps(user_data), expires_delta=timedelta(minutes=Config.JWT_ACCESS_TOKEN_EXPIRES))
    
    def generate_refresh_token(self):
        user_data = {
            'user_id': self.id,
            'phone_number': self.phone_number,
        }
        return create_refresh_token(identity=json.dumps(user_data), expires_delta=timedelta(minutes=Config.JWT_REFRESH_TOKEN_EXPIRES))

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'patronymic': self.patronymic,
            'phone_number': self.phone_number,
            'avatar': self.avatar,
            'roles': [role.name for role in self.roles],
            'branch_id': self.branch_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
