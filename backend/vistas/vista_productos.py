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

#Vista para editar y eliminar Productos

class VistaProductoed(Resource):
    def put(self, id):
        producto = Producto.query.get(id)
        if not producto:
            return 'Producto no encontrado', 404

        producto.nombre_prod = request.json.get('nombre_prod', producto.nombre_prod)
        producto.medida_prod = request.json.get('medida_prod', producto.medida_prod)
        producto.unidad_medida = request.json.get('unidad_medida', producto.unidad_medida)
        producto.precio_bruto_prod = request.json.get('precio_bruto_prod', producto.precio_bruto_prod)
        producto.iva_prod = request.json.get('iva_prod', producto.iva_prod)
        producto.porcentaje_ganancia = request.json.get('porcentaje_ganancia', producto.porcentaje_ganancia)
        producto.precio_neto_unidad_prod = request.json.get('precio_neto_unidad_prod', producto.precio_neto_unidad_prod)
        producto.unidades_totales = request.json.get('unidades_totales', producto.unidades_totales)
        producto.marca_prod = request.json.get('marca_prod', producto.marca_prod)
        producto.estado_prod = request.json.get('estado_prod', producto.estado_prod)
        producto.proveedor = request.json.get('proveedor', producto.proveedor)
        producto.subcategoria = request.json.get('subcategoria', producto.subcategoria)

        db.session.commit()
        return producto_schema.dump(producto), 202

    def delete(self, id):
        producto = Producto.query.get(id)
        if not producto:
            return 'producto no encontrado', 404
        
        db.session.delete(producto)
        db.session.commit()
        return 'Producto eliminado', 204