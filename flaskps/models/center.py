from flaskps.models.classes.model import Center
from flaskps.models.alchemy import db_session

def get_all():
    return db_session.query(Center).all()

def get_by_id(id):
    return db_session.query(Center).get(id) 

def get_name_by_id(id):
    return db_session.query(Center).get(id).name

def check_exist_by_name(name):
    return db_session.query(Center).filter_by(name=name).count()  

def check_exist_by_id(id):
    return db_session.query(Center).filter_by(id=id).count()  

def create(name, pn, address, lat, lng):
    new = Center(name=name, address=address, phone_number=pn, lat=lat, lng=lng)
    db_session.add(new)
    db_session.commit()  

def update_center_info(id, name, address, phone, lat, lng):        
    center = get_by_id(id)
    center.name = name    
    center.address = address    
    center.phone_number = phone  
    center.lat = lat
    center.lng = lng  
    db_session.commit()

def delete_center(id):
    db_session.delete(get_by_id(id))
    db_session.commit()    