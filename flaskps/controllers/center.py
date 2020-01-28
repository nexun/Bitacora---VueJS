from flask import request, Response, jsonify, session
import requests
from flaskps.models import center
from flaskps.classes.forms.Center import addCenterForm, updateCenterForm
from flaskps.config import Config


def index():
    response = [{
        'id': center.id,
        'name': center.name,
        'address': center.address,
        'phone_number': center.phone_number
    } for center in center.get_all()]
    return jsonify(response)

def up():
    form = addCenterForm()
    if form.validate_on_submit():
        name = request.form['name']       
        phone = request.form['phone']
        address = request.form['address']
        city = request.form['city']

        dir = name +' '+ city
        params = {'address' : dir}        
        url = 'https://maps.googleapis.com/maps/api/geocode/json?,+CA&key='+Config.MAPS_API_KEY
        location = requests.get(url = url, params = params)  
        latitude = location.json()['results'][0]['geometry']['location']['lat'] 
        longitude = location.json()['results'][0]['geometry']['location']['lng']                      

        if center.check_exist_by_name(name) == 1:
            return Response(status=501)
        else:    
            center.create(name, phone, address, latitude, longitude)                      
            return Response(status=200)
    else:
        response = jsonify(list(form.errors.keys()))
        response.status_code = 400
        return response

def center_update(id):
    form = updateCenterForm()
    if form.validate_on_submit():

        #vars
        name = request.form['name']       
        phone = request.form['phone']
        address = request.form['address']         
        latitude = request.form['lat'] 
        longitude = request.form['lng']     

        if center.get_name_by_id(id) != name:
            if center.check_exist_by_name(name) == 1:
                return Response(status=501)

        #update
        center.update_center_info(id, name, address, phone, latitude, longitude)                            
        return Response(status=200)        
    else:
        response = jsonify(list(form.errors.keys()))
        response.status_code = 400
        return response    

def get_center_profile(id):
    if (center.check_exist_by_id(id) == 1):
        data = center.get_by_id(id)    
        response = {
        'center_data_name': data.name,        
        'center_data_address': data.address,
        'center_data_phone': data.phone_number,
        'latitude' : data.lat,
        'longitude' : data.lng       
        }
        return jsonify(response)
    else:     
        return Response(status=400)        

def exist(id):  
    if (center.check_exist_by_id(id) == 1):
        response = {'value':'True' }
    else:
        response = {'value':'False'}         
    return jsonify(response)

def center_delete(id):   
    center.delete_center(id) 
    return Response(status=200)         
