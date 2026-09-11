# 📚 Explicación conceptual — Clase 05: Archivos de texto

Este documento desarrolla, en orden pedagógico, los siete bloques temáticos de la clase.
Cada bloque sigue la secuencia **Contexto → Concepto → Explicación**. El lenguaje es
deliberadamente sencillo y solo supone lo visto en las Clases 01, 02, 03 y 04
(variables, tipos de datos básicos, operadores, condicionales, bucles, funciones,
listas, tuplas, conjuntos y diccionarios).

Convención de código: los nombres de variables, archivos y funciones, y los comentarios
están en español; solo las palabras reservadas de Python (`open`, `with`, `as`, `try`,
`except`, `for`, …) están en inglés porque forman parte del lenguaje.

---

## 1️⃣ Introducción a los archivos de texto

**Resultado de aprendizaje**: RA-1.

### 🌍 Contexto

Hasta ahora, todos los datos de un programa —variables, listas, diccionarios— viven
solo mientras el programa se está ejecutando: al terminar el programa, desaparecen de
la memoria. Si un programa calcula un reporte y lo único que hace es mostrarlo con
`print`, esa información se pierde en cuanto se cierra la terminal.

### 🧠 Concepto

Un **archivo de texto** es un recurso guardado en el disco (fuera del programa) que
contiene datos como texto plano. A diferencia de una variable, un archivo **persiste**:
sigue existiendo después de que el programa termina, y puede volver a abrirse más
tarde, incluso por otro programa.

Es la misma idea que una libreta de papel frente a algo que se dice en voz alta: lo que
se dice se pierde apenas se deja de hablar; lo que se anota en la libreta queda
disponible para consultarlo después.

### 📖 Explicación

Python trata un archivo de texto como una secuencia de caracteres organizados en
líneas, cada una terminada por un salto de línea (`\n`). Para trabajar con un archivo,
un programa siempre sigue el mismo ciclo:

```text
abrir el archivo → leer o escribir → cerrar el archivo
```

Ese ciclo —abrir, usar, cerrar— es el que se explica en los siguientes bloques: primero
cómo abrir y cerrar de forma segura, después cómo leer, cómo escribir, cómo procesar el
contenido, y cómo anticipar que el archivo con el que se quiere trabajar podría no
existir.

---

## 2️⃣ Abrir y cerrar archivos

**Resultado de aprendizaje**: RA-2.

### 🌍 Contexto

Antes de leer o escribir un archivo, hay que decirle a Python cuál es (su ruta) y para
qué se va a usar (leer, escribir, o agregar). Eso es "abrir" el archivo. Y cuando ya no
se necesita, hay que "cerrarlo" para que los cambios queden guardados y el recurso
quede libre.

### 🧠 Concepto

Se abre un archivo con `open(ruta, modo)`:

```python
archivo = open("notas.txt", "r")   # abrir para leer ("r" = read)
# ... usar el archivo ...
archivo.close()                     # cerrar explícitamente
```

Los tres modos básicos:

| Modo | Significado | Si el archivo no existe | Si el archivo ya existe |
|------|--------------|---------------------------|----------------------------|
| `'r'` | leer (*read*) | error (`FileNotFoundError`) | lo abre para leer |
| `'w'` | escribir (*write*) | lo crea | lo **sobrescribe** por completo |
| `'a'` | agregar (*append*) | lo crea | agrega al **final**, sin borrar nada |

### 📖 Explicación

**La forma preferida: `with`.** Cerrar un archivo manualmente con `close()` funciona,
pero si ocurre un error entre `open()` y `close()`, el `close()` nunca se ejecuta y el
archivo queda abierto. La sentencia `with` evita ese riesgo: cierra el archivo
automáticamente al salir del bloque, **incluso si ocurre un error dentro**.

```python
with open("notas.txt", "r") as archivo:
    contenido = archivo.read()
    # archivo se cierra automáticamente al salir de este bloque,
    # ocurra o no un error dentro de él

print(contenido)
```

Por eso, en el resto de esta clase, todos los ejemplos abren archivos con `with`. La
variable que sigue a `as` (aquí, `archivo`) solo existe y es válida dentro del bloque
indentado; al salir de él, el archivo ya está cerrado.

---

## 3️⃣ Leer archivos

**Resultado de aprendizaje**: RA-3.

### 🌍 Contexto

