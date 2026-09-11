# Quiz 01 — Estructuras de datos lineales y algoritmos de ordenamiento

**Instrucciones**: 10 preguntas. En las de selección múltiple, marca **una** opción. En
las de análisis y de corrección, escribe tu respuesta con una breve justificación. El
problema final se entrega como código.

> Este documento no incluye las respuestas. La clave está en
> `../soluciones/soluciones-quiz.md` (material docente).

---

## 1. [Selección múltiple]

¿Cuál de las siguientes afirmaciones describe **mejor** por qué conviene usar una lista
en vez de variables sueltas para guardar las cinco calificaciones de un estudiante?

- A) Porque una lista ocupa menos espacio en la pantalla al escribirla.
- B) Porque agrupa los datos del mismo tipo bajo un solo nombre y permite recorrerlos y
     procesarlos con un bucle.
- C) Porque las variables sueltas no pueden guardar números decimales.
- D) Porque una lista no permite modificar sus elementos.

_RA: RA-1_

---

## 2. [Selección múltiple]

Dada `letras = ["a", "b", "c", "d", "e"]`, ¿qué expresión obtiene `["c", "d"]`?

- A) `letras[2:4]`
- B) `letras[2:3]`
- C) `letras[-2:]`
- D) `letras[3:2]`

_RA: RA-2_

---

## 3. [Selección múltiple]

¿Cuál de las siguientes operaciones **no modifica** la lista original?

- A) `lista.append(10)`
- B) `lista.remove(10)`
- C) `sorted(lista)`
- D) `lista.pop()`

_RA: RA-3_

---

## 4. [Selección múltiple]

¿Cuál es la diferencia principal entre `lista.sort()` y `sorted(lista)`?

- A) `sort()` funciona solo con números; `sorted()` funciona con cualquier tipo de dato.
- B) `sort()` modifica la lista original y no devuelve nada útil; `sorted()` devuelve
     una lista nueva y deja la original sin cambios.
- C) `sorted()` solo ordena de menor a mayor; `sort()` permite ambos órdenes.
- D) No hay ninguna diferencia real entre ambas.

_RA: RA-5_

---

## 5. [Selección múltiple]

¿Qué ocurre al ejecutar el siguiente código?

```python
punto = (3, 4)
punto[0] = 10
```

- A) `punto` queda como `(10, 4)`.
- B) Python lanza `TypeError` porque las tuplas son inmutables.
- C) Python lanza `IndexError` porque el índice `0` no existe.
- D) No ocurre nada; Python ignora la instrucción.

_RA: RA-8_

---

## 6. [Análisis de código]

Analiza el siguiente programa. Indica **qué lista final imprime** `pares` y explica por
qué `numeros` no cambió.

```python
numeros = [3, 8, 5, 12, 7, 10]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(numeros)
print(pares)
```

_RA: RA-3, RA-4_

---

## 7. [Análisis de código]

Analiza el siguiente programa. Indica **qué imprime cada línea**.

```python
etiquetas = {"oferta", "nuevo", "oferta", "destacado"}
etiquetas.add("nuevo")
etiquetas.discard("destacado")

print(len(etiquetas))
print("oferta" in etiquetas)
print("destacado" in etiquetas)
```

_RA: RA-9_

---

## 8. [Identificación de resultado]

Se ordena la lista `[9, 3, 7, 1]` con el algoritmo de ordenamiento por burbuja
(comparando pares de vecinos de izquierda a derecha, intercambiando cuando el de la
izquierda es mayor). ¿Cuál es el estado de la lista **al terminar la primera pasada
completa**?

- A) `[1, 3, 7, 9]`
- B) `[3, 7, 1, 9]`
- C) `[9, 3, 7, 1]`
- D) `[3, 9, 7, 1]`

_RA: RA-6_

---

## 9. [Corrección de errores]

El siguiente programa debería agregar `"nueva_etiqueta"` a un registro de producto, pero
falla con un error. Identifica el error y explica cómo corregirlo sin perder la ventaja
de que el nombre y el precio del producto no puedan modificarse por accidente.

```python
producto = ("Cuaderno", 1500)
producto.append("nueva_etiqueta")
```

_RA: RA-8_

---

## 10. [Problema breve de programación]

Una app de mensajería guarda, para cada conversación, el número de mensajes no leídos
en una lista: `no_leidos = [0, 5, 0, 12, 3, 0, 8]`. Escribe un programa que:

1. Elija y justifique en un comentario si esta tarea requiere una lista, una tupla o un
   conjunto (ya está resuelto: es una lista; justifica por qué).
2. Muestre, usando `sorted` y sin escribir un algoritmo de ordenamiento a mano, la
   lista ordenada de mayor a menor cantidad de mensajes no leídos, justificando en un
   comentario por qué aquí conviene el ordenamiento integrado y no uno clásico.
3. Muestre cuántas conversaciones tienen exactamente `0` mensajes no leídos, usando
   `count`.

_RA: RA-7, RA-1, RA-5_
