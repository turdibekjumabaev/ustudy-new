from flask import request

def get_locale_from_headers():
    locale = request.headers.get('locale', 'kk')
    return locale
