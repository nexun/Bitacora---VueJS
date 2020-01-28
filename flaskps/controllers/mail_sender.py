from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from flaskps import app, mail
from flaskps.models import user
from flask import url_for, redirect, Request, Response, jsonify, json, request, render_template
from flaskps import hashing
from flaskps.controllers.feedback import page_not_found
from flaskps.config import Config


def send_to(email):
    last_id = str(user.get_id_by_email(email))     
    dire = hashing.hash_value(email, salt='grupo15')
    msg = Message("Confirm Email", recipients=[email])
    link = Config.LINK + '/activate?id=' + last_id + '&hash=' + dire
    msg.body = "Your link is {}".format(link)    
    msg.html = "<a href={} >Click aqui para activar</a>".format(link)
    mail.send(msg)        



def confirm_email(token_id, token_hash):
    email = str(user.get_email_by_id(token_id))
    if  hashing.check_value(token_hash,email, salt='grupo15'):
        cant = str(user.get_confirm_value_by_id(token_id))
        if cant == 'si':
            return page_not_found(400)
        else:
            return redirect('/activate/'+token_id+'/'+token_hash)
            #return render_template('user/activate_password.html', email = email )

    else:
        return page_not_found(400)
        
       
def check_link():
    id = request.form['id']
    token = request.form['hash']   
    email = str(user.get_email_by_id(id))    
    if  hashing.check_value(token, email, salt='grupo15'):
        cant = str(user.get_confirm_value_by_id(id))
        if cant == 'si':
            response = {
            'valid': 'False'      
            }
        else:
            response = {
            'valid': 'True'      
            }
    else:
        response = {
            'valid': 'False'      
            }
    return jsonify(response)        