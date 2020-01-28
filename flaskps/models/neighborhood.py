from flaskps.models.classes.model import Neighborhood
from flaskps.models.alchemy import db_session

#Getter's
def get_all():
    return db_session.query(Neighborhood).all()

def get_name_by_id(id):
    return db_session.query(Neighborhood).filter_by(id = id).first().name    