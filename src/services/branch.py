from datetime import datetime
from src.database import db
from src.infrastructure.models import Branch
from sqlalchemy.exc import SQLAlchemyError


class BranchService:
    """
    Service class for managing Branch CRUD operations.
    """

    @staticmethod
    def create_branch(data):
        try:
            branch = Branch(
                name=data.get('name'),
                address=data.get('address'),
                landmark=data.get('landmark'),
                phone_number=data.get('phone_number'),
                open_time=data.get('open_time'),
                banner=data.get('banner'),
                latitude=data.get('latitude'),
                longitude=data.get('longitude')
            )
            db.session.add(branch)
            db.session.commit()
            return branch.to_dict()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_branch_by_id(id):
        branch = Branch.query.filter_by(id=id, deleted_at=None).first()
        if branch is None:
            return None
        return branch.to_dict()

    @staticmethod
    def get_all_branches(page, per_page):
        branches = Branch.query.filter_by(deleted_at=None).paginate(page=page, per_page=per_page, error_out=False)
        return {
            'items': [branch.to_dict() for branch in branches.items],
            'total': branches.total,
            'pages': branches.pages,
            'per_page': branches.per_page,
            'current_page': branches.page
        }

    @staticmethod
    def update_branch(id, data):
        branch = Branch.query.get(id)
        if branch:
            for key, value in data.items():
                if hasattr(branch, key):
                    setattr(branch, key, value)
            
            db.session.commit()
            return branch.to_dict()
        return None

    @staticmethod
    def delete_branch(id):
            branch = Branch.query.get(id)
            if branch:
                branch.deleted_at = datetime.now()
                db.session.commit()
                return True
            return False
