from flask import request
from flask_restful import Resource
from ..modelos import db, Fecha_Registro_Prod, FechaRegistroSchema

fecha_registro_schema = FechaRegistroSchema()

class VistaFechaRegistro(Resource):
    def get(self):
        return [fecha_registro_schema.dump(Fecha_Registro_Prod) for Fecha_Registro_Prod in Fecha_Registro_Prod.query.all()]
    
    def post(self):
        nueva_fecha_registro = Fecha_Registro_Prod(fecha_registro = request.json['fecha_registro'],
                                                   cantidad = request.json['cantidad'],
                                                   proveedor = request.json['proveedor'],
                                                   producto = request.json['producto'])
        db.session.add(nueva_fecha_registro)
        db.session.commit()
        return fecha_registro_schema.dump(nueva_fecha_registro)

