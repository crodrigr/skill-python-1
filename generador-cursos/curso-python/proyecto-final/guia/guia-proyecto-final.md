# 📘 Proyecto final — Gestor de Biblioteca Personal

## 🎯 Objetivo

Construir, paso a paso y con tus propias manos, una aplicación de consola en Python
que gestione tu colección de libros: agregar, listar, buscar, marcar como
prestado/devuelto, eliminar, y que los datos **no se pierdan** al cerrar el programa.

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

---

## 🪜 Pasos

### Paso 1 — Preparar el proyecto en VS Code

Crea una carpeta `proyecto-biblioteca` y ábrela en Visual Studio Code (`Archivo >
Abrir carpeta`). Dentro, crea tres archivos vacíos: `libros.py`, `almacenamiento.py`
y `main.py`. Usarás la terminal integrada de VS Code (`Ver > Terminal`) para ejecutar
tu programa a medida que avances.

### Paso 2 — Modelar un libro

En `libros.py`, decide cómo vas a representar **un** libro. Usa un diccionario con las
claves `titulo`, `autor`, `anio` y `prestado` (este último, `True`/`False`). Escribe
una función que reciba título, autor y año, y devuelva ese diccionario ya armado
(con `prestado` iniciando en `False`).

```python
def crear_libro(titulo, autor, anio):
    # arma y devuelve el diccionario del libro
    ...
```

La **colección completa** de libros será una simple lista de estos diccionarios.

### Paso 3 — Operaciones sobre la colección

Sigue en `libros.py`. Escribe funciones que reciban la lista de libros y hagan una
operación cada una:

- `agregar_libro(libros, libro)`: agrega un libro a la lista.
- `buscar_libro(libros, titulo)`: recorre la lista y devuelve el libro cuyo título
  coincide (ignorando mayúsculas/minúsculas), o `None` si no lo encuentra.
- `eliminar_libro(libros, titulo)`: usa `buscar_libro` para encontrarlo y quitarlo de
  la lista; devuelve `True`/`False` según si lo encontró.
- `cambiar_prestado(libros, titulo, prestado)`: busca el libro y cambia su clave
  `prestado`; devuelve `True`/`False` según si lo encontró.

💡 Pista: `buscar_libro` es la función que más vas a reutilizar; escríbela primero y
pruébala antes de seguir.

### Paso 4 — Ordenar la colección

Todavía en `libros.py`, escribe `ordenar_por_titulo(libros)` y `ordenar_por_anio(libros)`,
cada una devolviendo una **nueva** lista ordenada (no modifiques la original). Revisa
en tus apuntes de la Clase 03 la función `sorted()` y su parámetro `key`.

### Paso 5 — Guardar y cargar desde un archivo

En `almacenamiento.py`, decide un formato simple para guardar cada libro como una
línea de texto (por ejemplo, separando los datos con `|`). Escribe dos funciones:

- `guardar_libros(ruta, libros)`: abre el archivo en modo escritura y escribe una
  línea por libro.
- `cargar_libros(ruta)`: abre el archivo en modo lectura, lo recorre línea por línea,
  y reconstruye la lista de diccionarios. Debe manejar con `try`/`except` el caso de
  que el archivo **todavía no exista** (primera vez que se usa el programa), devolviendo
  una lista vacía en ese caso.

💡 Pista: recuerda `strip()` para quitar el salto de línea, y `split("|")` para separar
los datos de cada línea (Clase 05); recuerda `FileNotFoundError` (Clase 06).

### Paso 6 — Construir el menú

En `main.py`, importa tus dos módulos. Escribe una función `main()` con un bucle
`while True` que:

1. Muestre las opciones (Agregar, Listar, Buscar, Marcar prestado/devuelto, Eliminar,
   Salir).
2. Lea la opción elegida.
3. Según la opción, llame a la función correspondiente (puedes escribir una función
   auxiliar por cada opción, por ejemplo `opcion_agregar(coleccion)`).
4. Al elegir Salir, guarde los datos y termine el bucle con `break`.

### Paso 7 — Conectar todo

Al iniciar `main()`, carga la colección con `almacenamiento.cargar_libros(...)` antes
de entrar al bucle. Después de cada operación que modifique la colección (agregar,
eliminar, marcar prestado), guarda de nuevo con `almacenamiento.guardar_libros(...)`
— no esperes solo a la opción "Salir", así minimizas la pérdida de datos si algo
interrumpe el programa.

### Paso 8 — Manejar los errores de entrada

Revisa estos casos y decide cómo tu programa debe responder a cada uno **sin
detenerse**:

- El usuario escribe letras donde se espera el año → captura `ValueError` al hacer
  `int(...)` y vuelve a pedir el dato.
- El usuario deja el título vacío al agregar → muestra un mensaje y no agregues nada.
- Se busca, elimina o marca un libro que no existe → muestra un mensaje claro (ya
  deberías tenerlo cubierto si tus funciones del Paso 3 devuelven `None`/`False`
  cuando no encuentran el libro).
- Se lista la biblioteca cuando está vacía → muestra un mensaje en vez de no mostrar
  nada.

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
