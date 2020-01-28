from flaskps import app
from flaskps.util.feedback import *
from flask import render_template, redirect, url_for, Response, jsonify
from flaskps.models.feedback import Feedback


@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html')
    # msj = 'La página que estás buscando no existe.'
    # data = Feedback.data(msj, 'Página no encontrada')
    # return render_template('feedback.html', data=data), 404


@app.errorhandler(500)
def server_error(e):
    return Response(status=500)
    # msj = 'Lo sentimos, en este momento no podemos atender tu solicitud.'
    # data = Feedback.data(msj)
    # return render_template('feedback.html', data=data), 500


@app.errorhandler(Exception)
def kaboom(e):
    return e
    # if app.config['ENV'] != 'production':
    #     raise e
    # else:
    #     data = Feedback.data('Algo salió mal.', 'Ups!')
    #     return render_template('feedback.html', data=data), 500


@app.errorhandler(PageUnderConstruction)
def page_under_construction(e):
    pass
    # msj = 'Esta página estará disponible próximamente.'
    # data = Feedback.data(msj, 'Página en construcción')
    # return render_template('feedback.html', data=data), 501

@app.errorhandler(501)
def usuario_repetido(e):
    msj = 'El usuario ya se encuentra registrado.'
    data = Feedback.data(msj, 'Usuario ya esta registrado')
    return render_template('feedback.html', data=data), 501

@app.errorhandler(501)
def unico_admin(e):
    msj = 'No puedes dejar la pagina sin administradores.'
    data = Feedback.data(msj, 'Unico administrador')
    return render_template('feedback.html', data=data), 501    

@app.errorhandler(AppInMaintenanceMode)
def app_in_maintenance_mode(e):
    response = jsonify({
        'exception': 'AppInMaintenanceMode'
    })
    response.status_code = 503
    return response

@app.errorhandler(RestrictedAcess)
def page_restricted_access(e):
    response = jsonify({
        'exception': 'RestrictedAcess'
    })
    response.status_code = 403
    return response

@app.errorhandler(UserIsBloqued)
def user_is_blocked(e):
    response = jsonify({
        'exception': 'UserIsBloqued'
    })
    response.status_code = 403
    return response

@app.errorhandler(UserHasNoSession)
def user_has_not_session(e):
    response = jsonify({
        'exception': 'UserHasNoSession'
    })
    response.status_code = 401
    return response

@app.errorhandler(ChangeBaseRole)
def change_base_role(e):
    msj = 'No puede cambiar los parametros del rol base.'
    data = Feedback.data(msj, 'Operacion denegada')
    return render_template('feedback.html', data=data), 403

@app.errorhandler(FailEmailSend)
def fail_email_send(e):
    msj = 'No pudimos crear al usuario. Por favor verificá que la dirección de email que proporcionaste sea la correcta y volvé a intentarlo.'
    data = Feedback.data(msj, 'Usuario no creado')
    return render_template('feedback.html', data=data), 403