Una vez abierto un archivo para lectura, hay más de una forma de obtener su contenido,
según si se necesita todo de una vez, una línea a la vez, o todas las líneas por
separado.

### 🧠 Concepto

```python
with open("notas.txt", "r") as archivo:
    contenido = archivo.read()   # todo el archivo como un solo texto

print(contenido)
```

`read()` devuelve **todo** el contenido del archivo como una sola cadena de texto,
incluidos los saltos de línea.

### 📖 Explicación

**Las tres formas de leer:**

| Método | Qué devuelve |
|--------|---------------|
| `read()` | todo el contenido, como un solo texto |
| `readline()` | una sola línea (la siguiente cada vez que se llama) |
| `readlines()` | una lista, con cada línea del archivo como un elemento |

```python
with open("notas.txt", "r") as archivo:
    lineas = archivo.readlines()

print(lineas)   # ['primera línea\n', 'segunda línea\n', ...]
```

**Recorrer un archivo con `for`.** Un archivo abierto se puede recorrer directamente
con un bucle, línea por línea, sin necesidad de llamar antes a `readlines()`:

```python
with open("notas.txt", "r") as archivo:
    for linea in archivo:
        print(linea)
```

Cualquiera de las tres formas de leer requiere que el archivo exista; si no existe,
Python detiene el programa con `FileNotFoundError` — un caso que se retoma en el bloque
de manejo de errores.

---

## 4️⃣ Escribir archivos

**Resultado de aprendizaje**: RA-4.

### 🌍 Contexto

Guardar información nueva o actualizar un archivo existente son dos necesidades
distintas: a veces se quiere empezar "de cero" (por ejemplo, generar un reporte nuevo
cada vez), y otras veces se quiere conservar lo que ya había y solo sumar algo (por
ejemplo, agregar un registro a un historial).

### 🧠 Concepto

`write()` escribe una cadena de texto en el archivo abierto:

```python
with open("reporte.txt", "w") as archivo:
    archivo.write("Reporte generado\n")
    archivo.write("Total: 1500\n")
```

`writelines()` escribe una lista de cadenas de una sola vez (sin agregar saltos de
línea automáticamente: cada elemento de la lista debe incluir su propio `\n` si se
quiere que quede en líneas separadas):

```python
lineas = ["Reporte generado\n", "Total: 1500\n"]
with open("reporte.txt", "w") as archivo:
    archivo.writelines(lineas)
```

### 📖 Explicación

**El modo decide el efecto, no el método.** `write()` y `writelines()` se comportan
igual sin importar el modo; lo que cambia es **qué le pasó al archivo al abrirlo**:

| Modo | Si el archivo no existía | Si el archivo ya existía |
|------|-----------------------------|------------------------------|
| `'w'` | lo crea vacío y luego escribe | **borra todo su contenido anterior** y escribe desde cero |
| `'a'` | lo crea vacío y luego escribe | **conserva** el contenido anterior; lo nuevo se agrega al final |

```python
with open("historial.txt", "w") as archivo:
    archivo.write("Primer registro\n")

with open("historial.txt", "a") as archivo:
    archivo.write("Segundo registro\n")   # se agrega SIN borrar el primero

with open("historial.txt", "r") as archivo:
    print(archivo.read())
# Primer registro
# Segundo registro
```

Si en el segundo bloque se hubiera usado `'w'` en vez de `'a'`, "Primer registro" se
habría perdido: `'w'` no avisa, simplemente sobrescribe.

---

## 5️⃣ Manipular contenido

**Resultado de aprendizaje**: RA-5.

### 🌍 Contexto

Leer un archivo rara vez es el objetivo final: casi siempre hay que hacer algo con esos
datos —calcular, filtrar, reorganizar— antes de mostrarlos o guardarlos de nuevo. Para
eso hace falta limpiar y separar el texto que se leyó.

### 🧠 Concepto

Cada línea leída con `readlines()` o con un `for` conserva su salto de línea final
(`\n`). Antes de usarla, conviene quitarlo con `strip()`:

```python
linea = "manzana,25\n"
linea_limpia = linea.strip()
print(linea_limpia)   # "manzana,25" (sin el \n)
```

Cuando una línea junta varios valores separados por un carácter (una coma, por
ejemplo), `split(separador)` la divide en una lista de partes:

```python
partes = linea_limpia.split(",")
print(partes)   # ['manzana', '25']
```

