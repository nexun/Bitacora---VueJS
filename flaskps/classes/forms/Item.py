from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class addItemForm(FlaskForm):
    tittle = StringField(validators=[DataRequired()])  
    id_category = StringField(validators=[DataRequired()])  
    description = StringField(validators=[DataRequired()])           

    
