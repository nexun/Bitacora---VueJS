from flask import request, Response, jsonify
from flaskps.models import item
from flaskps.classes.forms.Item import addItemForm
from datetime import datetime
from password_generator import PasswordGenerator


def index():
    response = [{
        'id': item.iditem,
        'tittle': item.tittle,
        'description': item.description,
        'code': item.code,
        'id_category': item.id_category,
        'id_state': item.id_state,
        'solution': item.solution,
        'created_at': item.created_at,
    } for item in item.get_all()]
    return jsonify(response)

def up():
    form = addItemForm()
    if form.validate_on_submit():
        tittle = request.form['tittle']       
        
        if item.check_exist_by_tittle(tittle) == 1:
            return Response(status=501)
        else:    
            pwo = PasswordGenerator()
            code = (pwo.generate())[1:6]
            description = request.form['description']
            id_c = request.form['id_category']
            id_s = 1
            created = datetime.now()
            item.create(code, tittle, description, id_c, id_s, created)                      
            return Response(status=200)
    else:
        response = jsonify(list(form.errors.keys()))
        response.status_code = 400
        return response

def item_update(id):
    form = addItemForm()
    if form.validate_on_submit():

        #vars
        tittle = request.form['tittle']           

        if item.get_tittle_by_id(id) != tittle:
            if item.check_exist_by_tittle(tittle) == 1:
                return Response(status=501)

        #update
        code = 'Err01'
        description = request.form['description']
        id_c = request.form['id_category']
        id_s = request.form['id_state']
        updated = datetime.now()
        item.update_item_info_nosolution(id, code, tittle, description, id_c, id_s, updated)                            
        return Response(status=200)        
    else:
        response = jsonify(list(form.errors.keys()))
        response.status_code = 400
        return response    

def get_item(id):
    if (item.check_exist_by_id(id) == 1):
        data = item.get_by_id(id)    
        response = {
        'id': data.iditem,
        'tittle': data.tittle,
        'description': data.description,
        'code': data.code,
        'id_category': data.id_category,
        'id_state': data.id_state,
        'solution': data.solution,
        'created_at': data.created_at,  
        'updated_at': data.updated_at,                
              
        }
        return jsonify(response)
    else:     
        return Response(status=400)        

def exist(id):  
    if (item.check_exist_by_id(id) == 1):
        response = {'value':'True' }
    else:
        response = {'value':'False'}         
    return jsonify(response)

def item_delete(id):   
    item.delete_item(id) 
    return Response(status=200)         
