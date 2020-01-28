from flask_wtf import FlaskForm
from wtforms import Form, StringField
from wtforms.validators import DataRequired, Length, Regexp


class RoleForm(Form):
    name_role = StringField('name_rol',[DataRequired(message="El nombre del rol no puede estar vacio"), Length(min=4, max=20, message="El nombre del rol debe ser superior a 4 e inferior a 20 caracteres"), Regexp(
        "[A-Za-z_]+$", message="El nombre del rol no debe contener numeros, espacios ni caracteres especiales (a excepcion del '_')")])

class PermissionForm(Form):
    name_permission = StringField('name_permission',[DataRequired(message="El nombre del permiso no puede estar vacio"), Length(min=4, max=20, message="El nombre del permiso debe ser superior a 4 e inferior a 20 caracteres"), Regexp(
        "[A-Za-z\s]+$", message="El nombre del permiso no debe contener numeros ni caracteres especiales")])
    code_permission = StringField('code_permission',[DataRequired(message="El codigo del permiso no puede estar vacio"), Length(min=4, max=20, message="El codigo del permiso debe ser superior a 4 e inferior a 20 caracteres"), Regexp(
        "[A-Za-z_]+$", message="El codigo del permiso no debe contener numeros, espacios ni caracteres especiales (a excepcion del '_')")])
