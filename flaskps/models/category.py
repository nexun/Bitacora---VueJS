from flaskps.models.classes.model import Category
from flaskps.models.alchemy import db_session

def get_all():
    return db_session.query(Category).all()

def get_by_id(id):
    return db_session.query(Category).get(id) 

def get_name_by_id(id):
    return db_session.query(Category).get(id).name

def check_exist_by_name(name):
    return db_session.query(Category).filter_by(name=name).count()  

def check_exist_by_id(id):
    return db_session.query(Category).filter_by(idcategory=id).count()  

def create(name):
    new = Category(name=name)
    db_session.add(new)
    db_session.commit()  

def update_category_info(id, name):        
    category = get_by_id(id)
    category.name = name     
    db_session.commit()

def delete_category(id):
    db_session.delete(get_by_id(id))
    db_session.commit()    