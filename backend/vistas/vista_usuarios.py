from flask import request
from flask_restful import Resource
from ..modelos import db, Usuario, UsuarioSchema

usuario_schema = UsuarioSchema()

#Vista para ver y agregar usuarios

class VistaUsuario(Resource):
    def get(self):
        return [usuario_schema.dump(Usuario) for Usuario in Usuario.query.all()]

    def post(self):
        nuevo_usuario = Usuario(nombre_usu = request.json ['nombre_usu'],
                                contrasena_usu = request.json['contrasena_usu'],    
                                email_usu = request.json['email_usu'],    
                                telefono_usu = request.json['telefono_usu'],
                                fecha_inicio_contrato = request.json['fecha_inicio_contrato'],
                                cedula_usu = request.json['cedula_usu'],
                                rol = request.json['rol'])
        db.session.add(nuevo_usuario)
        db.session.commit()
        return usuario_schema.dump(nuevo_usuario)