from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flaskps.config import Config
from flaskps.util import filters
from flaskps.models.model import Model
from flaskps.models import alchemy
from flask_cors import CORS
from flask_mail import Mail
from flask_hashing import Hashing
from datetime import timedelta
import random


# Initial configuration
app = Flask(__name__)
app.config.from_object(Config)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
hashing = Hashing(app)
cors = CORS(app)


# SQLAchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)


# Mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'fran86bellino@gmail.com'
app.config['MAIL_DEFAULT_SENDER'] = 'fran86bellino@gmail.com'
app.config['MAIL_PASSWORD'] = 'grupo152019'
mail = Mail(app)


# Session
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=60) 
Session(app)

# Public Folder
app.config['IMAGE_USER'] = 'flaskps/static/uploads'
app.config['ALLOW_IMAGE_EXTENSIONS'] = ["PNG","JPG","JPEG"]
app.config['MAX_IMAGE_FILESIZE'] = 2 * 1024 * 1024


# Routes
from flaskps.util import routes


# Feedback
from flaskps.controllers import feedback


# Db connection release
@app.teardown_request
def clean_db(exception):
    Model.close_db()

# Alchemy connection release
@app.teardown_appcontext
def clean_alchemy_db(exception=None):
    alchemy.shutdown_session()  

# Maintenance mode filter
@app.before_request
def check_maintenace_mode():
    filters.check_maintenace_mode() 

# # Active session filter
@app.before_request
def check_active_session():
    filters.has_session()

# # Blocked user filter
@app.before_request
def check_bloqued():
    filters.is_bloqued()

 #  Permission check filter
@app.before_request
def check_valid_permission():
    filters.has_permission()