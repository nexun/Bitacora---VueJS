from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, AnyOf


class MaintenanceModeForm(FlaskForm):
    set_maintenance_mode = StringField(
        validators=[DataRequired(), AnyOf(['true', 'false'])])
