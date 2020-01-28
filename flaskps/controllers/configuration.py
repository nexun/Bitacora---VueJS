from flask import request, Response, jsonify
from flaskps.models import configuration
from flaskps.classes.forms.pagination import PaginationForm
from flaskps.classes.forms.public_info import PublicInfoForm
from flaskps.classes.forms.maintenance_mode import MaintenanceModeForm


def index():
    response = {
        'config_options_app_title': configuration.get_app_title(),
        'config_options_app_description': configuration.get_app_description(),
        'config_options_app_contact_email':  configuration.get_app_contact_email(),
        'config_options_items_per_page': configuration.get_items_per_page(),
        'config_options_is_maintenance_mode': configuration.get_is_maintenance_mode()
    }
    return jsonify(response)


def public_info():
    response = {
        'config_options_app_title': configuration.get_app_title(),
        'config_options_app_description': configuration.get_app_description(),
        'config_options_app_contact_email':  configuration.get_app_contact_email()
    }
    return jsonify(response)


def pagination():
    response = {
        'config_options_items_per_page': configuration.get_items_per_page()
    }
    return jsonify(response)


def maintenance_mode():
    response = {
        'config_options_is_maintenance_mode': configuration.get_is_maintenance_mode()
    }
    return jsonify(response)


def update_pagination():
    form = PaginationForm()
    if form.validate_on_submit():
        configuration.update_pagination(
            int(request.form['items_per_page_input']))
        return Response(status=200)
    else:
        response = jsonify(list(form.errors.keys()))
        response.status_code = 400
        return response


def update_public_info():
    form = PublicInfoForm()
    if form.validate_on_submit():
        configuration.update_public_info(
            request.form['public_info_title_input'],
            request.form['public_info_description_input'],
            request.form['public_info_contact_email_input']
        )
        return Response(status=200)
    else:
        response = jsonify(list(form.errors.keys()))
        response.status_code = 400
        return response


def toggle_maintenance_mode():
    form = MaintenanceModeForm()
    if form.validate_on_submit():
        configuration.update_maintenance_mode(request.form['set_maintenance_mode'])
        return Response(status=200)
    else:
        response = jsonify(list(form.errors.keys()))
        response.status_code = 400
        return response
