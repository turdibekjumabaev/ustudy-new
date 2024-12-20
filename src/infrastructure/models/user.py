from werkzeug.security import generate_password_hash

from src.database import db
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
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.id'))

    # Relationship with Role (many-to-many via Role_User)
    roles = db.relationship('Role', secondary='role_user', back_populates='users')

    # Relationship with Permission (many-to-many via Permission_User)
    permissions = db.relationship('Permission', secondary='permission_user', back_populates='users')

    def __init__(self, first_name=None, last_name=None, patronymic=None, phone_number=None, avatar=None, branch_id=None, password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.phone_number = phone_number
        self.avatar = avatar
        self.branch_id = branch_id
        self.password = generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.id

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'patronymic': self.patronymic,
            'phone_number': self.phone_number,
            'avatar': self.avatar,
            'branch_id': self.branch_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
