import logging
from flask import request
from flask_babel import _
from src.database import db
from src.services.branch import BranchService
from src.common.utils import success_response, error_response


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class BranchController:

    @staticmethod
    def get_all_branches(page, per_page, locale):
        try:
            branches = BranchService.get_all_branches(page=page, per_page=per_page, locale=locale)
            return success_response(data=branches)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
        
    @staticmethod
    def get_branch_by_id(id):
        try:
            branch = BranchService.get_branch_by_id(id)
            if branch is None:
                return error_response(404, _("Branch not found"))
            return success_response(data=branch)
        except Exception as e:
            logger.error(e)
            return error_response(500, _('Try again later'))
