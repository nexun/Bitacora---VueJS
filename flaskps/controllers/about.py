from flask import jsonify 
from flaskps.models import about


def getInfo():
    response = [{
        'name': about.name,
        'value': about.value
    } for about in about.get_all()]
    return jsonify(response)