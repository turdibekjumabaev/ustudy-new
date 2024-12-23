from datetime import datetime
from flask_babel import _
from src.infrastructure.models import Lead, Role, RoleUser
from src.common.utils import error_response
from src.database import db


class LeadService:

    @staticmethod
    def get_lead_by_id(id):
        lead: Lead = Lead.query.get(id)
        if not lead:
            return None, error_response(_("Lead not found"), 404)
        return lead.to_dict(), None
    
    @staticmethod
    def get_all_leads(page, per_page):
        pagination = Lead.query.order_by(Lead.created_at.desc()).paginate(page=page, per_page=per_page)
        pagination_items = pagination.items
        leads = [lead.to_dict() for lead in pagination_items]
        return {
            "items": leads,
            "total": pagination.total,
            "pages": pagination.pages,
            "current_page": pagination.page,
            "per_page": pagination.per_page
        }
    
    @staticmethod
    def create_lead(data):
        full_name = data.get('full_name')
        phone_number = data.get('phone_number')
        branch_id = data.get('branch_id')
        is_talked = data.get('is_talked', False)
        description = data.get('description')
        course_id = data.get('course_id')

        lead = Lead(phone_number=phone_number, branch_id=branch_id, full_name=full_name, is_talked=is_talked, description=description, course_id=course_id)
        try:
            db.session.add(lead)
            db.session.commit()
            return lead.to_dict(), None
        except Exception as e:
            return None, error_response(code=500, message=_("Internal server error"))
    
    @staticmethod
    def update_lead(id, data):
        lead: Lead = Lead.query.get(id)
        if not lead:
            return error_response(_("Lead not found"), 404)
        
        lead.full_name = data.get('full_name', lead.full_name)
        lead.phone_number = data.get('phone_number', lead.phone_number)
        lead.branch_id = data.get('branch_id', lead.branch_id)
        lead.is_talked = data.get('is_talked', lead.is_talked)
        lead.description = data.get('description', lead.description)
        lead.course_id = data.get('course_id', lead.course_id)
        try:
            db.session.commit()
            return lead.to_dict(), None
        except Exception as e:
            return None, error_response(code=500, message=_("Internal server error"))
        
    @staticmethod
    def delete_lead(id):
        lead: Lead = Lead.query.get(id)
        if not lead:
            return error_response(_("Lead not found"), 404)
        try:
            db.session.delete(lead)
            db.session.commit()
            return None, None
        except Exception as e:
            return None, error_response(code=500, message=_("Internal server error"))
