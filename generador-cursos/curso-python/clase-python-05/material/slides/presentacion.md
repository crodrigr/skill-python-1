<!--
Presentación — Clase 05: Archivos de texto
Formato: Markdown compatible con Marp. Cada diapositiva va separada por una línea "---".
Regla: una sola idea clave por diapositiva; primero el apoyo visual, después poco texto.
Rango permitido: 15-25 diapositivas.
-->

# 📘 Clase 05
## Archivos de texto

Curso: Introducción a la Programación con Python · Duración: 3 horas

---

## 🎯 Qué vas a lograr hoy

- Abrir, leer y cerrar archivos de texto de forma segura.
- Escribir y agregar contenido sin perder datos.
- Manipular el contenido y guardar el resultado.
- Anticipar y manejar errores comunes de archivos.

---

## 📄 ¿Qué es un archivo de texto?

```text
programa (memoria) → termina → los datos desaparecen
archivo (disco)    → persiste → los datos quedan guardados
```

Un recurso fuera del programa donde los datos persisten como texto plano.

---

## 🔓 Abrir un archivo

```python
with open("notas.txt", "r") as archivo:
    ...
```

`open(ruta, modo)`. Modos: `'r'` leer, `'w'` escribir, `'a'` agregar.

---

## 🔐 with: cierre garantizado

```python
with open("notas.txt", "r") as archivo:
    contenido = archivo.read()
# se cierra solo, incluso si hay un error adentro
```

Preferible a `open()`/`close()` manual.

---

## 📖 Leer: read, readline, readlines

| Método | Devuelve |
|--------|----------|
| `read()` | todo el contenido, un solo texto |
| `readline()` | una línea a la vez |
| `readlines()` | lista con todas las líneas |

---

## 🔁 Recorrer un archivo

```python
with open("tareas.txt") as archivo:
    for linea in archivo:
        print(linea.strip())
```

`strip()` quita el salto de línea de cada una.

---

## ✏️ Escribir: write y writelines

```python
with open("reporte.txt", "w") as archivo:
    archivo.write("Total: 1500\n")
```

`writelines(lista)` escribe varias líneas de una vez.

---

## ⚠️ 'w' sobrescribe, 'a' agrega

```python
open("historial.txt", "w")   # borra todo lo anterior
open("historial.txt", "a")   # conserva y agrega al final
```

`'w'` no avisa antes de borrar.

---

## ✂️ Limpiar y dividir una línea

```python
linea = "manzana,25\n"
linea.strip()            # "manzana,25"
linea.strip().split(",")  # ['manzana', '25']
```

`strip()` quita el salto de línea; `split()` separa por un carácter.

---

## 🔄 Procesar y guardar

```python
nombre, cantidad = linea.strip().split(",")
cantidad = int(cantidad)
archivo_salida.write(nombre + ": " + str(cantidad) + "\n")
```

Leer → limpiar → dividir → transformar → escribir.

---

## 🚨 Archivo inexistente

```python
open("no_existe.txt", "r")
# FileNotFoundError
```

Abrir para leer un archivo que no existe detiene el programa.

---

## 🛡️ try / except

```python
try:
    with open("no_existe.txt") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("No se encontró el archivo")
```

Anticipa el error en vez de dejar que detenga el programa.

---

## ✨ with dentro de try

```python
try:
    with open(ruta) as archivo:
        ...
except FileNotFoundError:
    ...
```

`with` cierra el archivo; `try`/`except` evita que el error detenga el programa.

---

## 🛠️ Actividad práctica

**Taller 01 — Registro de ventas de un día**

Crear `ventas.txt`, leerlo con manejo de `FileNotFoundError`, acumular por producto en
un diccionario, y escribir `reporte_ventas.txt`.

---

## 📌 Resumen

- Archivo de texto: persiste en disco, a diferencia de una variable.
- `with open(ruta, modo) as archivo:` — cierre garantizado; modos `'r'`/`'w'`/`'a'`.
- Leer: `read()`, `readline()`, `readlines()`, o recorrer con `for`.
- `'w'` sobrescribe; `'a'` agrega. `strip()`+`split()` limpian y dividen cada línea.
- `try`/`except FileNotFoundError` anticipa que el archivo podría no existir.

---

## 📝 Evaluación

**Quiz 01** — 10 preguntas: selección múltiple, análisis de código, identificación de
resultado, corrección de errores y un problema breve de programación.
