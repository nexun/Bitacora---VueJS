from flaskps.models import neighborhood
from flask import jsonify


def get_all():
    response = [{
        'id': neighborhood.id,
        'name':neighborhood.name
    } for neighborhood in neighborhood.get_all()]
    return jsonify(response)