from pymongo import MongoClient

def get_database():
   CONNECTION_STRING = "mongodb://alex:1234@DB_Comics:27017/?authMechanism=DEFAULT"
   #CONNECTION_STRING = "mongodb://localhost:27017/"
   client = MongoClient(CONNECTION_STRING)
   db = client['comics']
   print("connected")
   return db

def insert_user(user):
    user = db.users.insert_one(user)
    id = user.inserted_id
    return db.users.find_one({'_id':id})

def find_user(name, password=None, token=None):
    if (password != None):
        return db.users.find_one({'name':name, 'password':password})
    elif ( token != None):
        return db.users.find_one({'token':token })
    else:
        return db.users.find_one({'name':name})
    
db = get_database()