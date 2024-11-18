from flask import request
from datetime import datetime
from flask_restful import Resource
from ..modelos import db, Usuario, UsuarioSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token

usuario_schema = UsuarioSchema()

#Vista para ver y agregar usuarios

class VistaUsuario(Resource):
    @jwt_required()
    def get(self):
        return [usuario_schema.dump(Usuario) for Usuario in Usuario.query.all()]

    def post(self):
        fecha = request.json['fecha_inicio_contrato']
        fecha_inicio_contrato = datetime.strptime(fecha, "%Y-%m-%d").date()
        nuevo_usuario = Usuario(nombre_usu = request.json ['nombre_usu'],   
                                email_usu = request.json['email_usu'],    
                                telefono_usu = request.json['telefono_usu'],
                                fecha_inicio_contrato = fecha_inicio_contrato,
                                cedula_usu = request.json['cedula_usu'],
                                rol = request.json['rol'])
        nuevo_usuario.contrasena = request.json['contrasena_usu'] 
        db.session.add(nuevo_usuario)
        db.session.commit()

        token_de_acceso = create_access_token(identity=nuevo_usuario.nombre_usu)

        return  {'Mensaje': 'Usuario creado exitosamente',
                 'Usuario': usuario_schema.dump(nuevo_usuario),
                 'Token de acceso': token_de_acceso
                 }
    
#Vista para editar y eliminar usuarios

class VistaUsuarioed(Resource):
    def put(self, id):
        usuario = Usuario.query.get(id)
        if not usuario:
            return 'Usuario no encontrado', 404
        
        usuario.nombre_usu = request.json.get('nombre_usu', usuario.nombre_usu)
        usuario.contrasena_usu = request.json.get('contrasena_usu', usuario.contrasena_usu)
        usuario.email_usu = request.json.get('email_usu', usuario.email_usu)
        usuario.telefono_usu = request.json.get('telefono_usu', usuario.telefono_usu)
        if 'fecha_inicio_contrato' in request.json:
            fecha = request.json['fecha_inicio_contrato']
            usuario.fecha_inicio_contrato = datetime.strptime(fecha, "%Y-%m-%d").date()
        usuario.cedula_usu = request.json.get('cedula_usu', usuario.cedula_usu)
        usuario.rol = request.json.get('rol', usuario.rol)

    def delete(self, id):
        usuario = Usuario.query.get(id)
        if not usuario:
            return 'Usuario no encontrado', 404
        
        db.session.delete(usuario)
        db.session.commit()
        return 'Usuario eliminado'
    
class VistaLogIn(Resource):
    def post(self):
        nombre = request.json["nombre_usu"]
        contrasena = request.json["contrasena_usu"]
        usuario = Usuario.query.filter_by(nombre_usu=nombre).first()
        if usuario and usuario.verificar_contrasena(contrasena):
            return {'Mensaje': 'Inicio de sesión exitoso'}
        else:
            return {'Mensaje': 'Nombre de usuario o contraseña incorrectos'}

