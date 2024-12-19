from datetime import datetime
from src.database import db


class Lead(db.Model):
    __tablename__ = 'leads'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(64))
    phone_number = db.Column(db.String(20), nullable=False)
    is_talked = db.Column(db.Boolean, default=False, nullable=False)
    description = db.Column(db.String(500))
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    def __init__(self, phone_number: str, branch_id: int, full_name: str = None, is_talked: bool = False, description: str = None, course_id: int = None):
        self.phone_number = phone_number
        self.branch_id = branch_id
        self.full_name = full_name
        self.is_talked = is_talked
        self.description = description
        self.course_id = course_id

    def __repr__(self):
        return f"Lead[{self.phone_number}]"
