
from flask import Flask
from flask import request

import json
#import log

app = Flask(__name__)

productos = list()
productos.append({"Id":1, "Nombre" : "Leche", "valor" : 500})
productos.append({"Id":2, "Nombre" : "Cafe", "valor" : 600})
productos.append({"Id":3, "Nombre" : "Azucar", "valor" : 300})
productos.append({"Id":4, "Nombre" : "Arroz", "valor" : 400})


# exponer un servicio GET /, devuelve todos los objetos actuales de la lista
# impl opentelemetry
@app.route('/', methods=['GET'])
def get_productos():
    jsonString = json.dumps(productos)
    return jsonString


# exponer un servicio GET /producto/{id}, devuelve el elemento del id
# impl opentelemetry
@app.route('/producto/<id>', methods=['GET'])
def get_producto(id=None):
    jsonString = json.dumps(productos[int(id)])
    return jsonString


# exponer un servicio POST /producto, agrega elementos a la lista
# impl opentelemetry
@app.route('/producto/<id>/<nombre>/<valor>', methods=['POST'])
def add_producto(id=None, nombre=None, valor=None):
    productos.append({"Id":id, "Nombre" : nombre, "valor" : valor})
    return "200"


# exponer un serviio DELETE /producto/{id}, eliminar un elemento de la lista
# impl opentelemetry
@app.route('/producto/<id>', methods=['DELETE'])
def delete_producto(id=None):
    productos.remove(productos[int(id)])
    return "200"
