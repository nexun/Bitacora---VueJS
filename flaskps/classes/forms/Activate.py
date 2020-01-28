from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField  
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField


class activate(FlaskForm):
    password = PasswordField(validators=[DataRequired()])
    
