from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class QueryForm(FlaskForm):
    query_input = StringField()
    query_order = StringField(validators=[DataRequired(), Length(1)])
    query_page = IntegerField(validators=[DataRequired(), NumberRange(1)])
