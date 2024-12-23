from datetime import datetime
from flask_babel import _
from marshmallow import fields, validates, ValidationError
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.database import db
from src.infrastructure.models import Lead

class LeadSchema(SQLAlchemyAutoSchema):
    
    class Meta:
        model = Lead
        load_instance = True
        include_fk = True
        fields = []

    full_name = fields.String(required=True, error_messages={"required": _("Full name is required")})
    phone_number = fields.String(required=True, error_messages={"required": _("Invalid phone number")})
    is_talked = fields.Boolean()
    description = fields.String()
    branch_id = fields.Integer(required=True, error_messages={"required": _("Branch is required")})
    course_id = fields.Integer()

    @validates("phone_number")
    def validate_phone_number(self, value):
        if value and not value.isdigit():
            raise ValidationError(_("The phone number must consist of numbers only"))
        if len(value) != 12:
            raise ValidationError(_("The phone number must be exactly 12 digits"))
    
    def __init__(self, *args, **kwargs):
        if kwargs.get('partial', False):
            self.Meta.fields = [field for field in self.Meta.fields if field not in ['full_name', 'phone_number', 'branch_id']]
        super().__init__(*args, **kwargs)
