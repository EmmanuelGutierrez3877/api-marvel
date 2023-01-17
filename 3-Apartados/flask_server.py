from flask import Flask, request
from layaway import *

app = Flask(__name__)

@app.post("/addToLayaway/")
def new():
    token = request.args.get('token')
    comic = request.args.get('comic')
    cantidad = request.args.get('cantidad')
    apartado = new_apartado(token,comic,cantidad)
    return apartado


app.run(host='0.0.0.0', port=8000, debug=False)
#app.run(host='0.0.0.0', port=8003, debug=False)