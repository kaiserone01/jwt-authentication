"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
import json
from flask_cors import CORS, cross_origin

api = Blueprint('api', __name__)
CORS(api)

@api.route('/hello', methods=['POST', 'GET'])
@cross_origin()
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/sign-up', methods=['POST'])
def handle_register():

    data = request.data
    data_decode = json.loads(data)
    newUser = User(**data_decode)
    user = User.query.filter_by(email=newUser.email,password=newUser.password).first()
    if user is None:
        db.session.add(newUser)
        db.session.commit()
        response_body = {
            "message": "Usuario creado con exito",
            "token":"token"
        }
        return jsonify(response_body), 200
    else :
        response_body = {
            "message": "Usuario ya existe"
        }
        return jsonify(response_body), 400

