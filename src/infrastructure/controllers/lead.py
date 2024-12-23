import logging
from flask import request
from flask_babel import _
from marshmallow import ValidationError
from src.services.lead import LeadService
from src.database import db
from src.common.marshmallow import LeadSchema
from src.common.utils import success_response, error_response, validation_error_response, get_request_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class LeadController:

    @staticmethod
    def get_all_leads(page, per_page):
        try:
            leads = LeadService.get_all_leads(page=page, per_page=per_page)
            return success_response(data=leads)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
        
    @staticmethod
    def get_lead_by_id(id):
        try:
            lead, error = LeadService.get_lead_by_id(id)
            if error:
                return error_response(404, error)
            return success_response(data=lead)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
        
    @staticmethod
    def create_lead():
        try:
            lead_schema = LeadSchema(session=db.session)
            lead_data = lead_schema.load(request.get_json())
            lead_dict = lead_schema.dump(lead_data)
            created_lead_data, error = LeadService.create_lead(lead_dict)
            if error:
                return error_response(400, error)
            return success_response(data=created_lead_data)
        except ValidationError as e:
            return validation_error_response(e)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
        
    @staticmethod
    def update_lead(id):
        try:
            lead_schema = LeadSchema(session=db.session)
            lead_data = lead_schema.load(request.get_json())
            lead_dict = lead_schema.dump(lead_data)
            updated_lead_data, error = LeadService.update_lead(id, lead_dict)
            if error:
                return error_response(404, error)
            return success_response(data=updated_lead_data)
        except ValidationError as e:
            return validation_error_response(e)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))