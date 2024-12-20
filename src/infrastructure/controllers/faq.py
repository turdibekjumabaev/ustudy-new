import logging
from flask import request
from flask_babel import _
from src.database import db
from src.services.faq import FaqService
from src.common.utils import success_response, error_response


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class FaqController:

    @staticmethod
    def get_all_faqs(page, per_page, locale):
        try:
            faqs = FaqService.get_all_faqs(page=page, per_page=per_page, locale=locale)
            return success_response(data=faqs)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
        
    @staticmethod
    def get_faq_by_id(id):
        try:
            faq = FaqService.get_faq_by_id(id)
            if faq is None:
                return error_response(404, _("Faq not found"))
            return success_response(data=faq)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
