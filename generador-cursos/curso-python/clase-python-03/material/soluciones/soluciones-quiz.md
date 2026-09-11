# 🔑 Clave del Quiz 01 — Clase 03

> **Material docente.** No entregar al estudiantado. Referencia rápida:
> 1-B · 2-A · 3-C · 4-B · 5-B · 6→pares=[8,12,10] · 7→2/True/False · 8-B ·
> 9→falta atributo append en tupla · 10→programa

---

## 1️⃣ Respuesta: **B**

Agrupar datos del mismo tipo bajo un solo nombre permite recorrerlos y procesarlos con
un bucle, en vez de repetir la misma lógica con `nota1`, `nota2`, etc. A) es irrelevante
(no se trata de espacio en pantalla); C) es falso (las variables sí guardan decimales);
D) es falso (las listas sí se modifican).

_RA: RA-1_

---

## 2️⃣ Respuesta: **A**

`letras[2:4]` toma los índices `2` y `3` (el `4` no se incluye): `["c", "d"]`. B) da
solo `["c"]`; C) da `["d", "e"]`; D) da una lista vacía (`inicio > fin`).

_RA: RA-2_

---

## 3️⃣ Respuesta: **C**

`sorted(lista)` devuelve una lista nueva y no toca la original. `append`, `remove` y
`pop` sí modifican la lista sobre la que se llaman.

_RA: RA-3_

---

## 4️⃣ Respuesta: **B**

`lista.sort()` ordena "en el lugar" (modifica la lista y devuelve `None`);
`sorted(lista)` construye y devuelve una lista nueva, dejando la original sin cambios.
A), C) y D) son falsas: ambas aceptan cualquier tipo comparable y ambas admiten
`reverse=True`.

_RA: RA-5_

---

## 5️⃣ Respuesta: **B**

Las tuplas son inmutables: intentar asignar un nuevo valor a una posición lanza
`TypeError: 'tuple' object does not support item assignment`. No hay forma de
"editar" una tupla existente.

_RA: RA-8_

---

## 6️⃣ `pares` queda `[8, 12, 10]`

El bucle recorre `numeros` y agrega a `pares` (con `append`) solo los valores pares, en
el orden en que aparecen: `8`, `12` y `10`. `numeros` no cambia porque el programa nunca
llama a un método que lo modifique (ni `append`, ni `remove`, ni asignación por
índice); solo se **lee** para decidir qué agregar a la lista nueva.

_RA: RA-3, RA-4_

---

## 7️⃣ Imprime `2`, `True`, `False`

- `{"oferta", "nuevo", "oferta", "destacado"}` se reduce a tres elementos únicos:
  `oferta`, `nuevo`, `destacado` (los conjuntos no admiten duplicados).
- `etiquetas.add("nuevo")` no cambia nada: `"nuevo"` ya estaba.
- `etiquetas.discard("destacado")` lo quita, dejando `{"oferta", "nuevo"}` → `len` es
  `2`.
- `"oferta" in etiquetas` es `True`; `"destacado" in etiquetas` es `False` porque ya se
  quitó.

_RA: RA-9_

---

## 8️⃣ Respuesta: **B**

Primera pasada sobre `[9, 3, 7, 1]`, comparando vecinos de izquierda a derecha:

1. Compara `(9, 3)`: `9 > 3` → intercambia → `[3, 9, 7, 1]`
2. Compara `(9, 7)`: `9 > 7` → intercambia → `[3, 7, 9, 1]`
3. Compara `(9, 1)`: `9 > 1` → intercambia → `[3, 7, 1, 9]`

Al final de la primera pasada, el `9` (el mayor) ya llegó a su posición final:
`[3, 7, 1, 9]`.

_RA: RA-6_

---

## 9️⃣ Error: las tuplas no tienen el método `append`

`producto` es una tupla, y las tuplas no admiten agregar, quitar ni modificar
elementos: `producto.append(...)` lanza
`AttributeError: 'tuple' object has no attribute 'append'`.

**Corrección conservando la inmutabilidad de nombre y precio**: separar lo que no debe
cambiar (nombre y precio, en una tupla) de lo que sí puede crecer (las etiquetas, en una
lista aparte):

```python
nombre_producto, precio_producto = ("Cuaderno", 1500)
etiquetas_producto = []
etiquetas_producto.append("nueva_etiqueta")
```

_RA: RA-8_

---

## 🔟 Solución de referencia

```python
# 1. Los mensajes no leídos por conversación pueden repetirse y no tienen por qué
#    modificarse individualmente aquí, pero como colección conviene una lista: se
#    necesita conservar una posición por conversación y permitir valores repetidos
#    (varias conversaciones con 0 mensajes no leídos).
no_leidos = [0, 5, 0, 12, 3, 0, 8]

# 2. sorted() es la opción adecuada: el objetivo es obtener una lista ordenada para
#    mostrarla, no comprender el mecanismo de ordenamiento; un algoritmo clásico haría
#    más trabajo sin ninguna ventaja aquí.
ordenado_desc = sorted(no_leidos, reverse=True)
print("De mayor a menor:", ordenado_desc)

# 3. Contar conversaciones sin mensajes pendientes
sin_pendientes = no_leidos.count(0)
print("Conversaciones sin mensajes pendientes:", sin_pendientes)
```

Salida esperada:

```text
De mayor a menor: [12, 8, 5, 3, 0, 0, 0]
Conversaciones sin mensajes pendientes: 3
```

**Criterios de corrección**:

| Elemento | Presente en la solución |
|----------|--------------------------|
| Justificación de la estructura (lista) | Comentario junto a `no_leidos` |
| Ordenamiento con `sorted`, no a mano | `sorted(no_leidos, reverse=True)` |
| Justificación de usar el ordenamiento integrado | Comentario junto al `sorted` |
| Conteo con función integrada | `no_leidos.count(0)` |

Se acepta cualquier variante equivalente (por ejemplo, ordenar ascendente y leer de
atrás hacia adelante), siempre que use `sorted`/`sort` y `count`, y justifique la
elección de estructura y de mecanismo de ordenamiento.

_RA: RA-7, RA-1, RA-5_
