from flask import Flask, request
from characters import *

app = Flask(__name__)

@app.get("/searchComics/")
def search():
    name = request.args.get('name')
    filter = request.args.get('filter')
    return searchCharacter(name,filter)

app.run(host='0.0.0.0', port=8000, debug=False)