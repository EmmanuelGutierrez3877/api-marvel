from pymongo import MongoClient
from pymongo import ReturnDocument
from bson.objectid import ObjectId


def get_database():
   CONNECTION_STRING = "mongodb://alex:1234@DB_Comics:27017/?authMechanism=DEFAULT"
   #CONNECTION_STRING = "mongodb://localhost:27017/"
   client = MongoClient(CONNECTION_STRING)
   db = client['comics']
   print("connected")
   return db

def insert_apartado(user,comic,cantidad):

    apartado = db.apartados.find_one({'user':ObjectId(user['$oid']),'comic':comic})

    if(apartado == None):
        apartado = db.apartados.insert_one({'user':ObjectId(user['$oid']),'comic':comic,'cantidad':int(cantidad)})
        id = apartado.inserted_id
        return db.apartados.find_one({'_id':id})

    else:
        cantidad = int(cantidad) + apartado['cantidad']
        apartado = db.apartados.find_one_and_update(
            {'user':ObjectId(user['$oid']),'comic':comic},
            {'$set':{'cantidad':cantidad}},
            return_document = ReturnDocument.AFTER
        )
        return apartado


    
db = get_database()