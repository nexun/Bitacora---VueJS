from flaskps.models.classes.model import AppConfig
from flaskps.models.alchemy import db_session



def get_app_title():
    return db_session.query(AppConfig).filter_by(name = 'app_title').first().value

def get_app_description():
    return db_session.query(AppConfig).filter_by(name = 'app_description').first().value

def get_items_per_page():    
    return db_session.query(AppConfig).filter_by(name = "items_per_page").first().value

def get_app_contact_email():    
    return db_session.query(AppConfig).filter_by(name = "app_contact_email").first().value

def get_is_maintenance_mode():    
    return db_session.query(AppConfig).filter_by(name = "is_maintenance_mode").first().value

def update_pagination(value):    
    db_session.query(AppConfig).filter_by(name = "items_per_page").first().value = value
    db_session.commit()

def update_public_info(app_title, app_description, app_contact_email):
    db_session.query(AppConfig).filter_by(name = "app_title").first().value = app_title
    db_session.query(AppConfig).filter_by(name = "app_description").first().value = app_description
    db_session.query(AppConfig).filter_by(name = "app_contact_email").first().value = app_contact_email
    db_session.commit()

def update_maintenance_mode(set_maintenance_mode):
    db_session.query(AppConfig).filter_by(name = "is_maintenance_mode").first().value = set_maintenance_mode
    db_session.commit()


 