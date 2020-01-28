from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired, NumberRange


class PaginationForm(FlaskForm):
    items_per_page_input = IntegerField(
        validators=[DataRequired(), NumberRange(1)])
