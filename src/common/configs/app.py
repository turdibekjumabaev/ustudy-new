import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', './uploads')
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH_MB', 5)) * 1024 * 1024 
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    ALLOWED_MIME_TYPES = {'image/png', 'image/jpeg', 'image/jpg'}

    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRATION', 1440)) * 60
    JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRATION', 43200)) * 60

    BABEL_DEFAULT_LOCALE = os.getenv('BABEL_DEFAULT_LOCALE', 'uz')
    BABEL_SUPPORTED_LOCALES = os.getenv('BABEL_SUPPORTED_LOCALES', 'uz,ru,kaa').split(',')
    
    project_folder = os.path.dirname(os.path.abspath(__file__))
    
    translation_folder_name = os.getenv('BABEL_TRANSLATION_DIRECTORIES', 'translations')
    BABEL_TRANSLATION_DIRECTORIES = os.path.join(project_folder, translation_folder_name)


class DevelopmentConfig(Config):
    DEBUG = os.getenv('DEBUG', True) == 'True'
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI', f'sqlite:///{os.path.join(basedir, "dev.db")}')


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI', 'sqlite:///:memory:')
    WTF_CSRF_ENABLED = False
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
