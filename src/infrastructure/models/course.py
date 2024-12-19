from sqlalchemy import event
from datetime import datetime
from src.database import db
from src.common.utils import fill_missing_translations


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.JSON, nullable=False, default={})
    short_description = db.Column(db.JSON, nullable=False, default={})
    description = db.Column(db.JSON, nullable=False, default={})
    icon = db.Column(db.String(255), nullable=False)
    duration_month = db.Column(db.Integer, nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    branch = db.relationship('Branch', backref='courses', lazy='select')

    def __init__(self, name: dict, short_description: dict, description: dict, icon: str, duration_month: int, branch_id: int):
        self.name = name
        self.short_description = short_description
        self.description = description
        self.icon = icon
        self.duration_month = duration_month
        self.branch_id = branch_id
