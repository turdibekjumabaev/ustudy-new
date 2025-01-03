import json
from src.database import db
from src.common.utils import fill_missing_translations
from .base import BaseModel
from .language import Language


class Branch(BaseModel):
    __tablename__ = 'branches'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.JSON, nullable=False, default= lambda: {})
    address = db.Column(db.JSON, nullable=False, default= lambda: {})
    landmark = db.Column(db.JSON, nullable=False, default= lambda: {})
    phone_number = db.Column(db.String(12), nullable=False)
    open_time = db.Column(db.JSON, nullable=False, default= lambda: {})
    banner = db.Column(db.String, nullable=False)
    latitude = db.Column(db.String)
    longitude = db.Column(db.String)

    def __init__(self, name=None, address=None, landmark=None, phone_number=None, open_time=None, 
                 banner=None, latitude=None, longitude=None):
        """
        Initialize the Branch object with support for multiple languages.
        
        Args:
            name (dict): Translations for the name field (e.g., {'uz': 'Filial 1', 'ru': 'Филиал 1'})
            address (dict): Translations for the address field (e.g., {'uz': 'Toshkent sh.', 'ru': 'г. Ташкент'})
            landmark (dict): Translations for the landmark field (e.g., {'uz': 'Chorsu bozori yaqinida', 'ru': 'рядом с Чорсу'})
            phone_number (str): The phone number of the branch.
            open_time (dict): The open time in multiple languages (if needed) or general format.
            banner (str): URL or path to the banner image.
            latitude (str): Latitude coordinate.
            longitude (str): Longitude coordinate.
        """
        language_codes = Language.get_language_codes()
        
        self.name = fill_missing_translations(name, language_codes)
        self.address = fill_missing_translations(address, language_codes)
        self.landmark = fill_missing_translations(landmark, language_codes)
        
        self.phone_number = phone_number
        self.open_time = open_time
        self.banner = banner
        self.latitude = latitude
        self.longitude = longitude

    def to_dict_with_locale(self, locale):
        return {
            "locale": locale,
            "id": self.id,
            "name": self.name.get(locale, ''),
            "address": self.address.get(locale, ''),
            "landmark": self.landmark.get(locale, ''),
            "phone_number": self.phone_number,
            "open_time": self.open_time,
            "banner": self.banner,
            "latitude": self.latitude,
            "longitude": self.longitude,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "landmark": self.landmark,
            "phone_number": self.phone_number,
            "open_time": self.open_time,
            "banner": self.banner,
            "latitude": self.latitude,
            "longitude": self.longitude,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
