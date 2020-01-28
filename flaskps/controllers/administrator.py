from flask import jsonify
from flaskps.models import administrator


def index():
    response = [{
        'id': administrator.id,
        'username': administrator.username,
        'email': administrator.email,
        'first_name': administrator.first_name,
        'last_name': administrator.last_name
    } for administrator in administrator.get_all()]
    return jsonify(response)