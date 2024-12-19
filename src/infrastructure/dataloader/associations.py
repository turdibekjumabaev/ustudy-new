import logging

from src.infrastructure.models.role import Role
from src.infrastructure.models.permission import Permission
from src.infrastructure.models.associations import PermissionRole

logger = logging.getLogger(__name__)


def set_permissions_for_the_super_admin_role(db):
    super_admin = Role.query.filter_by(name='SUPER_ADMIN').first()
    if not super_admin:
        super_admin = Role(name='SUPER_ADMIN') 
        db.session.add(super_admin)
        db.session.commit()

    permissions = Permission.query.all()

    existing_permission_roles = set(
        (pr.role_id, pr.permission_id) for pr in PermissionRole.query.filter_by(role_id=super_admin.id).all()
    )

    permission_roles_to_add = []
    for permission in permissions:
        if (super_admin.id, permission.id) not in existing_permission_roles:
            permission_roles_to_add.append(PermissionRole(role_id=super_admin.id, permission_id=permission.id))

    if permission_roles_to_add:
        db.session.add_all(permission_roles_to_add)
        db.session.commit()



def set_permissions_for_the_manager_role(db):
    default_permissions = [
        'CREATE_LEAD', 'VIEW_LEAD', 'UPDATE_LEAD', 'DELETE_LEAD',
        'UPLOAD_CONTENT_TO_GALLERY', 'VIEW_GALLERY', 'UPDATE_GALLERY', 'DELETE_CONTENT_FROM_GALLERY',
        'VIEW_COURSE',
    ]

    permissions: list[Permission] = []
    for permission_name in default_permissions:
        permission: Permission = Permission.query.filter_by(name=permission_name).first()
        if not permission:
            logger.error(f"Default permission not found: {permission_name}")
            continue
        permissions.append(permission)

    manager_role: Role = Role.query.filter_by(name='MANAGER').first()
    if not manager_role:
        manager_role = Role(name='MANAGER')
        db.session.add(manager_role)
        db.session.commit()
    
    for permission in permissions:
        exists: PermissionRole = PermissionRole.query.filter_by(role_id=manager_role.id, permission_id=permission.id).first()
        if not exists:
            permission_role = PermissionRole(role_id=manager_role.id, permission_id=permission.id)
            db.session.add(permission_role)
        
    db.session.commit()
