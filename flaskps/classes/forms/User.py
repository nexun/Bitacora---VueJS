from flask_wtf import FlaskForm
from wtforms import StringField, FieldList, BooleanField
from wtforms.validators import DataRequired, Length, Email


class addUserform(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()])
    first_name = StringField(validators=[DataRequired()])
    last_name = StringField(validators=[DataRequired()])
    roles = BooleanField(validators=[DataRequired()])

class updateUserForm(FlaskForm):
    first_name_input = StringField(validators=[DataRequired()])
    last_name_input = StringField(validators=[DataRequired()])
    email_input = StringField(validators=[DataRequired(), Email()])