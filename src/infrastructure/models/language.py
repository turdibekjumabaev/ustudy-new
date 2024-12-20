from src.database import db
from .base import BaseModel


# Language Model
class Language(BaseModel):
    __tablename__ = 'languages'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    code = db.Column(db.String(2), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, name, code, is_active=True):
        self.name = name
        self.code = code
        self.is_active = is_active

    @classmethod
    def get_language_codes(cls):
        return [language.code for language in cls.query.all()]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "is_active": self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
