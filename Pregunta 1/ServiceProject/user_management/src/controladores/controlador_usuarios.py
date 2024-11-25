from servicios.servicio_usuarios import ServicioUsuarios

class ControladorUsuarios:
    def __init__(self):
        self.servicio_usuarios = ServicioUsuarios()

    def manejar_peticion(self, accion, parametros=None):
        if accion == "CREAR":
            return self.servicio_usuarios.crear_usuario(parametros["nombre"], parametros["correo"])
        elif accion == "LEER_TODOS":
            return self.servicio_usuarios.obtener_todos_los_usuarios()
        elif accion == "LEER_UNO":
            return self.servicio_usuarios.obtener_usuario(parametros["id_usuario"])
        elif accion == "ACTUALIZAR":
            return self.servicio_usuarios.actualizar_usuario(
                parametros["id_usuario"], parametros.get("nombre"), parametros.get("correo")
            )
        elif accion == "ELIMINAR":
            return self.servicio_usuarios.eliminar_usuario(parametros["id_usuario"])
        else:
            return {"error": "Acción no válida"}
