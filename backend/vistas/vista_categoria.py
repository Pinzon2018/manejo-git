from flask import request
from flask_restful import Resource
from ..modelos import db, Categoria, CategoriaSchema

categoria_schema = CategoriaSchema()

#Vista para ver y agregar Categorias

class VistaCategoria(Resource):
    def get(self):
        return [categoria_schema.dump(Categoria) for Categoria in Categoria.query.all()]

    def post(self):
        nueva_categoria = Categoria(nombre_categoria = request.json['nombre_categoria'],
                                    descripcion_categoria = request.json['descripcion_categoria'])
        db.session.add(nueva_categoria)
        db.session.commit()
        return categoria_schema.dump(nueva_categoria)

#Vista para editar y eliminar Categorias
    
class VistaCategoriaed(Resource):
    def put(self, id):
        categoria = Categoria.query.get(id)
        if not categoria:
            return 'Categoria no encontrada', 404
        
        categoria.nombre_categoria = request.json.get('nombre_categoria', categoria.nombre_categoria)
        categoria.descripcion_categoria = request.json.get('descripcion_categoria', categoria.descripcion_categoria)
        
        db.session.commit()
        return categoria_schema.dump(categoria), 200

    def delete(self, id):
        categoria = Categoria.query.get(id)
        if not categoria:
            return 'Categoria no encontrada', 404

        db.session.delete(categoria)
        db.session.commit()
        return 'Categoria Eliminada'
