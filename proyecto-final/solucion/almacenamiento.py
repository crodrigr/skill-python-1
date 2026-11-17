"""Modulo para guardar y cargar la coleccion de libros en un archivo de texto."""

SEPARADOR = "|"


def cargar_libros(ruta):
    """Carga la coleccion de libros desde un archivo de texto.

    Si el archivo no existe todavia (primera ejecucion del programa),
    devuelve una lista vacia en vez de fallar.
    """
    libros = []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                titulo, autor, anio_texto, prestado_texto = linea.split(SEPARADOR)
                libros.append({
                    "titulo": titulo,
                    "autor": autor,
                    "anio": int(anio_texto),
                    "prestado": prestado_texto == "si",
                })
    except FileNotFoundError:
        print("No se encontro un archivo de datos previo; se inicia una biblioteca vacia.")
    return libros


def guardar_libros(ruta, libros):
    """Guarda la coleccion completa de libros en un archivo de texto,
    sobrescribiendo su contenido anterior."""
    with open(ruta, "w", encoding="utf-8") as archivo:
        for libro in libros:
            prestado_texto = "si" if libro["prestado"] else "no"
            archivo.write(
                f"{libro['titulo']}{SEPARADOR}{libro['autor']}"
                f"{SEPARADOR}{libro['anio']}{SEPARADOR}{prestado_texto}\n"
            )
