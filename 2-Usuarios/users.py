import hashlib
from flask import Response
from database import *

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
        user = str(insert_user(user))
        return user
    else:
        #print("usuario ya existe")
        return Response( "Usuario ya existe", status=400,)

def get_user(name):
    user = find_user(name)
    return user

def login(name,password):
    user = find_user(name)
    if (user != None):
        token = user['token']
        return token
    else:
        return Response( "Error en usuario y/o contraseña", status=400,)

def data_user(token):
    user = find_user(None,None,token)
    if (user != None):
        return str(user)
    else:
        return Response( "Error en token", status=400,)

#get_user("alex")
#new_user('alex','123456','25')