from flask import Blueprint
from flask import jsonify, request
from flask_jwt_extended import (
    jwt_required, fresh_jwt_required, JWTManager, jwt_refresh_token_required,
    jwt_optional, create_access_token, create_refresh_token, get_jwt_identity,
    decode_token
)
from flask_restplus import Resource, Api
from services.UsersService import UsersService
from app import app

users_api = Blueprint('users_api', __name__)

# app = Api(app = app)

users_service = UsersService()

@users_api.route('/users/login',
                 methods = ['POST'])
def login():
    try:
        app.logger.info("in /login")
        json = request.json
        username = json['username']
        password = json['password']
        user_id = users_service.login(username,
                                      password)
        #print(user_id)
        if user_id is None:
            resp = jsonify({'message': 'incorrect username or password'})
            resp.status_code = 401
        else:
            app.logger.info("user_id: " + str(user_id['id']))
            access_token = create_access_token(identity=user_id['id'])
            resp = jsonify({'token': 'Bearer {}'.format(access_token)})
            resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@users_api.route('/users',
                 methods = ['GET'])
#@jwt_required
def get_users():
    try:
        app.logger.info("in /users")
        user_id = request.args.get('id', default = None, type = int)
        user_name = request.args.get('name', default = None, type = str)
        if user_id is not None:
            user = users_service.get_user_by_id(user_id)
            if user is None:
                resp = jsonify({'message': 'user not found'})
                resp.status_code = 404
            else:
                app.logger.info("user: " + str(user))
                resp = jsonify(user)
                resp.status_code = 200
        elif user_name is not None:
            # Buscar por nombre
            user = users_service.get_user_by_name(user_name)
            if user is None:
                resp = jsonify({'message': 'user not found'})
                resp.status_code = 404
            else:
                app.logger.info("user: " + str(user))
                resp = jsonify(user)
                resp.status_code = 200
        else:
            # Buscar todos los usuarios
            user = users_service.get_all_users()
            app.logger.info("users: " + str(user))
            resp = jsonify(user)
            resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@users_api.route('/users/userCreate',
                 methods = ['POST'])
def crear_nuevo_usuario():
    try:
        app.logger.info("in /userCreate")
        json = request.json
        email = json['email']
        name = json['name']
        username = json['username']
        password = json['password']
        rowsAffected = users_service.crear_nuevo_usuario(email, name, password, username) #como es insert
        resp = jsonify({'message': 'Succesful'})                                          #se retorna un None
        resp.status_code = 200
        return resp
    except Exception as e:
        #print(e)
        resp = jsonify({'message': 'Error in registration'})
        resp.status_code = 401