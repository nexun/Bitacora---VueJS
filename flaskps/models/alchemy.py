from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData
from sqlalchemy import Table
from flaskps.config import Config


    
#Create 
DB_URL= 'mysql://{}:{}@{}:3306/{}'.format(Config.DB_USER, Config.DB_PASS,Config.DB_HOST,Config.DB_NAME)

engine = create_engine(DB_URL, convert_unicode=True)
    
#Create declarative base
Base = declarative_base()

#Create Session and save on the db
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False,bind=engine))
Base.query = db_session.query_property()   

#Here we import all models
from flaskps.models.classes import model

#Create database with the models
Base.metadata.create_all(bind=engine)                
            
def shutdown_session(exception=None):
    db_session.remove()


