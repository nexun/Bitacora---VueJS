from flask import request, redirect, url_for, session, render_template
from flaskps.util.feedback import AppInMaintenanceMode, RestrictedAcess, UserHasNoSession, UserIsBloqued
from flaskps.util.permissions import checkPermissions
from flaskps.models import auth
from flaskps.models import user
from flaskps.models import configuration

filters_session = ['static',
                   'auth_login',
                   'auth_authenticate',
                   'confirm_email',
                   'change_password',
                   'home_index',
                   'check_link']

filters_permission = ['static',
                      'auth_login',
                      'auth_authenticate',
                      'confirm_email',
                      'change_password',
                      'auth_authorize',
                      'check_link']


def check_maintenace_mode():
    if 'user' in session:
        is_maintenance_mode = True if configuration.get_is_maintenance_mode() == "true" else False
        is_admin = 'administrator' in session['roles']
        if 'static' not in request.path and not is_admin and is_maintenance_mode:
            session.pop('user', None)
            raise AppInMaintenanceMode
    

def is_bloqued():
    if 'user' in session:
        if(session['user'].bloqued == 'si'):
            session.pop('user', None)
            raise UserIsBloqued


def has_session():
    if request.endpoint and request.endpoint not in filters_session and 'user' not in session:
        raise UserHasNoSession


def has_permission():
    if 'user' in session and request.endpoint:
        if request.endpoint not in filters_permission:
            permissions = auth.get_permissions_by_username(session['user'].username)
            all_p = []
            for p in permissions:
                all_p.append(p.name)
            if not checkPermissions(all_p, request.endpoint):
                raise RestrictedAcess
