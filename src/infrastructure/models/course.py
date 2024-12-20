from src.database import db
from src.common.utils import fill_missing_translations
from .base import BaseModel
from .language import Language


class Course(BaseModel):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.JSON, nullable=False, default= lambda: {})
    short_description = db.Column(db.JSON, nullable=False, default= lambda: {})
    description = db.Column(db.JSON, nullable=False, default= lambda: {})
    icon = db.Column(db.String(255), nullable=False)
    duration_month = db.Column(db.Integer, nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.id'), nullable=False)

    branch = db.relationship('Branch', backref='courses', lazy='select')

    def __init__(self, name, short_description, description, icon: str, duration_month: int, branch_id: int):
        language_codes = Language.get_language_codes()
        self.name = fill_missing_translations(name, language_codes)
        self.short_description = fill_missing_translations(short_description, language_codes)
        self.description = fill_missing_translations(description, language_codes)
        self.icon = icon
        self.duration_month = duration_month
        self.branch_id = branch_id
