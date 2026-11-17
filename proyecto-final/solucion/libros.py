"""Modulo con las operaciones sobre la coleccion de libros."""


def crear_libro(titulo, autor, anio):
    """Crea un diccionario que representa un libro."""
    return {
        "titulo": titulo,
        "autor": autor,
        "anio": anio,
        "prestado": False,
    }


def agregar_libro(libros, libro):
    """Agrega un libro al final de la lista de libros."""
    libros.append(libro)


def buscar_libro(libros, titulo):
    """Busca un libro por titulo (sin distinguir mayusculas).

    Devuelve el diccionario del libro, o None si no se encuentra.
    """
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            return libro
    return None


def eliminar_libro(libros, titulo):
    """Elimina el primer libro que coincida con el titulo dado.

    Devuelve True si elimino algo, False si no lo encontro.
    """
    libro = buscar_libro(libros, titulo)
    if libro is None:
        return False
    libros.remove(libro)
    return True


def cambiar_prestado(libros, titulo, prestado):
    """Marca un libro como prestado (True) o devuelto (False).

    Devuelve True si encontro el libro, False si no.
    """
    libro = buscar_libro(libros, titulo)
    if libro is None:
        return False
    libro["prestado"] = prestado
    return True


def ordenar_por_titulo(libros):
    """Devuelve una nueva lista de libros ordenada por titulo."""
    return sorted(libros, key=lambda libro: libro["titulo"].lower())


def ordenar_por_anio(libros):
    """Devuelve una nueva lista de libros ordenada por anio de publicacion."""
    return sorted(libros, key=lambda libro: libro["anio"])
