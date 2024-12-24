import os
from datetime import datetime
from flask_babel import _
from werkzeug.datastructures import FileStorage
from src.common.configs.app import Config


class FileService:

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS
    
    @staticmethod
    def allowed_mime_type(file: FileStorage):
        return file.content_type in Config.ALLOWED_MIME_TYPES

    @staticmethod
    def generate_unique_filename(filename):
        ext = filename.rsplit('.', 1)[1].lower()
        unique_name = f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}.{ext}"
        return unique_name

    @staticmethod
    def upload_file(file):
        if not file:
            raise ValueError(_("No file provided"))

        if not FileService.allowed_file(file.filename):
            raise ValueError(_("File type is not allowed"))

        if not FileService.allowed_mime_type(file):
            raise ValueError(_("MIME type is not allowed"))

        filename = FileService.generate_unique_filename(file.filename)
        upload_folder = Config.UPLOAD_FOLDER

        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return filename

    @staticmethod
    def upload_files(files):
        file_paths = []
        for file in files:
            file_path = FileService.upload_file(file)
            file_paths.append(file_path)
        return file_paths

    @staticmethod
    def download_file(filename):
        uploads_dir = os.path.join(os.getcwd(), Config.UPLOAD_FOLDER)
        file_path = os.path.join(uploads_dir, filename)
        if os.path.exists(file_path):
            return file_path
        else:
            raise FileNotFoundError(_("File not found"))
