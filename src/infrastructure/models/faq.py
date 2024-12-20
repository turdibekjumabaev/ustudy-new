from datetime import datetime

from src.database import db


class Faq(db.Model):
    __tablename__ = 'faqs'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.JSON, nullable=False, default={})
    answer = db.Column(db.JSON, nullable=False, default={})
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    def __init__(self, question=None, answer=None):
        self.question = question
        self.answer = answer

    def __repr__(self):
        return '<Faq %r>' % self.id
    
    def to_dict_with_locale(self, locale):
        return {
            'id': self.id,
            'question': self.question.get(locale, ''),
            'answer': self.answer.get(locale, ''),
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def to_dict(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
