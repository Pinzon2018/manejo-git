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

class VistaFechaRegistroed(Resource):
    def get(self, id):
        return fecha_registro_schema.dump(Fecha_Registro_Prod.query.get_or_404(id))

    def put(self, id):
        fecha_registro_p = Fecha_Registro_Prod.query.get_or_404(id)
        fecha_registro_p.fecha_registro = request.json.get("fecha_registro", fecha_registro_p.fecha_registro)
        fecha_registro_p.cantidad = request.json.get("cantidad", fecha_registro_p.cantidad)
        fecha_registro_p.proveedor = request.json.get("proveedor", fecha_registro_p.proveedor)
        fecha_registro_p.producto = request.json.get("producto", fecha_registro_p.producto)
        db.session.commit()
        return fecha_registro_schema.dump(fecha_registro_p)
    
    def delete(self, id):
        fecha_registro_p = Fecha_Registro_Prod.query.get_or_404(id)
        db.session.delete(fecha_registro_p)
        db.session.commit()
        return '', 204
