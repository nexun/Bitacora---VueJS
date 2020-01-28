from flaskps.models.classes.model import Role, Permission, Role_Permission
from flaskps.models.alchemy import db_session

def get_role_permissions(id_rol):
    role_permissions= db_session.query(Permission.id,Permission.public_name).\
        join(Role_Permission, Role_Permission.id_permission == Permission.id).\
        join(Role, Role_Permission.id_role == Role.id).filter(Role.id == id_rol).all()
    result=[{
        'id':permission[0],
        'name':permission[1]
    }for permission in role_permissions]
    return result


def get_permissions():
    return db_session.query(Permission).all()

def get_ids():
    return db_session.query(Permission.id).all()

def check_exist(name):
    return db_session.query(Permission).filter_by(name=name).count()

def check_exist_public(public):
    return db_session.query(Permission).filter_by(public_name=public).count()

def create(name,public):
    new = Permission(name=name,public_name=public)
    db_session.add(new)
    db_session.commit()
    return new.id

def get_by_name(name):
    return db_session.query(Permission).filter_by(name=name).first()

def update(selected, newName,newPublic):
    permission = get_by_name(selected)
    permission.name = newName
    permission.public_name= newPublic
    db_session.commit()

def delete(name):
    db_session.delete(get_by_name(name))
    db_session.commit()