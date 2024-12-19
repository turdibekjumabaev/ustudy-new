from datetime import datetime
from src.database import db


class RoleUser(db.Model):
    __tablename__ = 'role_user'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())

class PermissionRole(db.Model):
    __tablename__ = 'permission_role'
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True)
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, role_id, permission_id):
        self.role_id = role_id
        self.permission_id = permission_id

class PermissionUser(db.Model):
    __tablename__ = 'permission_user'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
