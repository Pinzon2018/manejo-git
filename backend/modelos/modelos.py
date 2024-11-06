from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy
import enum

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre_proveedor = db.Column(db.String(50))
    telefono_proveedor = db.Column(db.String(50))
    direccion_proveedor = db.Column(db.String(60))

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre_categoria = db.Column(db.String(150))
    descripcion_categoria = db.Column(db.String(150))

class Subcategoria(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre_subca = db.Column(db.String(50))
    descripcion_subca = db.Column(db.String(150))
    categoria = db.Column(db.Integer, db.ForeignKey("categoria.id"))

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre_prod = db.Column(db.String(100))
    medida_prod = db.Column(db.Integer)
    unidad_medida = db.Column(db.String(50))
    precio_bruto_prod = db.Column(db.Numeric(19, 0))
    iva_prod = db.Column(db.Numeric(3, 2))
    porcentaje_ganancia = db.Column(db.Numeric(3, 2))
    precio_neto_unidad_prod = db.Column(db.Numeric(19, 2))
    unidades_totales = db.Column(db.Integer)
    marca_prod = db.Column(db.String(60))
    estado_prod = db.Column(db.String(50))
    proveedor = db.Column(db.Integer, db.ForeignKey("proveedor.id"))
    subcategoria = db.Column(db.Integer, db.ForeignKey("subcategoria.id"))

class Fecha_Registro_Prod(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fecha_registro = db.Column(db.Date)
    cantidad = db.Column(db.Integer)
    proveedor = db.Column(db.Integer, db.ForeignKey("proveedor.id"))
    producto = db.Column(db.Integer, db.ForeignKey("producto.id"))

# class Rol(enum.Enum):
#     Administrador = 1
#     Empleado = 2

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre_rol = db.Column(db.String(50))

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre_usu = db.Column(db.String(50))
    contrasena_usu = db.Column(db.String(255))
    email_usu = db.Column(db.String(60))
    telefono_usu = db.Column(db.String(50))
    fecha_inicio_contrato = db.Column(db.Date)
    cedula_usu = db.Column(db.String(30))
    rol = db.Column(db.Integer, db.ForeignKey("rol.id"))

class Factura(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    impuestos_fact = db.Column(db.Numeric(5, 2))
    fecha_generacion_fact = db.Column(db.DateTime)

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fecha_venta = db.Column(db.DateTime)
    total_venta = db.Column(db.Numeric(19, 0))
    forma_pago = db.Column(db.String(50))
    usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"))

class Detalle_Venta(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cantidad = db.Column(db.Integer)
    precio_unidad = db.Column(db.Numeric(19, 0))
    venta = db.Column(db.Integer, db.ForeignKey("venta.id"))
    factura = db.Column(db.Integer, db.ForeignKey("factura.id"))
    producto = db.Column(db.Integer, db.ForeignKey("producto.id"))

#Schemas para la base de datos

class ProveedorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Proveedor
        include_relationships = True
        load_instance = True

class CategoriaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Categoria
        include_relationships = True
        load_instance = True

class SubcategoriaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Subcategoria
        include_relationships = True
        load_instance = True

class ProductoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Producto
        include_relationships = True
        load_instance = True

class FechaRegistroSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Fecha_Registro_Prod
        include_relationships = True
        load_instance = True

class RolSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Rol
        include_relationships = True
        load_instance = True

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True

class FacturaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Factura
        include_relationships = True
        load_instance = True
    
class VentaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Venta
        include_relatioships = True
        load_instance = True

class DetalleVentaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Detalle_Venta
        include_relationships = True
        load_instance = True