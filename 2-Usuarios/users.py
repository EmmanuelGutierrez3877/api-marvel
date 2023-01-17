import hashlib
from flask import Response, make_response
from database import *
from bson.json_util import dumps
import json

def new_user(name,password,age):
    exist = get_user(name)
    if (exist == None):
        aux = (name+password)
        token = hashlib.md5(aux.encode()).hexdigest()
        user = {
            'name':name,
            'password':password,
            'age':age,
            'token':token
        }
        user = insert_user(user)
        user = json.loads(dumps(user))
        return make_response(user, 200)
    else:
        #print("usuario ya existe")
        return Response( "Usuario ya existe", status=400,)

def get_user(name):
    user = find_user(name)
    return user

def login(name,password):
    user = find_user(name,password)
    if (user != None):
        token = user['token']
        return make_response(token, 200)
    else:
        return Response( "Error en usuario y/o contraseña", status=400,)

def data_user(token):
    user = find_user(None,None,token)
    if (user != None):
        user = json.loads(dumps(user))
        return make_response(user, 200)
    else:
        return Response( "Error en token", status=404,)

#get_user("alex")
#new_user('alex','123456','25')