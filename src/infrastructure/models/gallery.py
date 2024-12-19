from datetime import datetime
from src.database import db
from src.common.enums import ContentTypeEnum


class Gallery(db.Model):
    __tablename__ = 'gallery'

    id = db.Column(db.Integer, primary_key=True)
    alt_text = db.Column(db.String)
    orginal_filename = db.Column(db.String)
    content_type = db.Column(db.Enum(ContentTypeEnum), nullable=False)
    filename = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    def __init__(self, alt_text, orginal_filename, content_type, filename):
        self.alt_text = alt_text
        self.orginal_filename = orginal_filename
        self.content_type = content_type
        self.filename = filename

    def __repr__(self):
        return '<Gallery %r>' % self.id
