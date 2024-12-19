from flask import request
from flask_babel import Babel

def get_locale():
    locale = request.headers.get('locale', 'uz')
    return 'uz'

babel = Babel()
