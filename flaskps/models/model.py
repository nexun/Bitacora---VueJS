import pymysql
from flask import g
from flaskps.config import Config


class Model:
    '''
    Every other model has to inherit from this one.
    Use `cls.get_db()` to get a connection to the database.
    Example: use `with cls.get_db().cursor() as cursor:` to query the database.
    Disregard `close_db()` as the connection is closed automatically.
    '''

    @classmethod
    def get_db(cls):
        if 'db' not in g:
            g.db = pymysql.connect(
                host=Config.DB_HOST,
                user=Config.DB_USER,
                password=Config.DB_PASS,
                db=Config.DB_NAME,
                cursorclass=pymysql.cursors.DictCursor
            )
        return g.db

    @classmethod
    def close_db(cls):
        db = g.pop('db', None)
        if db is not None:
            db.close()
