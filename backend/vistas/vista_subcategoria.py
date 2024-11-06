from flask import request
from flask_restful import Resource
from ..modelos import db, Subcategoria, SubcategoriaSchema

subcategoria_schema = SubcategoriaSchema()

#Vista para ver y agregar Subcategorias

class VistaSubcategoria(Resource):
    def get(self):
        return [subcategoria_schema.dump(Subcategoria) for Subcategoria in Subcategoria.query.all()]
    
    def post(self):
        nueva_subcategoria = Subcategoria(nombre_subca = request.json['nombre_subca'],
                                          descripcion_subca = request.json['descripcion_subca'],
                                          categoria = request.json['categoria'])
        db.session.add(nueva_subcategoria)
        db.session.commit()
        return subcategoria_schema.dump(nueva_subcategoria)
    
#Vista para editar y eliminar Subcategorias

class VistaSubcategoriaed(Resource):
    def put(self, id):
        subcategoria = Subcategoria.query.get(id)
        if not subcategoria:
            return 'Subcategoria no encontrada'
        
        subcategoria.nombre_subca = request.json.get('nombre_subca', subcategoria.nombre_subca)
        subcategoria.descripcion_subca = request.json.get('descripcion_subca', subcategoria.descripcion_subca)
        subcategoria.categoria = request.json.get('categoria', subcategoria.categoria)

        db.session.commit()
        return subcategoria_schema.dump(subcategoria), 200

    def delete(self, id):
        subcategoria = Subcategoria.query.get(id)
        if not subcategoria:
            return 'Subcategoria no encontrada'
        
        db.session.delete(subcategoria)
        db.session.commit()
        return 'Subcategoria Eliminada'