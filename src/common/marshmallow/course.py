from datetime import datetime
from flask_babel import _
from marshmallow import ValidationError, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.services.teacher import TeacherService
from src.database import db
from src.infrastructure.models import course

class CourseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = course.Course
        load_instance = True
        include_relationships = True
        include_fk = True
    
    name = fields.Dict(required=True, error_messages={"required": _("Name is required")})
    description = fields.Dict(required=True, error_messages={"required": _("Description is required")})
    branch_id = fields.Integer(required=True, error_messages={"required": _("Branch is required")})

    def __init__(self, *args, **kwargs):
        if kwargs.get('partial', False):
            self.Meta.fields = [field for field in self.Meta.fields if field not in ['name', 'description', 'branch_id']]
        super().__init__(*args, **kwargs)
