"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required,verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)



@api.route('/user', methods=['GET'])
def get_users():

    result = db.session.scalars(db.select(User)).all()
    response_body = list(map(lambda item: item.serialize(),result))

    if response_body == []:
        return jsonify({"msg":"there are no registered users"}), 404

    return jsonify({"results":response_body}), 200

@api.route('/signup', methods=['POST'])
def signup():
    try:
        request_body=request.json
        user = db.session.execute(db.select(User).filter_by(email=request_body["email"])).scalar_one()
        return jsonify({"msg":"user exist"}), 401
    except:
        user = User(email=request_body["email"], password=request_body["password"],is_active=request_body["is_active"])
        db.session.add(user)
        db.session.commit()
        return jsonify({"msg":"created"}), 201

@api.route("/login", methods=["POST"])
def login():

    email = request.json.get("email", None)
    password = request.json.get("password", None)
    try:
        user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one()
        if password != user.password:
            return jsonify({"msg": "Bad email or password"}), 401
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token)
    except:
        return jsonify({"msg": "this user does not exist"}), 404

@api.route("/private", methods=["GET"])
@jwt_required()
def private():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@api.route("/verify-token", methods=["GET"])
def verify_token():
    try:
        verify_jwt_in_request()  # Verifica la validez del token
        identity = get_jwt_identity()  # Obtiene el usuario del token
        return jsonify({"valid": True, "user": identity}), 200
    except NoAuthorizationError:
        return jsonify({"valid": False, "message": "Token inválido o no proporcionado"}), 401