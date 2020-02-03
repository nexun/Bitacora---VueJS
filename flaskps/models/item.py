from flaskps.models.classes.model import Item
from flaskps.models.alchemy import db_session

def get_all():
    return db_session.query(Item).all()

def get_by_id(id):
    return db_session.query(Item).get(id) 

def get_tittle_by_id(id):
    return db_session.query(Item).get(id).tittle

def check_exist_by_tittle(tittle):
    return db_session.query(Item).filter_by(tittle=tittle).count()  

def check_exist_by_id(id):
    return db_session.query(Item).filter_by(iditem=id).count()  

def create(code,tittle, description, id_c, id_s, created):
    new = Item(code=code, tittle=tittle, description=description, id_category=id_c, id_state=id_s, created_at=created)
    db_session.add(new)
    db_session.commit()  

def update_item_info(id, code, tittle, description, id_c, id_s, updated, solution):        
    item = get_by_id(id)
    item.code = code    
    item.tittle = tittle    
    item.description = description    
    item.id_category = id_c
    item.id_state = id_s
    item.solution = solution    
    item.updated_at = updated     
    db_session.commit()

def update_item_info_nosolution(id, code, tittle, description, id_c, id_s, updated):        
    item = get_by_id(id)
    item.code = code    
    item.tittle = tittle    
    item.description = description    
    item.id_category = id_c
    item.id_state = id_s
    item.updated_at = updated     
    db_session.commit()

def delete_item(id):
    db_session.delete(get_by_id(id))
    db_session.commit()    