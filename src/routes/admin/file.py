from flask import Blueprint, send_from_directory
from src.infrastructure.controllers.file import FileController


file_routes = Blueprint('admin-file', __name__)


@file_routes.route('/upload-file', methods=['POST'])
def upload_file():
    return FileController.upload_file()

@file_routes.route('/upload-files', methods=['POST'])
def upload_files():
    return FileController.upload_files()

@file_routes.route('/download-file/<filename>', methods=['GET'])
def download_file(filename):
    return FileController.download_file(filename)
