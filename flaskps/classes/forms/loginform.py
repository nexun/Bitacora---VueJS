from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField  
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField


class LoginForm(FlaskForm):
    inputEmail = EmailField(validators=[DataRequired()])
    inputPassword = PasswordField(validators=[DataRequired()])
