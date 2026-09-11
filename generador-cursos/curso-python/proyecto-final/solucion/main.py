"""Punto de entrada del Gestor de Biblioteca Personal."""
import libros as libros_modulo
import almacenamiento

ARCHIVO_DATOS = "biblioteca.txt"


def mostrar_menu():
    print("\n=== Gestor de Biblioteca Personal ===")
    print("1. Agregar libro")
    print("2. Listar libros")
    print("3. Buscar libro")
    print("4. Marcar prestado / devuelto")
    print("5. Eliminar libro")
    print("6. Salir")


def pedir_anio():
    """Pide el anio de publicacion hasta recibir un numero valido."""
    while True:
        try:
            return int(input("Anio de publicacion: "))
        except ValueError:
            print("El anio debe ser un numero. Intenta de nuevo.")


def opcion_agregar(coleccion):
    titulo = input("Titulo: ").strip()
    if not titulo:
        print("El titulo no puede estar vacio.")
        return
    autor = input("Autor: ").strip()
    anio = pedir_anio()
    libro = libros_modulo.crear_libro(titulo, autor, anio)
    libros_modulo.agregar_libro(coleccion, libro)
    print(f"Libro '{titulo}' agregado.")


def opcion_listar(coleccion):
    if not coleccion:
        print("No hay libros registrados todavia.")
        return
    print("Ordenar por: 1) Titulo  2) Anio")
    opcion = input("Elige una opcion: ").strip()
    if opcion == "2":
        lista_ordenada = libros_modulo.ordenar_por_anio(coleccion)
    else:
        lista_ordenada = libros_modulo.ordenar_por_titulo(coleccion)
    for libro in lista_ordenada:
        estado = "prestado" if libro["prestado"] else "disponible"
        print(f"- {libro['titulo']} ({libro['anio']}) de {libro['autor']} [{estado}]")


def opcion_buscar(coleccion):
    titulo = input("Titulo a buscar: ").strip()
    libro = libros_modulo.buscar_libro(coleccion, titulo)
    if libro is None:
        print(f"No se encontro ningun libro con el titulo '{titulo}'.")
    else:
        estado = "prestado" if libro["prestado"] else "disponible"
        print(f"{libro['titulo']} ({libro['anio']}) de {libro['autor']} [{estado}]")


def opcion_prestamo(coleccion):
    titulo = input("Titulo del libro: ").strip()
    respuesta = input("Marcar como prestado? (s/n): ").strip().lower()
    prestado = respuesta == "s"
    encontrado = libros_modulo.cambiar_prestado(coleccion, titulo, prestado)
    if encontrado:
        estado = "prestado" if prestado else "disponible"
        print(f"'{titulo}' ahora esta {estado}.")
    else:
        print(f"No se encontro ningun libro con el titulo '{titulo}'.")


def opcion_eliminar(coleccion):
    titulo = input("Titulo del libro a eliminar: ").strip()
    eliminado = libros_modulo.eliminar_libro(coleccion, titulo)
    if eliminado:
        print(f"Libro '{titulo}' eliminado.")
    else:
        print(f"No se encontro ningun libro con el titulo '{titulo}'.")


def main():
    coleccion = almacenamiento.cargar_libros(ARCHIVO_DATOS)

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            opcion_agregar(coleccion)
        elif opcion == "2":
            opcion_listar(coleccion)
        elif opcion == "3":
            opcion_buscar(coleccion)
        elif opcion == "4":
            opcion_prestamo(coleccion)
        elif opcion == "5":
            opcion_eliminar(coleccion)
        elif opcion == "6":
            almacenamiento.guardar_libros(ARCHIVO_DATOS, coleccion)
            print("Datos guardados. Hasta pronto!")
            break
        else:
            print("Opcion invalida, intenta de nuevo.")

        # Se guarda tambien despues de cada operacion que modifica la
        # coleccion, no solo al salir, para minimizar la perdida de datos.
        almacenamiento.guardar_libros(ARCHIVO_DATOS, coleccion)


if __name__ == "__main__":
    main()
