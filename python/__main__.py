

importar lo de opentelemetry;

producto {
    id: int,
    nombre: string,
    valor: float
}

lista


# exponer un servicio GET /, devuelve todos los objetos actuales de la lista
# impl opentelemetry

# exponer un servicio GET /producto/{id}, devuelve el elemento del id
# impl opentelemetry

# exponer un servicio POST /producto, agrega elementos a la lista
# impl opentelemetry

# exponer un serviio DELETE /producto/{id}, eliminar un elemento de la lista
# impl opentelemetry