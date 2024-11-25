from controladores.controlador_productos import ControladorProductos

def main():
    controlador_productos = ControladorProductos()

    while True:
        print("\n1. Crear Producto")
        print("2. Ver Todos los Productos")
        print("3. Ver Producto por ID")
        print("4. Actualizar Producto")
        print("5. Eliminar Producto")
        print("6. Salir")

        opcion = input("\nElige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del Producto: ")
            precio = float(input("Precio: "))
            usuario_id = int(input("ID del Usuario: "))
            try:
                respuesta = controlador_productos.manejar_peticion(
                    "CREAR", {"nombre": nombre, "precio": precio, "usuario_id": usuario_id}
                )
                print(respuesta)
            except ValueError as e:
                print(e)
        elif opcion == "2":
            respuesta = controlador_productos.manejar_peticion("LEER_TODOS")
            print(respuesta)
        elif opcion == "3":
            id_producto = int(input("ID del Producto: "))
            respuesta = controlador_productos.manejar_peticion("LEER_UNO", {"id_producto": id_producto})
            print(respuesta)
        elif opcion == "4":
            id_producto = int(input("ID del Producto: "))
            nombre = input("Nuevo Nombre (dejar vacío si no cambia): ")
            precio = input("Nuevo Precio (dejar vacío si no cambia): ")
            respuesta = controlador_productos.manejar_peticion(
                "ACTUALIZAR", {"id_producto": id_producto, "nombre": nombre, "precio": float(precio) if precio else None}
            )
            print(respuesta)
        elif opcion == "5":
            id_producto = int(input("ID del Producto: "))
            respuesta = controlador_productos.manejar_peticion("ELIMINAR", {"id_producto": id_producto})
            print(respuesta)
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Solo es del 1 al 6")

if __name__ == "__main__":
    main()
