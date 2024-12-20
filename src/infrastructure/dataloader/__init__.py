from .branch import init_nukus_branch
from .role import load_roles
from .permission import load_permissions
from .associations import set_permissions_for_the_manager_role, set_permissions_for_the_super_admin_role
from .language import load_language

def load_data(db):
    init_nukus_branch(db)
    load_roles(db)
    load_permissions(db)
    set_permissions_for_the_super_admin_role(db)
    set_permissions_for_the_manager_role(db)
    load_language(db)
