# 📘 Proyecto final — Gestor de Biblioteca Personal

## 🎯 Objetivo

Construir, paso a paso y transcribiendo el código de esta guía, una aplicación de
consola en Python que gestione tu colección de libros: agregar, listar, buscar,
marcar como prestado/devuelto, eliminar, y que los datos **no se pierdan** al cerrar
el programa.

## 🌍 Contexto

Quieres llevar el control de tu biblioteca personal sin usar una hoja de cálculo.
Necesitas un pequeño programa que recuerde tus libros de una ejecución a otra.

## ✅ Prerrequisitos

Haber cursado las Clases 01 a 06 (variables y tipos, funciones, listas/ordenamiento,
diccionarios, archivos de texto, módulos y manejo de excepciones) y tener
[Visual Studio Code](https://code.visualstudio.com/) con Python instalado.

## 🧱 Resultado final

Una carpeta con tres archivos (`libros.py`, `almacenamiento.py`, `main.py`) que, al
ejecutar `python3 main.py`, muestra un menú en bucle para gestionar tu biblioteca, y
que recuerda tus libros la próxima vez que la abres.

## 📝 Cómo usar esta guía

Cada paso te da el código completo de una parte del programa. **Transcríbelo** (escríbelo
tú mismo, no copies y pegues) en el archivo indicado, en el orden en que aparece dentro
de ese archivo. Cada bloque de código va acompañado de una explicación breve de qué hace
y por qué.

---

## 🪜 Pasos

### Paso 1 — Preparar el proyecto en VS Code

Crea una carpeta `proyecto-biblioteca` y ábrela en Visual Studio Code (`Archivo >
Abrir carpeta`). Dentro, crea tres archivos vacíos: `libros.py`, `almacenamiento.py`
y `main.py`. Usarás la terminal integrada de VS Code (`Ver > Terminal`) para ejecutar
tu programa a medida que avances.

Este es el árbol de archivos con el que vas a terminar (`biblioteca.txt` todavía no
existe en este paso: lo crea el propio programa la primera vez que lo ejecutes, en el
Paso 8):

```text
proyecto-biblioteca/
├── libros.py            # Pasos 2, 3 y 4 - modelo del libro y operaciones sobre la coleccion
├── almacenamiento.py    # Paso 5 - guardar y cargar desde archivo
├── main.py              # Pasos 6 y 7 - menu y punto de entrada
└── biblioteca.txt       # se crea solo, al ejecutar el programa (Paso 8)
```

📖 **Explicación**: cada archivo `.py` es un módulo con una única responsabilidad
(Clase 06): `libros.py` sabe de libros, `almacenamiento.py` sabe de guardar/cargar, y
`main.py` conecta a los otros dos con el menú. `biblioteca.txt` no lo creas tú a mano:
es un archivo de datos que tu programa genera y actualiza solo.

### Paso 2 — Modelar un libro (`libros.py`)

Un libro se representa como un diccionario con cuatro claves. Transcribe esto al
principio de `libros.py`:

```python
"""Modulo con las operaciones sobre la coleccion de libros."""


def crear_libro(titulo, autor, anio):
    """Crea un diccionario que representa un libro."""
    return {
        "titulo": titulo,
        "autor": autor,
        "anio": anio,
        "prestado": False,
    }
```

📖 **Explicación**: `crear_libro` recibe los tres datos que el usuario conoce
(título, autor, año) y arma el diccionario completo, agregando `prestado: False`
porque un libro recién creado nunca empieza prestado. La **colección completa** de
libros será, más adelante, una simple lista de estos diccionarios.

### Paso 3 — Operaciones sobre la colección (`libros.py`)

Debajo de `crear_libro`, agrega estas cuatro funciones:

```python
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
```

📖 **Explicación**: `buscar_libro` recorre la lista comparando títulos en minúsculas
(así "El Hobbit" y "el hobbit" se consideran el mismo libro) y es la función que más
se reutiliza: tanto `eliminar_libro` como `cambiar_prestado` la usan primero para
encontrar el libro, y devuelven `True`/`False` según si lo encontraron. Esto evita
repetir la misma búsqueda en cada función.

### Paso 4 — Ordenar la colección (`libros.py`)

Agrega estas dos funciones al final de `libros.py`:

```python
def ordenar_por_titulo(libros):
    """Devuelve una nueva lista de libros ordenada por titulo."""
    return sorted(libros, key=lambda libro: libro["titulo"].lower())


def ordenar_por_anio(libros):
    """Devuelve una nueva lista de libros ordenada por anio de publicacion."""
    return sorted(libros, key=lambda libro: libro["anio"])
```

📖 **Explicación**: `sorted(..., key=...)` no modifica la lista original: devuelve una
lista **nueva**, ya ordenada. `key=lambda libro: libro["titulo"].lower()` le dice a
`sorted` que compare los libros por su título en minúsculas; `key=lambda libro:
libro["anio"]` los compara por año.

### Paso 5 — Guardar y cargar desde un archivo (`almacenamiento.py`)

Este módulo convierte cada libro en una línea de texto y viceversa. Transcribe todo
esto en `almacenamiento.py`:

```python
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
```

📖 **Explicación**: cada libro se guarda como una línea `titulo|autor|anio|prestado`
(`SEPARADOR = "|"`). Al cargar, `linea.split(SEPARADOR)` deshace esa unión; `int(anio_texto)`
convierte el año de vuelta a número, y `prestado_texto == "si"` convierte el texto
guardado de nuevo a `True`/`False`. El `try`/`except FileNotFoundError` es clave: la
**primera vez** que ejecutes el programa, el archivo todavía no existe, y en vez de
detenerse con un error, `cargar_libros` simplemente devuelve una lista vacía.

### Paso 6 — Construir el menú y sus opciones (`main.py`)

Este archivo conecta los dos módulos anteriores. Transcribe primero el encabezado y
las funciones que atienden cada opción del menú:

```python
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
```

📖 **Explicación**: `import libros as libros_modulo` importa tu primer módulo con un
alias (para no confundirlo con la variable `libros` que usan sus propias funciones);
`import almacenamiento` importa el segundo. Cada `opcion_*` atiende **una** opción del
menú: pide los datos con `input()`, llama a la función correspondiente de
`libros_modulo`, y muestra el resultado. Fíjate que `pedir_anio()` ya trae su propio
`try`/`except ValueError` (Paso 6), y que `opcion_agregar` rechaza un título vacío
antes de seguir — así se manejan dos de los errores de entrada más comunes.

### Paso 7 — La función `main()` (`main.py`)

Al final de `main.py`, después de las funciones del Paso 6, transcribe:

```python
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
```

📖 **Explicación**: `coleccion` se carga **una sola vez**, antes de entrar al bucle
`while True`. En cada vuelta del bucle se muestra el menú, se lee la opción y se
llama a la función correspondiente; la opción `"6"` guarda, se despide, y usa `break`
para salir del bucle. Nota que `guardar_libros` se llama también al final de **cada**
vuelta (no solo al salir): así, si algo interrumpe el programa a mitad de camino, los
cambios ya hechos no se pierden. `if __name__ == "__main__": main()` es lo que hace
que, al ejecutar `python3 main.py`, se llame automáticamente a `main()`.

### Paso 8 — Probar tu programa completo

Guarda los tres archivos y, en la terminal integrada de VS Code, ejecuta:

```bash
python3 main.py
```

Prueba en orden: agregar dos o tres libros, listarlos ordenados por título y por año,
marcar uno como prestado, buscar uno por título, y salir con la opción 6. Vuelve a
ejecutar `python3 main.py`: tus libros —y su estado de préstamo— deben seguir ahí,
porque quedaron guardados en `biblioteca.txt`.

Prueba también que tu programa **no se rompe** ante estos casos (ya están cubiertos
por el código de los Pasos 5 y 6, pero vale la pena confirmarlo):

- Escribir letras donde se espera el año (Paso 6, `pedir_anio`).
- Dejar el título vacío al agregar (Paso 6, `opcion_agregar`).
- Buscar, marcar o eliminar un libro que no existe (Paso 3, `buscar_libro` devuelve
  `None`, y las funciones que dependen de ella responden con un mensaje).
- Listar la biblioteca cuando está vacía (Paso 6, `opcion_listar`).
- Ejecutar el programa por primera vez, sin que `biblioteca.txt` exista todavía
  (Paso 5, `cargar_libros`).

---

## 🏁 Verificación final

Tu proyecto está completo cuando puedes marcar todo esto:

- [ ] El programa se ejecuta con `python3 main.py` sin errores.
- [ ] Puedes agregar, listar (ordenado por título y por año), buscar, marcar
      prestado/devuelto y eliminar un libro desde el menú.
- [ ] Si cierras el programa (opción Salir) y lo vuelves a abrir, tus libros —y su
      estado de préstamo— siguen ahí.
- [ ] Si el archivo de datos no existe (primera vez), el programa inicia sin fallar.
- [ ] Ingresar un año inválido, buscar un título inexistente, o listar con la
      biblioteca vacía, muestra un mensaje claro y el programa sigue funcionando.

Si algo no funciona, revisa primero las funciones de `libros.py` de forma aislada
antes de sospechar del menú.
