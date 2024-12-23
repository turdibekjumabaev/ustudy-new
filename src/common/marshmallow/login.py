from flask_babel import _
from marshmallow import ValidationError, fields, validates, Schema


class LoginSchema(Schema):
    phone_number = fields.String(required=True, error_messages={"required": _("Invalid phone number")})
    password = fields.String(required=True, error_messages={"required": _("Password is required")})

    @validates("phone_number")
    def validate_phone_number(self, value):
        if value and not value.isdigit():
            raise ValidationError(_("The phone number must consist of numbers only"))
        if len(value) != 12:
            raise ValidationError(_("The phone number must be exactly 12 digits"))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
