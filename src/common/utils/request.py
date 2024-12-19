from flask import request
from flask_babel import _
from src.common.utils.response import error_response, validation_error_response


def get_request_data(required_fields):
    data = request.get_json()
    if not data:
        return None, error_response(400, _('Request body JSON cannot be null'))
    return data, None
