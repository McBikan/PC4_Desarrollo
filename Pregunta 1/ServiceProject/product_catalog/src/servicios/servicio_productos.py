from repositorios.repositorio_productos import RepositorioProductos
from integraciones.servicio_gestion_usuarios import ServicioGestionUsuarios

class ServicioProductos:
    def __init__(self):
        self.repositorio_productos = RepositorioProductos()
        self.servicio_gestion_usuarios = ServicioGestionUsuarios()

    def crear_producto(self, nombre, precio, usuario_id):
        # Validamos que el usuario exista
        if not self.servicio_gestion_usuarios.validar_usuario(usuario_id):
            raise ValueError("El usuario no existe.")
        return self.repositorio_productos.crear_producto(nombre, precio, usuario_id)

    def obtener_todos_los_productos(self):
        return self.repositorio_productos.obtener_todos_los_productos()

    def obtener_producto(self, id_producto):
        return self.repositorio_productos.obtener_producto_por_id(id_producto)

    def actualizar_producto(self, id_producto, nombre=None, precio=None):
        return self.repositorio_productos.actualizar_producto(id_producto, nombre, precio)

    def eliminar_producto(self, id_producto):
        return self.repositorio_productos.eliminar_producto(id_producto)
