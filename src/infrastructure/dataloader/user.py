from src.infrastructure.models.user import User
from src.infrastructure.models.role import Role


def load_user(db):
    user = User.query.filter_by(phone_number='998555015353').first()
    if not user:
        new_user = User(first_name='Super', last_name='Admin', phone_number='998555015353', password='1234', is_active=True, is_staff=True)
        super_admin_role = Role.query.filter_by(name='SUPER_ADMIN').first()
        new_user.add_role(super_admin_role)
        db.session.add(new_user)
        db.session.commit()
