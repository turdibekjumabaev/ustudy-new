from flask import Blueprint, request
from src.infrastructure.controllers.lead import LeadController

lead_routes = Blueprint('core-lead', __name__)


@lead_routes.route('/register', methods=['POST'])
def register():
    return LeadController.create_lead()
