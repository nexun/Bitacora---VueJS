from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import DataRequired


class addCenterForm(FlaskForm):
    name = StringField(validators=[DataRequired()])    
    phone = StringField(validators=[DataRequired()])
    address = StringField(validators=[DataRequired()])          
    

class updateCenterForm(FlaskForm):
    name = StringField(validators=[DataRequired()])    
    phone = StringField(validators=[DataRequired()])
    address = StringField(validators=[DataRequired()])
