from datetime import datetime
from src.database import db
from src.infrastructure.models import User, Branch


class Review(db.Model):
    __tablename__ = 'rewviews'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    preview_image = db.Column(db.String, nullable=False)
    youtube_link = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    def __init__(self, student_id: int, preview_image: str, youtube_link: str):
        self.student_id = student_id
        self.preview_image = preview_image
        self.youtube_link = youtube_link
    
    def __repr__(self):
        return f"Review[{self.id}]"
