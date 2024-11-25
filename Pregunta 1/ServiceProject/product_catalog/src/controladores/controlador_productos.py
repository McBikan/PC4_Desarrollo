from servicios.servicio_productos import ServicioProductos

class ControladorProductos:
    def __init__(self):
        self.servicio_productos = ServicioProductos()

    def manejar_peticion(self, accion, parametros=None):
        if accion == "CREAR":
            return self.servicio_productos.crear_producto(
                parametros["nombre"], parametros["precio"], parametros["usuario_id"]
            )
        elif accion == "LEER_TODOS":
            return self.servicio_productos.obtener_todos_los_productos()
        elif accion == "LEER_UNO":
            return self.servicio_productos.obtener_producto(parametros["id_producto"])
        elif accion == "ACTUALIZAR":
            return self.servicio_productos.actualizar_producto(
                parametros["id_producto"], parametros.get("nombre"), parametros.get("precio")
            )
        elif accion == "ELIMINAR":
            return self.servicio_productos.eliminar_producto(parametros["id_producto"])
        else:
            return {"error": "Acción no válida"}
