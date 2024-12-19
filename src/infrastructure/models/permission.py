from datetime import datetime

from src.database import db


class Permission(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # Relationship with Role (many-to-many via Permission_Role)
    roles = db.relationship('Role', secondary='permission_role', back_populates='permissions')

    # Relationship with User (many-to-many via Permission_User)
    users = db.relationship('User', secondary='permission_user', back_populates='permissions')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Permission %r>' % self.name
