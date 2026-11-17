# ❓ Quiz 01 — Diccionarios

**Instrucciones**: 10 preguntas. En las de selección múltiple, marca **una** opción. En
las de análisis y de corrección, escribe tu respuesta con una breve justificación. El
problema final se entrega como código.

> Este documento no incluye las respuestas. La clave está en
> `../soluciones/soluciones-quiz.md` (material docente).

---

## 1️⃣ [🔘 Selección múltiple]

Un sistema necesita guardar el precio de cada producto de una tienda, buscando siempre
por el **nombre** del producto. ¿Cuál estructura es la más adecuada?

- A) Una lista, porque conserva el orden de los productos.
- B) Un diccionario, porque asocia cada nombre de producto (clave) con su precio (valor).
- C) Un conjunto, porque no permite productos repetidos.
- D) Una tupla, porque los precios no deberían cambiar nunca.

_RA: RA-1_

---

## 2️⃣ [🔘 Selección múltiple]

¿Cuál de las siguientes expresiones crea correctamente un diccionario?

- A) `datos = ["nombre": "Ana", "edad": 20]`
- B) `datos = ("nombre": "Ana", "edad": 20)`
- C) `datos = {"nombre": "Ana", "edad": 20}`
- D) `datos = {"nombre", "Ana", "edad", 20}`

_RA: RA-2_

---

## 3️⃣ [🔘 Selección múltiple]

Dado `precios = {"pan": 1200}`, ¿qué ocurre al ejecutar `print(precios["leche"])`?

- A) Imprime `None`.
- B) Imprime una cadena vacía.
- C) Python detiene el programa con `KeyError`.
- D) Agrega `"leche"` al diccionario con valor `0`.

_RA: RA-3_

---

## 4️⃣ [🔘 Selección múltiple]

¿Cuál es la diferencia principal entre `diccionario.pop(clave)` y
`del diccionario[clave]`?

- A) No hay ninguna diferencia real.
- B) `pop` elimina y devuelve el valor eliminado; `del` elimina sin devolver nada.
- C) `del` funciona con diccionarios y `pop` solo con listas.
- D) `pop` no elimina la clave, solo la oculta.

_RA: RA-5_

---

## 5️⃣ [🔘 Selección múltiple]

¿Qué devuelve `diccionario.items()`?

- A) Solo las claves del diccionario.
- B) Solo los valores del diccionario.
- C) Una vista de pares `(clave, valor)`.
- D) La cantidad de elementos del diccionario.

_RA: RA-6_

---

## 6️⃣ [🔬 Análisis de código]

Analiza el siguiente programa. Indica **qué diccionario final imprime**.

```python
inventario = {"lápices": 10, "gomas": 5}
inventario["lápices"] = 8
inventario.update({"gomas": 12, "reglas": 20})
inventario.pop("gomas")

print(inventario)
```

_RA: RA-4, RA-5_

---

## 7️⃣ [🔬 Análisis de código]

Analiza el siguiente programa. Indica **qué imprime** y explica por qué el segundo
`setdefault` no cambia el valor de `"pan"`.

```python
conteo = {}
conteo.setdefault("pan", 0)
conteo["pan"] += 1
conteo.setdefault("pan", 100)

print(conteo)
```

_RA: RA-7_

---

## 8️⃣ [🎯 Identificación de resultado]

¿Qué imprime el siguiente programa?

```python
puntos = {"Ana": 10, "Luis": 25, "Eva": 15}
for nombre, cantidad in puntos.items():
    if cantidad > 12:
        print(nombre)
```

- A) `Ana`
- B) `Ana`, `Luis`, `Eva`
- C) `Luis`, `Eva`
- D) No imprime nada.

_RA: RA-6_

---

## 9️⃣ [🐛 Corrección de errores]

El siguiente programa debería mostrar el precio de `"queso"` o `"No disponible"` si no
está registrado, pero falla con un error cuando `"queso"` no está en el diccionario.
Identifica el error y corrígelo.

```python
precios = {"pan": 1200, "leche": 950}
print(precios["queso"])
```

_RA: RA-3_

---

## 🔟 [💻 Problema breve de programación]

Una biblioteca registra, para cada préstamo del mes, el título del libro prestado (en
una lista, con repetidos: un libro prestado varias veces aparece varias veces). Escribe
un programa que:

1. Elija y justifique en un comentario por qué un diccionario es la estructura
   adecuada para contar cuántas veces se prestó cada libro distinto.
2. Construya el diccionario de conteo usando `get` o `setdefault` (no fijando las
   claves de antemano).
3. Muestre el título del libro más prestado.

_RA: RA-7, RA-8_
