from controladores.controlador_usuarios import ControladorUsuarios

def main():
    controlador_usuarios = ControladorUsuarios()

    while True:
        print("\n1. Crear Usuario")
        print("2. Ver Todos los Usuarios")
        print("3. Ver Usuario por ID")
        print("4. Actualizar Usuario")
        print("5. Eliminar Usuario")
        print("6. Salir")

        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            respuesta = controlador_usuarios.manejar_peticion("CREAR", {"nombre": nombre, "correo": correo})
            print(respuesta)
        elif opcion == "2":
            respuesta = controlador_usuarios.manejar_peticion("LEER_TODOS")
            print(respuesta)
        elif opcion == "3":
            id_usuario = int(input("ID del Usuario: "))
            respuesta = controlador_usuarios.manejar_peticion("LEER_UNO", {"id_usuario": id_usuario})
            print(respuesta)
        elif opcion == "4":
            id_usuario = int(input("ID del Usuario: "))
            nombre = input("Nuevo Nombre (dejar vacío si no cambia): ")
            correo = input("Nuevo Correo (dejar vacío si no cambia): ")
            respuesta = controlador_usuarios.manejar_peticion(
                "ACTUALIZAR", {"id_usuario": id_usuario, "nombre": nombre, "correo": correo}
            )
            print(respuesta)
        elif opcion == "5":
            id_usuario = int(input("ID del Usuario: "))
            respuesta = controlador_usuarios.manejar_peticion("ELIMINAR", {"id_usuario": id_usuario})
            print(respuesta)
        elif opcion == "6":
            print("Nos vemos, que tenga buen día, buen hombre")
            break
        else:
            print("Opción no válida. Solo es del 1 al 6")

if __name__ == "__main__":
    main()
