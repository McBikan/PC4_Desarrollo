class RepositorioProductos:
    def __init__(self):
        self.productos = {}
        self.contador_id = 1

    def crear_producto(self, nombre, precio, usuario_id):
        producto = {
            "id": self.contador_id,
            "nombre": nombre,
            "precio": precio,
            "usuario_id": usuario_id
        }
        self.productos[self.contador_id] = producto
        self.contador_id += 1
        return producto

    def obtener_todos_los_productos(self):
        return list(self.productos.values())

    def obtener_producto_por_id(self, id_producto):
        return self.productos.get(id_producto)

    def actualizar_producto(self, id_producto, nombre=None, precio=None):
        if id_producto in self.productos:
            if nombre:
                self.productos[id_producto]["nombre"] = nombre
            if precio:
                self.productos[id_producto]["precio"] = precio
            return self.productos[id_producto]
        return None

    def eliminar_producto(self, id_producto):
        return self.productos.pop(id_producto, None)
