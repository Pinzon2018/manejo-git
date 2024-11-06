from flask import request
from flask_restful import Resource
from ..modelos import db, Proveedor, ProveedorSchema

proveedor_schema = ProveedorSchema()

#Vista para ver y agregar Proveedores

class VistaProveedor(Resource):
    def get(self):
        return [proveedor_schema.dump(Proveedor) for Proveedor in Proveedor.query.all()]

    def post(self):
        nuevo_proveedor = Proveedor(nombre_proveedor=request.json['nombre_proveedor'],
                                    telefono_proveedor = request.json['telefono_proveedor'],
                                    direccion_proveedor = request.json['direccion_proveedor'])
        db.session.add(nuevo_proveedor)
        db.session.commit()
        return proveedor_schema.dump(nuevo_proveedor)