from flask import Flask, request
from users import *

app = Flask(__name__)

@app.post("/users/")
def new():
    name = request.args.get('name')
    password = request.args.get('password')
    age = request.args.get('age')
    user = new_user(name,password,age)
    return user

@app.get("/users/")
def search():
    name = request.args.get('name')
    password = request.args.get('password')
    token = login(name,password)
    return token

@app.get("/users/data/")
def data():
    token = request.args.get('token')
    user = data_user(token)
    return user

app.run(host='0.0.0.0', port=8000, debug=False)