from backend import create_app
from backend.modelos.modelos import Proveedor, Categoria, Subcategoria, Producto, Fecha_Registro_Prod, Rol, Usuario, Factura, Venta, Detalle_Venta
from .modelos import db
from flask_restful import Api
from .vistas.vista_proveedor import VistaProveedor, VistaProveedored
from .vistas.vista_categoria import VistaCategoria, VistaCategoriaed
from .vistas.vista_subcategoria import VistaSubcategoria, VistaSubcategoriaed
from .vistas.vista_productos import VistaProducto, VistaProductoed
from .vistas.vista_usuarios import VistaUsuario, VistaUsuarioed
from .vistas.vista_venta import VistaVenta, VistaVentaed

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()