### 📖 Explicación

**El patrón completo: limpiar, dividir, usar.**

```python
linea = "manzana,25\n"
nombre, cantidad_texto = linea.strip().split(",")
cantidad = int(cantidad_texto)

print(nombre, "->", cantidad, "unidades")
```

1. `strip()` quita el salto de línea.
2. `split(",")` separa el texto limpio en una lista de dos elementos.
3. El desempaquetado `nombre, cantidad_texto = ...` (visto con tuplas en la Clase 03)
   asigna cada parte a una variable.
4. `int(cantidad_texto)` convierte el texto `"25"` en el número `25`, porque todo lo
   leído de un archivo llega siempre como texto (`str`), aunque parezca un número.

**Guardar el resultado.** Una vez procesados los datos, se vuelven a escribir con
`write()` (visto en el bloque anterior), armando el texto de salida con el formato que
se necesite — por ejemplo, uniendo valores con `str(...)` y separadores propios.

---

## 6️⃣ Manejo de errores

**Resultado de aprendizaje**: RA-6.

### 🌍 Contexto

Hasta ahora, todos los ejemplos abrieron archivos que el propio programa acababa de
crear. En un programa real, un archivo puede no existir todavía (nunca se creó), o
haberse borrado o movido. Si el programa intenta abrirlo para leer sin anticipar esa
posibilidad, se detiene de golpe.

### 🧠 Concepto

Abrir para lectura un archivo que no existe produce un error que detiene el programa:

```python
with open("no_existe.txt", "r") as archivo:
    contenido = archivo.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'no_existe.txt'
```

Una **excepción** es justamente eso: un error que ocurre mientras el programa se está
ejecutando. Python permite **anticiparla** con la estructura `try`/`except`: el código
que podría fallar va dentro de `try`; si ocurre el error indicado, en vez de detener el
programa, se ejecuta el bloque `except`.

```python
try:
    with open("no_existe.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("No se encontró el archivo. Verifica que exista antes de continuar.")
```

### 📖 Explicación

**Cómo se lee un `try`/`except`.** Python ejecuta el bloque `try` de arriba abajo. Si
todas las líneas terminan sin error, el bloque `except` se ignora por completo y el
programa sigue después de él. Si en cambio ocurre el error indicado
(`FileNotFoundError`, en este caso), Python **interrumpe** el bloque `try` en ese punto
y salta directamente al bloque `except`, ejecuta su contenido, y continúa el programa
después de él — sin detenerse con una traza de error.

Este manejo se limita, en esta clase, a `FileNotFoundError` al abrir archivos; Python
tiene muchos otros tipos de excepción (por ejemplo, `ValueError` al convertir un texto
que no es un número válido), pero no se cubren en profundidad aquí.

---

## 7️⃣ Aplicación práctica

**Resultado de aprendizaje**: RA-7.

### 🌍 Contexto

Cada bloque anterior mostró una habilidad por separado: abrir y cerrar, leer, escribir,
procesar, manejar un error. Un programa real casi siempre combina varias de esas
habilidades para resolver un problema completo.

### 🧠 Concepto

Un programa que lee, procesa y guarda datos de forma robusta sigue, en general, esta
estructura:

```text
try:
    abrir el archivo de entrada (with)
    leer su contenido
    procesar cada línea (limpiar, dividir, transformar)
    escribir el resultado en el archivo de salida (with)
except FileNotFoundError:
    avisar de forma clara que el archivo de entrada no existe
```

### 📖 Explicación

**Por qué `with` sigue siendo importante dentro de un `try`.** Aunque el `try` ya
protege contra `FileNotFoundError`, `with` sigue garantizando que, pase lo que pase
dentro del bloque (incluido otro tipo de error inesperado), el archivo que sí se llegó
a abrir se cierre correctamente. Las dos herramientas resuelven problemas distintos: `with`
cierra el archivo; `try`/`except` evita que el programa se detenga por un error
anticipado.

El taller de esta clase (más adelante, en las actividades) aplica exactamente esta
estructura: lee un archivo de ventas que podría no existir, procesa cada línea, y
escribe un reporte — el resultado esperado (RA-7) del módulo completo.

---

## 7️⃣ Aplicación práctica

**Resultado de aprendizaje**: RA-7.

### 🌍 Contexto

### 🧠 Concepto

### 📖 Explicación
