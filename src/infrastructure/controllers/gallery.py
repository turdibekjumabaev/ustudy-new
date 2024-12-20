import logging
from flask import request
from flask_babel import _
from marshmallow import ValidationError
from src.services.gallery import GalleryService
from src.database import db
from src.common.utils import success_response, error_response, validation_error_response, get_request_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class GalleryController:

    @staticmethod
    def get_all_galleries(page, per_page):
        try:
            galleries = GalleryService.get_all_galleries(page=page, per_page=per_page)
            return success_response(data=galleries)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
        
    @staticmethod
    def get_gallery_by_id(id):
        try:
            gallery = GalleryService.get_gallery_by_id(id)
            if gallery is None:
                return error_response(404, _("Gallery not found"))
            return success_response(data=gallery)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))

        
    @staticmethod
    def delete_gallery(id):
        try:
            GalleryService.delete_gallery(id)
            return success_response()
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
