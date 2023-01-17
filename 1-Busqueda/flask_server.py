from flask import Flask, request
from characters import *

app = Flask(__name__)

@app.get("/searchComics/")
def search():
    name = request.args.get('name')
    filter = request.args.get('filter')
    return searchCharacter(name,filter)

@app.get("/searchComics/id/")
def comic():
    id = request.args.get('id')
    return searchComic(id)

app.run(host='0.0.0.0', port=8000, debug=False)
#app.run(host='0.0.0.0', port=8001, debug=False)