from flask_wtf import FlaskForm
from wtforms import FieldList, StringField
from wtforms.validators import DataRequired, Email

class InviteEmailListForm(FlaskForm):
    email = FieldList(StringField(validators=[DataRequired(), Email()]), validators=[DataRequired()])