from repositorios.repositorio_usuarios import RepositorioUsuarios

class ServicioUsuarios:
    def __init__(self):
        self.repositorio_usuarios = RepositorioUsuarios()

    def crear_usuario(self, nombre, correo):
        return self.repositorio_usuarios.crear_usuario(nombre, correo)

    def obtener_todos_los_usuarios(self):
        return self.repositorio_usuarios.obtener_todos_los_usuarios()

    def obtener_usuario(self, id_usuario):
        return self.repositorio_usuarios.obtener_usuario_por_id(id_usuario)

    def actualizar_usuario(self, id_usuario, nombre=None, correo=None):
        return self.repositorio_usuarios.actualizar_usuario(id_usuario, nombre, correo)

    def eliminar_usuario(self, id_usuario):
        return self.repositorio_usuarios.eliminar_usuario(id_usuario)
