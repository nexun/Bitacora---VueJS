from flaskps.models.classes.model import User
from flaskps.models.classes.model import Role
from flaskps.models.classes.model import Role_Permission
from flaskps.models.classes.model import Permission
from flaskps.models.classes.model import User_role
from flaskps.models.alchemy import db_session
from flask import session

def authenticate(email, password):
    if db_session.query(User).filter_by(email=email, password=password).count() == 1:
        return True
    else:
        return False    

def get_permissions_by_email(email):
    return db_session.query(Permission).\
        join(Role_Permission, Role_Permission.id_permission == Permission.id).\
        join(Role, Role.id == Role_Permission.id_role).\
        join(User_role, User_role.id_role == Role.id).\
        join(User, User.id == User_role.id_user).\
        filter_by(email = email).\
        group_by(Permission.name)

def get_permissions_by_username(username):
    return db_session.query(Permission).\
        join(Role_Permission, Role_Permission.id_permission == Permission.id).\
        join(Role, Role.id == Role_Permission.id_role).\
        join(User_role, User_role.id_role == Role.id).\
        join(User, User.id == User_role.id_user).\
        filter_by(username = username).\
        group_by(Permission.name)    
  