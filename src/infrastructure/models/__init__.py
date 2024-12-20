import logging
from flask import Flask
from src.database import db
from src.database.migrations import migrate

from src.infrastructure.dataloader import load_data

from src.infrastructure.models.role import Role
from src.infrastructure.models.permission import Permission
from src.infrastructure.models.faq import Faq
from src.infrastructure.models.language import Language

from src.infrastructure.models.user import User
from src.infrastructure.models.branch import Branch
from src.infrastructure.models.course import Course
from src.infrastructure.models.gallery import Gallery
from src.infrastructure.models.lead import Lead
from src.infrastructure.models.review import Review

from src.infrastructure.models.associations import *

def init_db(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        db.create_all()
        load_data(db)
