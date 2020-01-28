from flaskps.models import user
import os
from flask import current_app as app
from flask import request, Response, jsonify, session
from flaskps.classes.forms.User import addUserform, updateUserForm
from flaskps.classes.forms.Activate import activate
from flaskps.util.feedback import PageUnderConstruction, FailEmailSend
from flaskps.controllers.feedback import unico_admin
from flaskps.controllers import mail_sender,role
from flaskps.controllers.feedback import page_not_found
from flaskps import hashing
from password_generator import PasswordGenerator
from datetime import datetime
from werkzeug.utils import secure_filename


def index():
    response = [{
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'bloqued': user.bloqued,
        'confirmed': user.confirmed
    } for user in user.get_all()]
    return jsonify(response)


def get_all():  
     return user.get_all()


def get_cant_bloqued():   
    data = user.get_cant_bloqued()  
    tot = user.get_cant()  
    response = {
        'cant_bloqued':data,
        'cant_tot': tot,

    }     
    return jsonify(response)    

def get_cant_confirmed():  
    data = user.get_cant_confirmed()  
    tot = user.get_cant()  
    response = {
        'cant_confirmed':data,
        'cant_tot': tot,

    }         
    return jsonify(response)    

def exist(id):  
    if (user.check_exist_by_id(id) == 1):
        response = {'value':'True' }
    else:
        response = {'value':'False'}         
    return jsonify(response)
    

def up():
    form = addUserform()
    roles = request.form.getlist("roles")    
    if form.validate_on_submit():
        email = request.form['email']
        fn = request.form['first_name']
        ln = request.form['last_name']
        if str(user.check_exist_by_email(email)) == '1':
            return Response(status=501)
        else:    
            pwo = PasswordGenerator()
            generate = pwo.generate()
            passwd = hashing.hash_value(generate, salt='grupo15')
            user.create(email, fn, ln, passwd,datetime.now())                           
            id_user = str(user.get_by_email(email).id)
            user.set_user_roles(id_user, roles)                          
            mail_sender.send_to(email)              
            return Response(status=200)
    else:
        response = jsonify(list(form.errors.keys()))
        response.status_code = 400
        return response


def activate_account():
    form = activate()    
    if form.validate_on_submit():        
        id = request.form['id']
        token = request.form['token']
        email = str(user.get_email_by_id(id))     
        password = request.form['password']
        if  hashing.check_value(token,email, salt='grupo15'):            
            hashed_password = hashing.hash_value(password, salt='grupo15')
            user.set_user_password(email,hashed_password)
            user.set_confirm_value(email, datetime.now())
            return Response(status=200) 
        else:            
            return page_not_found(400)
    else:
        response = jsonify(list(form.errors.keys()))
        response.status_code = 400
        return response


def user_update(id):   
    form = updateUserForm()
    if form.validate_on_submit():
        #vars        
        username = user.get_username_by_id(id)
        email = request.form['email_input']
        fn = request.form['first_name_input']
        ln = request.form['last_name_input']
        password = str(request.form['password_input'])
        email_old = str(user.get_email_by_id(id))   
        filename = ""    
        if request.files:
                        if not allowed_image_filesize(request.form['photo_size']):
                            response = jsonify(["photo"])
                            response.status_code = 400
                            return response
                        else:
                            image = request.files["photo"]
                            if image.filename == "":
                                response = jsonify(["photo"])
                                response.status_code = 400
                                return response
                            if not allowed_image_extension(image.filename):
                                response = jsonify(["photo"])
                                response.status_code = 400
                                return response
                            else:
                                ext = image.filename.rsplit(".", 1)[1]
                                filename = secure_filename(
                                    "image_user_"+id+"."+ext)
                                image.save(os.path.join(
                                    app.config['IMAGE_USER'], filename))                    
                                #update
                                user.update_user_info(id, email,fn, ln, filename)
                                if  username in session['user'].username:
                                    session['user'].photo = filename
        user.update_user_info(id, email,fn, ln, filename)
        #check
        if password != 'password':
            password = hashing.hash_value(password, salt='grupo15')
            user.update_user_password(id, password)
        if email_old != email:
            if  username in session['user'].username:
                session.pop('user')                            
        return Response(status=200)        
    else:
        response = jsonify(list(form.errors.keys()))
        response.status_code = 400
        return response        


def get_user_profile(id):
    data = user.get_by_id(id)    
    if data is not None:        
        role = user.get_roles_by_id(id)
        response = {
        'user_data_first_name': data.first_name,
        'user_data_last_name': data.last_name,
        'user_data_email':  data.email,
        'photo': data.photo,
        }
        return jsonify(response)
    else:
        return page_not_found(400)


def get_user_roles(id):    
    roles = user.get_roles_by_id(id)
    if roles is not None:        
        names = [role.name for role in roles]
        return jsonify(names)
    else:
        return page_not_found(400)


def set_bloqued_value(id):
    value = request.form['set_bloqued_button']
    username = user.get_username_by_id(id)
    if value == 'True':
        data = 'si'        
    else:
        data = 'no'      

    if username == session['user'].username:
        return Response(status=404)

    user.set_bloqued_value(id,data)   
    return Response(status=200)   


def get_bloqued_value(id):  
    data = user.get_bloqued_value(id)
    if data is not None: 
        if data == 'si':
            response = {
                'user_bloqued_value': 'True'      
                }
        else:
            response = {
                'user_bloqued_value': 'False'      
            }
        return jsonify(response)
    else:
        return page_not_found(400)



def user_delete(id):   
    delete_user_id = id
    username = str(user.get_username_by_id(delete_user_id))
    if username in session['user'].username:
        return Response(status=404)             
    user.delete_user(delete_user_id) 
    return Response(status=200)     


def set_user_roles(id):
    roles = request.form.getlist("roles")
    username = str(user.get_username_by_id(id))

    if 'administrator' in roles:
        user.delete_user_role(id) 
        user.set_user_roles(id,roles)    
        if username in session['user'].username:
            session.pop('user') 
        return Response(status=200)              
    else:   
        if user.admin_count_check() > 1:
            user.delete_user_role(id)
            user.set_user_roles(id,roles)    
            return Response(status=200) 
        else:
            if user.admin_user_check(id) == 1:
                return unico_admin(501)   
            else:
                user.delete_user_role(id) 
                user.set_user_roles(id,roles)
                if username in session['user'].username:
                    session.pop('user')     
                return Response(status=200) 

def get_cant_roles():  
    response = [{
        'id_role':role.id,
        'cant': user.get_cant_per_role(role.id),

    } for role in role.show_ids()]         
    return jsonify(response)                

def allowed_image_extension(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config['ALLOW_IMAGE_EXTENSIONS']:
        return True
    else:
        return False


def allowed_image_filesize(filesize):
    if int(filesize) <= app.config['MAX_IMAGE_FILESIZE']:
        return True
    else:
        return False