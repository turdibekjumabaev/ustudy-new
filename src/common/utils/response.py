from flask import jsonify


def success_response(code = 200, message = "The request was completed successfully", data = None) -> tuple:
    return jsonify({'status': code, 'message': message, 'data': data}), code


def error_response(code: int, message: str) -> tuple:
    return jsonify({
        'status': code,
        'message': message,           
    }), code


def validation_error_response(message: str, errors: dict) -> tuple:
    http_status_code = 422
    return jsonify({
        'status': http_status_code,
        'message': message,
        'errors': errors       
    }), http_status_code
