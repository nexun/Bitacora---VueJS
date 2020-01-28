from flaskps.models.classes.model import AppConfig
from flaskps.models.alchemy import db_session


def get_all():
    return db_session.query(AppConfig).all() 