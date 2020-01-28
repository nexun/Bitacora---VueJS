from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email


class PublicInfoForm(FlaskForm):
    public_info_title_input = StringField(validators=[DataRequired()])

    public_info_description_input = StringField(
        validators=[DataRequired(), Length(max=255)])

    public_info_contact_email_input = StringField(
        validators=[DataRequired(), Email()])
