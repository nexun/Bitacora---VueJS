from flaskps.models.classes.model import User, Role, User_role
from flaskps.models.alchemy import db_session

def get_all():
    return db_session.query(User).\
        join(User_role, User.id == User_role.id_user).\
        join(Role, User_role.id_role == Role.id).\
        filter_by(name = 'administrator').\
        all()