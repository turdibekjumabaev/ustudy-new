from datetime import datetime
from flask_babel import _
from src.infrastructure.models import Gallery
from src.common.utils import error_response
from src.database import db


class GalleryService:

    @staticmethod
    def get_gallery_by_id(id):
        gallery: Gallery = Gallery.query.get(id)
        if not gallery:
            return None
        return gallery.to_dict()
    
    @staticmethod
    def get_all_galleries(page, per_page):
        pagination = Gallery.query.order_by(Gallery.created_at.desc()).paginate(page=page, per_page=per_page)
        pagination_items = pagination.items
        galleries = [gallery.to_dict() for gallery in pagination_items]
        return {
            "items": galleries,
            "total": pagination.total,
            "pages": pagination.pages,
            "current_page": pagination.page,
            "per_page": pagination.per_page
        }
