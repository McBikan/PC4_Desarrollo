class RepositorioUsuarios:
    def __init__(self):
        self.usuarios = {}
        self.contador_id = 1

    def crear_usuario(self, nombre, correo):
        usuario = {"id": self.contador_id, "nombre": nombre, "correo": correo}
        self.usuarios[self.contador_id] = usuario
        self.contador_id += 1
        return usuario

    def obtener_todos_los_usuarios(self):
        return list(self.usuarios.values())

    def obtener_usuario_por_id(self, id_usuario):
        return self.usuarios.get(id_usuario)

    def actualizar_usuario(self, id_usuario, nombre=None, correo=None):
        if id_usuario in self.usuarios:
            if nombre:
                self.usuarios[id_usuario]["nombre"] = nombre
            if correo:
                self.usuarios[id_usuario]["correo"] = correo
            return self.usuarios[id_usuario]
        return None

    def eliminar_usuario(self, id_usuario):
        return self.usuarios.pop(id_usuario, None)
