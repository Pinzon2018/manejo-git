from flask import request
from flask_restful import Resource
from ..modelos import db, Producto, ProductoSchema

producto_schema = ProductoSchema()

#Vista para ver y agregar Productos

class VistaProducto(Resource):
    def get(self): 
        return [producto_schema.dump(Producto) for Producto in Producto.query.all()]

    def post(self):
        nuevo_producto = Producto(nombre_prod = request.json['nombre_prod'],
                                  medida_prod = request.json['medida_prod'],
                                  unidad_medida = request.json['unidad_medida'],
                                  precio_bruto_prod = request.json['precio_bruto_unidad'],
                                  iva_prod = request.json['iva_prod'],
                                  porcentaje_ganancia = request.json['porcentaje_ganancia'],
                                  precio_neto_unidad_prod = request.json['precio_neto_unidad_prod'],
                                  unidades_totales = request.json['unidades_totales'],
                                  marca_prod = request.json['marca_prod'],
                                  estado_prod = request.json['estado_prod'],
                                  proveedor = request.json['proveedor'],
                                  subcategoria = request.json['subcategoria'])
        db.session.add(nuevo_producto)
        db.session.commit()
        return producto_schema.dump(nuevo_producto)