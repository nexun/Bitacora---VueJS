from flaskps.models.classes.model import Role, Permission, Role_Permission, User_role
from flaskps.models.alchemy import db_session
from flaskps.models import permission

def get_roles():
    return db_session.query(Role).all()


def get_all():
    result={}
    all_roles=[role.id for role in get_roles()]
    for role in all_roles:
        result[role]=permission.get_role_permissions(role)
    return result

def get_ids():
    rows = db_session.query(Role).all()
    return rows
    
def create(name):
    new = Role(name=name)
    db_session.add(new)
    db_session.commit()
    return new.id

def check_exist(name):
    return db_session.query(Role).filter_by(name=name).count()

def check_exist_id(id_role):
    return db_session.query(Role).filter_by(id=id_role).count()


def check_exist_user(name):
    return db_session.query(User_role).\
        join(Role, Role.id == User_role.id_role).\
        filter_by(name=name).count()


def update(selected, newName):
    role = get_by_name(selected)
    role.name = newName
    db_session.commit()


def delete(name):
    db_session.delete(get_by_name(name))
    db_session.commit()


def get_by_name(name):
    return db_session.query(Role).filter_by(name=name).first()

def nobody_need_it(name):
    subquery = db_session.query(User_role.id_user).\
        join(Role, Role.id == User_role.id_role).filter(Role.name != name)
    return db_session.query(User_role).filter(User_role.id_user.notin_(subquery)).count() == 0

def add_permission(id_role,id_permission):
    new = Role_Permission(id_role=id_role,id_permission=id_permission)
    db_session.add(new)
    db_session.commit()

def remove_permission(id_role,id_permission):
    Role_Permission.query.filter_by(id_role= id_role,id_permission=id_permission).delete()
    db_session.commit()
