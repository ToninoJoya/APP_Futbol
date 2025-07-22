"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash


api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)

def set_password(password, salt): 
    return generate_password_hash(f"{password}{salt}")

def check_password(pass_hash, password, salt):
    return check_password_hash(pass_hash, f"{password}{salt}")


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200
@api.route("/register", methods = ["POST"])
def register_user():
    data = request.json
    if not data: 
        return jsonify("No has ingresado tus datos para el registro"), 400
    
    email = data.get("email")
    password = data.get("password")
    is_active = data.get("is_active", True)

    if not email or not password:
        return jsonify("necesitas un email y tu contraseña para completar el registro"), 400
    
    usuario = User(email=email, password=set_password(password, salt=15), is_active=is_active)

    db.session.add(usuario)
    try:
        db.session.commit()
        return jsonify ("el usuario ha sido creado existosamente"), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify("El email ya está registrado. Intenta con otro."), 409
    except Exception as error: 
        db.session.rollback()
        return jsonify (f"hubo un error al registrarse:{error.args}"), 500

@api.route("/login", methods=["POST"])
def handle_login():
    data = request.json

    if not data: 
        return jsonify("No hemos recibido datos"), 400
    
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify("Necesitas completar todos los campos"), 400
    
    usuario = User.query.filter_by(email=email).one_or_none()
    if not usuario:
        return jsonify("Credenciales incorrectas")
    else:
        if(check_password(usuario.password, password, salt=15)):
            token = create_access_token(identity=str(usuario.id))
            return jsonify({
                "token":token
            }), 200
        else:
            return jsonify ("Credenciales incorrectas"), 401


@api.route("/user", methods=["GET"])
@jwt_required()
def get_user():
    user_id = get_jwt_identity()
    usuario = User.query.get(user_id)
    if not usuario: 
        return jsonify("Usuario no encontrado"), 404

    return jsonify(usuario.serialize()), 200

   
