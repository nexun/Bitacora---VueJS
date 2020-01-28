from flask import request, session, Response, jsonify
from flaskps.models import auth, user
from flaskps.classes.forms.loginform import LoginForm
from flaskps import hashing


def logout():
    session.pop('user', None)
    return Response(status=200)


def authenticate():
    form = LoginForm()
    user_data = request.form
    if form.validate_on_submit():
        email = str(user_data['inputEmail'])
        get_pass = str(user_data['inputPassword'])            
        password = hashing.hash_value(get_pass, salt='grupo15')            
        if(auth.authenticate(email, password)):
            open_session(email)
            user = {
                'id': session['user'].id,
                'username': session['user'].username,
                'email': session['user'].email,
                'first_name': session['user'].first_name,
                'last_name': session['user'].last_name,
                'photo': session['user'].photo,
                'roles': session['roles'],
                'permissions': session['permissions']
            }
            return jsonify({'user': user})
        else:
            return Response(status=400)
    else:
        return Response(status=400)        


def open_session(email):
    session['user'] = user.get_by_email(email)
    session['roles'] = [role.name for role in user.get_roles_by_email(email)]
    session['permissions'] = [permission.name for permission in auth.get_permissions_by_email(email)]


def authorize(endpoint):
    if endpoint in session['permissions']:
        return Response(status=200)
    else:
        response = jsonify({
            'exception': 'RestrictedAcess'
        })
        response.status_code = 403
        return response