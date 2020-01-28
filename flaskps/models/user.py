""" EN ESTE ARCHIVO HABIA UNA CLASE USUARIO, POR EL MOMENTO SOLO HAY FUNCIONES QUE VAN A LABURAR 
    CON LA CLASE USER QUE ESTA EN MODEL/CLASES/MODEL.PY .LUEGO HABIAMOS PENSADO TRAER LA CLASE USER
    Y METERLE TODAS ESTAS LAS FUNCIONES ADENTRO PERO POR EL MOMENTO IMPORTANDO LA CLASE Y DEFINIENDO 
    LAS FUNCIONES ANDA PERFECTO"""

from flaskps.models.classes.model import User
from flaskps.models.classes.model import User_role
from flaskps.models.alchemy import db_session
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

#move this call to the role model sheet
from flaskps.models.classes.model import Role

#Getter's
def get_all():
    return db_session.query(User).all()

def get_by_email(email):
    return db_session.query(User).filter_by(email=email).first()

def get_by_id(id):          
    return db_session.query(User).get(id)    

def get_cant():
    return db_session.query(User).count()   

def get_cant_bloqued():
    return db_session.query(User).filter_by(bloqued = 'si').count()  

def get_cant_confirmed():
    return db_session.query(User).filter_by(confirmed = 'si').count()    

def get_username_by_id(id):
    return db_session.query(User).get(id).username

def get_id_by_email(email):
    return db_session.query(User).filter_by(email=email).first().id

def get_email_by_id(id):
    return db_session.query(User).filter_by(id=id).first().email


def get_confirm_value_by_id(id):
    return db_session.query(User).filter_by(id=id).first().confirmed

#### Move this function to the role model sheet #################
def get_role_id(name):
    return db_session.query(Role).filter_by(name=name).first().id     
#################### t by google #########################

def set_user_roles(id_user, roles):    
    for role in roles:        
        new = User_role(id_user=id_user,id_role=get_role_id(role))
        db_session.add(new)
    db_session.commit()

def set_user_password(email, password):
    get_by_email(email).password = password
    db_session.commit()

def update_user_password(id, password):        
    user = get_by_id(id)
    user.password = password   
    db_session.commit()        

def set_confirm_value(email, date):
    user = get_by_email(email)
    user.confirmed = 'si'
    user.updated_at = date  
    db_session.commit()         
        
def update_user_info(id, email, first_name, last_name, photo):        
    user = get_by_id(id)
    user.email = email          
    user.first_name = first_name        
    user.last_name = last_name  
    if(photo != ""):
        user.photo = photo
    db_session.commit()

def create(email, fn, ln, psswd, datetime):
    new = User(first_name=fn, email=email, last_name=ln, password=psswd, created_at=datetime)
    db_session.add(new)
    db_session.commit()

def check_exist_by_email(email):
    return db_session.query(User).filter_by(email=email).count()    

def check_exist_by_id(id):
    return db_session.query(User).filter_by(id=id).count()     

def set_bloqued_value(id, value):        
    user = get_by_id(id)
    user.bloqued = value   
    db_session.commit()

def get_bloqued_value(id):
    return db_session.query(User).filter_by(id=id).first().bloqued

def delete_user(id):
    db_session.delete(get_by_id(id))
    db_session.commit()

def delete_user_role(id):
    roles = db_session.query(User_role).filter_by(id_user = id).all()
    for role in roles:        
        db_session.delete(role)
    db_session.commit()

def admin_count_check():
    return db_session.query(User_role).filter_by(id_role=1).count()

def admin_user_check(id):
    return db_session.query(User_role).filter_by(id_role=1,id_user=id).count() 

def get_roles_by_username(username):
    return db_session.query(Role).\
        join(User_role, User_role.id_role == Role.id).\
        join(User, User.id == User_role.id_user).\
        filter_by(username = username).\
        group_by(Role.name)  

def get_roles_by_email(email):
    return db_session.query(Role).\
        join(User_role, User_role.id_role == Role.id).\
        join(User, User.id == User_role.id_user).\
        filter_by(email = email).\
        group_by(Role.name)

def get_roles_by_id(id):
    return db_session.query(Role).\
        join(User_role, User_role.id_role == Role.id).\
        join(User, User.id == User_role.id_user).\
        filter_by(id = id).\
        group_by(Role.name)       


def get_with_roles_by_id(id):
    return {'user': get_by_id(id),
            'roles': get_roles_by_id(id)}

def get_cant_per_role(id):
    return db_session.query(User_role).filter_by(id_role = id).count()