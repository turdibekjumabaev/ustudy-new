from src.database import db
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    deleted_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    def delete(self):
        self.deleted_at = datetime.now()

    def to_dict(self):
        raise NotImplementedError
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_all_active(cls):
        return cls.query.filter(cls.deleted_at.is_(None)).all()
    
    @classmethod
    def get_all_deleted(cls):
        return cls.query.filter(cls.deleted_at.isnot(None)).all()
    
    @classmethod
    def get_all_paginated(cls, page=1, per_page=10):
        return cls.query.paginate(page, per_page, False)
    
    @classmethod
    def get_all_active_paginated(cls, page=1, per_page=10):
        return cls.query.filter(cls.deleted_at.is_(None)).paginate(page, per_page, False)
    
    @classmethod
    def get_all_deleted_paginated(cls, page=1, per_page=10):
        return cls.query.filter(cls.deleted_at.isnot(None)).paginate(page, per_page, False)
