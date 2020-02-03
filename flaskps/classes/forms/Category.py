from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class addCategoryForm(FlaskForm):
    name = StringField(validators=[DataRequired()])             
        
    
