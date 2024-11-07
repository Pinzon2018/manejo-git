from flask import request
from datetime import datetime
from flask_restful import Resource
from ..modelos import db, Venta, VentaSchema

venta_schema = VentaSchema()

#Vista para ver y agregar Ventas

class VistaVenta(Resource):
    def get(self):
       return [venta_schema.dump(Venta) for Venta in Venta.query.all()]

    def post(self):
        fecha = request.json['fecha_venta']
        fecha_venta = datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S").date()
        nueva_venta = Venta(fecha_venta = fecha_venta,
                            total_venta = request.json['total_venta'],
                            forma_pago = request.json['forma_pago'],
                            usuario = request.json['usuario'])
        db.session.add(nueva_venta)
        db.session.commit()
        return venta_schema.dump(nueva_venta)
    
#Vista para editar y eliminar Ventas

class VistaVentaed(Resource):
    def put(self, id):
        venta = Venta.query.get(id)
        
        if 'fecha_venta' in request.json:
            fecha = request.json['fecha_venta']
            venta.fecha_venta = datetime.strptime(fecha, "%Y-%m-%d").date()
        venta.total_venta = request.json.get('total_venta', venta.total_venta)
        venta.forma_pago = request.json.get('forma_pago', venta.forma_pago)
        venta.usuario = request.json.get('usuario', venta.usuario)

        db.session.commit()
        return venta_schema.dump(venta)
    
    def delete(self, id):
        venta = Venta.query.get(id)

        db.session.delete(venta)
        db.session.commit()
        return 'Venta eliminada'   