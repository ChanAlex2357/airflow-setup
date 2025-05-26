# create_admin_user.py

from airflow import settings
from airflow.www.security_manager import AirflowSecurityManager

def create_admin_user():
    session = settings.Session()

    security_manager = AirflowSecurityManager(None)

    existing_user = security_manager.find_user(username="admin")
    if existing_user:
        print("⚠️  L'utilisateur 'admin' existe déjà.")
        return

    user = security_manager.add_user(
        username='admin',
        first_name='Admin',
        last_name='User',
        email='admin@example.com',
        role=security_manager.find_role('Admin'),
        password='admin'  # 🔐 Remplacez par un mot de passe fort en production
    )

    session.commit()
    print("✅ Utilisateur admin créé avec succès !")

if __name__ == "__main__":
    create_admin_user()
