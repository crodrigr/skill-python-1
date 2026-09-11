# ❓ Quiz 01 — Archivos de texto

**Instrucciones**: 10 preguntas. En las de selección múltiple, marca **una** opción. En
las de análisis y de corrección, escribe tu respuesta con una breve justificación. El
problema final se entrega como código.

> Este documento no incluye las respuestas. La clave está en
> `../soluciones/soluciones-quiz.md` (material docente).

---

## 1️⃣ [🔘 Selección múltiple]

¿Por qué un programa necesita guardar datos en un archivo en vez de solo mostrarlos con
`print`?

- A) Porque `print` no puede mostrar números decimales.
- B) Porque una variable desaparece cuando el programa termina, y un archivo persiste
     en el disco.
- C) Porque los archivos son más rápidos de crear que las variables.
- D) Porque `print` solo funciona con archivos abiertos.

_RA: RA-1_

---

## 2️⃣ [🔘 Selección múltiple]

¿Por qué se prefiere `with open(ruta, modo) as archivo:` frente a
`archivo = open(ruta, modo)` seguido de `archivo.close()`?

- A) Porque `with` es más corto de escribir.
- B) Porque `with` garantiza que el archivo se cierre incluso si ocurre un error dentro
     del bloque.
- C) Porque `open()`/`close()` manual no permite leer el archivo.
- D) Porque `with` funciona solo en modo lectura.

_RA: RA-2_

---

## 3️⃣ [🔘 Selección múltiple]

¿Qué devuelve `archivo.readlines()`?

- A) Todo el contenido como un solo texto.
- B) Una lista con cada línea del archivo como un elemento.
- C) Solo la primera línea del archivo.
- D) La cantidad de líneas del archivo.

_RA: RA-3_

---

## 4️⃣ [🔘 Selección múltiple]

Un archivo `datos.txt` ya existe con contenido. Se vuelve a abrir con
`open("datos.txt", "w")` y se escribe algo nuevo. ¿Qué pasa con el contenido anterior?

- A) Se conserva, y lo nuevo se agrega al final.
- B) Se pierde por completo: el modo `'w'` sobrescribe el archivo.
- C) Python pregunta antes de sobrescribir.
- D) No se puede abrir un archivo que ya existe en modo `'w'`.

_RA: RA-4_

---

## 5️⃣ [🔘 Selección múltiple]

¿Qué hace exactamente `try`/`except` en un programa?

- A) Repite un bloque de código varias veces.
- B) Anticipa un error posible: si ocurre dentro de `try`, ejecuta `except` en vez de
     detener el programa.
- C) Cierra automáticamente todos los archivos abiertos.
- D) Convierte un texto en un número.

_RA: RA-6_

---

## 6️⃣ [🔬 Análisis de código]

Analiza el siguiente programa. Indica **qué contenido final** tiene `registro.txt`.

```python
with open("registro.txt", "w") as archivo:
    archivo.write("Inicio\n")

with open("registro.txt", "a") as archivo:
    archivo.write("Proceso\n")

with open("registro.txt", "w") as archivo:
    archivo.write("Fin\n")
```

_RA: RA-4_

---

## 7️⃣ [🔬 Análisis de código]

Analiza el siguiente programa. Indica **qué imprime** (el archivo `"clave.txt"` no
existe en ningún momento).

```python
try:
    with open("clave.txt", "r") as archivo:
        contenido = archivo.read()
    print("Clave:", contenido)
except FileNotFoundError:
    print("Clave no configurada")

print("Programa terminado")
```

_RA: RA-6_

---

## 8️⃣ [🎯 Identificación de resultado]

Un archivo `datos.txt` contiene la línea `"10,20,30\n"`. ¿Qué imprime el siguiente
código?

```python
with open("datos.txt", "r") as archivo:
    linea = archivo.readline()

numeros = linea.strip().split(",")
print(len(numeros))
```

- A) `1`
- B) `3`
- C) `10`
- D) `"10,20,30"`

_RA: RA-3, RA-5_

---

## 9️⃣ [🐛 Corrección de errores]

El siguiente programa debería mostrar el contenido de `"perfil.txt"` o un mensaje si el
archivo no existe, pero detiene el programa con un error si el archivo no existe.
Identifica el problema y corrígelo.

```python
with open("perfil.txt", "r") as archivo:
    print(archivo.read())
```

_RA: RA-6_

---

## 🔟 [💻 Problema breve de programación]

Un archivo `pedidos.txt` (que podría no existir) tiene, por línea, un producto y una
cantidad separados por coma, por ejemplo `"lápiz,4"`. Escribe un programa que:

1. Intente leer `pedidos.txt` manejando el caso de que no exista con
   `try`/`except FileNotFoundError`, mostrando un mensaje claro si falta.
2. Si el archivo existe, sume todas las cantidades (conviértelas a número) y escriba el
   total en un archivo `total_pedidos.txt`, con el formato `"Total: <suma>"`.

_RA: RA-6, RA-7_
