from src.database import db
from src.infrastructure.models import Faq
from sqlalchemy.exc import SQLAlchemyError


class FaqService:
    """
    Service class for managing Faq CRUD operations.
    """

    @staticmethod
    def create_faq(data):
        try:
            faq = Faq(
                question=data.get('question'),
                answer=data.get('answer'),
                category=data.get('category')
            )
            db.session.add(faq)
            db.session.commit()
            return faq.to_dict()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_faq_by_id(id):
        faq = Faq.query.filter_by(id=id).first()
        if faq is None:
            return None
        return faq.to_dict()

    @staticmethod
    def get_all_faqs(page, per_page, locale):
        faqs = Faq.query.filter_by().paginate(page=page, per_page=per_page, error_out=False)
        return {
            'items': [faq.to_dict_with_locale(locale) for faq in faqs.items],
            'total': faqs.total,
            'pages': faqs.pages,
            'per_page': faqs.per_page,
            'current_page': faqs.page
        }

    @staticmethod
    def update_faq(id, data):
        faq = Faq.query.get(id)
        if faq:
            for key, value in data.items():
                if hasattr(faq, key):
                    setattr(faq, key, value)
            
            db.session.commit()
            return faq.to_dict()
        return None
