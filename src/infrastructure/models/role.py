from datetime import datetime

from src.database import db


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    # Relationship with User (many-to-many with User via Role_User)
    users = db.relationship('User', secondary='role_user', back_populates='roles')
    permissions = db.relationship('Permission', secondary='permission_role', back_populates='roles')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Role %r>' % self.name
