from backend import create_app
from backend.modelos.modelos import Proveedor, Categoria, Subcategoria, Producto, Fecha_Registro_Prod, Rol, Usuario, Factura, Venta, Detalle_Venta
from .modelos import db
from flask_restful import Api
from .vistas.vista_proveedor import VistaProveedor, VistaProveedored
from .vistas.vista_categoria import VistaCategoria, VistaCategoriaed
from .vistas.vista_subcategoria import VistaSubcategoria, VistaSubcategoriaed
from .vistas.vista_productos import VistaProducto, VistaProductoed
from .vistas.vista_usuarios import VistaUsuario, VistaUsuarioed, VistaLogIn
from .vistas.vista_venta import VistaVenta, VistaVentaed

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

api = Api(app)

#Ruta para ver e insertar proveedores
api.add_resource(VistaProveedor, '/proveedor')
#Ruta para editar y eliminar proveedores
api.add_resource(VistaProveedored, '/proveedor/<int:id>')

api.add_resource(VistaCategoria, '/categorias')
api.add_resource(VistaCategoriaed, '/categorias/<int:id>')

api.add_resource(VistaSubcategoria, '/subcategorias')
api.add_resource(VistaSubcategoriaed, '/subcategorias/<int:id>')

api.add_resource(VistaProducto, '/productos')
api.add_resource(VistaProductoed, '/productos/<int:id>')

api.add_resource(VistaUsuario, '/usuarios')
api.add_resource(VistaUsuarioed, '/usuarios/<int:id>')
api.add_resource(VistaLogIn, '/login')

api.add_resource(VistaVenta, '/ventas')
api.add_resource(VistaVentaed, '/ventas/<int:id>')