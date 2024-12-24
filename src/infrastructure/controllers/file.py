import logging
from flask import request, send_file
from flask_babel import _
from src.services.file import FileService
from src.common.utils import success_response, error_response, validation_error_response
from src.common.configs.app import Config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class FileController:

    @staticmethod
    def upload_file():
        try:
            file = request.files['file']
            file = FileService.upload_file(file)
            return success_response(data=file)
        except ValueError as e:
            return validation_error_response(message=_('Validation error'), errors=[str(e)])
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
        
    @staticmethod
    def upload_files():
        try:
            files = request.files.getlist('files')
            files = FileService.upload_files(files)
            return success_response(data=files)
        except ValueError as e:
            return validation_error_response(message=_('Validation error'), errors=[str(e)])
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
    
    @staticmethod
    def download_file(filename):
        try:
            return send_file(FileService.download_file(filename), as_attachment=True)
        except FileNotFoundError as e:
            return error_response(404, _('File not found'))
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
