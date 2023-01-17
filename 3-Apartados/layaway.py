import requests
from database import *
from bson.json_util import dumps
from flask import Response
import json

def new_apartado(token,comic,cantidad):
    if (cantidad == None):
        return Response( "cantidad invalida", status=400)
        
    try:
        int(cantidad)
    except ValueError:
        return Response( "cantidad invalida", status=400)
    

    pageUser = "http://Usuarios:8000/users/data?token={}".format(token)
    res = requests.get(pageUser)
    if (res.status_code == 404):
        return Response( "token invalido", status=400,)
    else:
        resUser = res.json()

    pageComic = "http://Busqueda:8000/searchComics/id?id={}".format(comic)
    res = requests.get(pageComic)
    if (res.status_code != 200):
        return Response( "comic invalido", status=404,)
    else:
        resComic =  res.json()
    
    res = insert_apartado(resUser['_id'],resComic['id'],cantidad)

    return json.loads(dumps(res))
