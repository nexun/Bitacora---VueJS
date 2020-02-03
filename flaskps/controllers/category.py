from flask import request, Response, jsonify
from flaskps.models import category
from flaskps.classes.forms.Category import addCategoryForm


def index():
    response = [{
        'id': category.idcategory,
        'name': category.name,
    } for category in category.get_all()]
    return jsonify(response)

def up():
    form = addCategoryForm()
    if form.validate_on_submit():
        name = request.form['name']       
        
        if category.check_exist_by_name(name) == 1:
            return Response(status=501)
        else:    
            category.create(name)                      
            return Response(status=200)
    else:
        response = jsonify(list(form.errors.keys()))
        response.status_code = 400
        return response

def category_update(id):
    form = addCategoryForm()
    if form.validate_on_submit():

        #vars
        name = request.form['name']           

        if category.get_name_by_id(id) != name:
            if category.check_exist_by_name(name) == 1:
                return Response(status=501)

        #update
        category.update_category_info(id, name)                            
        return Response(status=200)        
    else:
        response = jsonify(list(form.errors.keys()))
        response.status_code = 400
        return response    

def get_category(id):
    if (category.check_exist_by_id(id) == 1):
        data = category.get_by_id(id)    
        response = {
        'category_data_name': data.name,                
        }
        return jsonify(response)
    else:     
        return Response(status=400)        

def exist(id):  
    if (category.check_exist_by_id(id) == 1):
        response = {'value':'True' }
    else:
        response = {'value':'False'}         
    return jsonify(response)

def category_delete(id):   
    category.delete_category(id) 
    return Response(status=200)         
