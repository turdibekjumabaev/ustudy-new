from src.infrastructure.models.permission import Permission


def load_permissions(db):
    default_permissions = [
        'CREATE_ADMIN', 'VIEW_ADMIN', 'UPDATE_ADMIN', 'DELETE_ADMIN'
        'CREATE_BRANCH', 'VIEW_BRANCH', 'UPDATE_BRANCH', 'DELETE_BRANCH',
        'CREATE_COURSE', 'VIEW_COURSE', 'UPDATE_COURSE', 'DELETE_COURSE',
        'CREATE_LEAD', 'VIEW_LEAD', 'UPDATE_LEAD', 'DELETE_LEAD',
        'CREATE_FAQ', 'VIEW_FAQ', 'UPDATE_FAQ', 'DELETE_FAQ',
        'UPLOAD_CONTENT_TO_GALLERY', 'VIEW_GALLERY', 'UPDATE_GALLERY', 'DELETE_CONTENT_FROM_GALLERY',
        'CREATE_REVIEW', 'VIEW_REVIEW', 'UPDATE_REVIEW', 'DELETE_REVIEW',
        'FILE_UPLOAD', 'FILE_DOWNLOAD'
    ]

    for default_permission in default_permissions:
        permission = Permission.query.filter_by(name=default_permission).first()

        if permission is None:
            new_permission = Permission(default_permission)
            db.session.add(new_permission)

    db.session.commit()
