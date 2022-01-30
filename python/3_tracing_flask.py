import flask
import requests
import json
from flask_cors import CORS

## Codigo de la instrumentacion con opentelemetry ###
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({SERVICE_NAME: "my-flask-service"})
    )
)

jaeger_exporter = JaegerExporter(
    agent_host_name="192.168.10.185",
    agent_port=6831,
)


app = flask.Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

tracer = trace.get_tracer(__name__)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)
### Fin codigo instrumentacion ### 

cors = CORS(app)

productos = list()
productos.append({"id":1, "nombre" : "Leche", "valor" : 500})
productos.append({"id":2, "nombre" : "Cafe", "valor" : 600})
productos.append({"id":3, "nombre" : "Azucar", "valor" : 300})
productos.append({"id":4, "nombre" : "Arroz", "valor" : 400})

'''
@app.route("/")
def hello():
    with tracer.start_as_current_span("example-request"):
        requests.get("http://www.example.com")
    return "hello"
'''

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
