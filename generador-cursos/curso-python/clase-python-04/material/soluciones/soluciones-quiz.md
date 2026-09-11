# 🔑 Clave del Quiz 01 — Clase 04

> **Material docente.** No entregar al estudiantado. Referencia rápida:
> 1-B · 2-C · 3-C · 4-B · 5-C · 6→{'lápices': 8, 'reglas': 20} · 7→{'pan': 1} ·
> 8-C · 9→usar get con valor por defecto · 10→programa

---

## 1️⃣ Respuesta: **B**

Un diccionario asocia cada nombre de producto (la clave) con su precio (el valor),
permitiendo buscar directamente por nombre. A) una lista obligaría a recorrerla para
encontrar un producto por nombre; C) un conjunto no puede asociar un precio a cada
producto; D) la inmutabilidad no es el criterio relevante aquí (los precios sí pueden
necesitar actualizarse).

_RA: RA-1_

---

## 2️⃣ Respuesta: **C**

`{"nombre": "Ana", "edad": 20}` es la sintaxis correcta: llaves, pares `clave: valor`
separados por comas. A) usa corchetes con `:` (sintaxis inválida); B) usa paréntesis
con `:` (sintaxis inválida); D) crea un conjunto de cuatro elementos sueltos, no pares
clave-valor.

_RA: RA-2_

---

## 3️⃣ Respuesta: **C**

Acceder con `[clave]` a una clave que no existe lanza `KeyError`. Para evitarlo se usa
`get` (que sí puede devolver `None` o un valor por defecto) o se comprueba antes con
`in`.

_RA: RA-3_

---

## 4️⃣ Respuesta: **B**

`pop` elimina la clave y **devuelve** el valor que tenía, útil para reutilizarlo o
mostrarlo; `del` elimina la clave sin devolver nada. Ambos funcionan sobre
diccionarios.

_RA: RA-5_

---

## 5️⃣ Respuesta: **C**

`items()` da una vista de pares `(clave, valor)`, pensada para recorrerse
desempaquetando ambos datos a la vez. `keys()` da solo las claves y `values()` solo los
valores.

_RA: RA-6_

---

## 6️⃣ Imprime `{'lápices': 8, 'reglas': 20}`

- `inventario["lápices"] = 8` modifica el valor de `"lápices"` (ya existía): pasa de
  `10` a `8`.
- `inventario.update({"gomas": 12, "reglas": 20})` actualiza `"gomas"` (de `5` a `12`)
  y agrega `"reglas"` con `20`.
- `inventario.pop("gomas")` elimina `"gomas"` del diccionario.
- Queda `{'lápices': 8, 'reglas': 20}`.

_RA: RA-4, RA-5_

---

## 7️⃣ Imprime `{'pan': 1}`

- El primer `setdefault("pan", 0)` crea la clave `"pan"` con valor `0` porque no
  existía.
- `conteo["pan"] += 1` la deja en `1`.
- El segundo `setdefault("pan", 100)` **no cambia nada**: `setdefault` solo asigna el
  valor indicado cuando la clave **no existe**; como `"pan"` ya existe (con valor `1`),
  la llamada no tiene efecto y devuelve el valor actual (`1`), pero no lo modifica.

_RA: RA-7_

---

## 8️⃣ Respuesta: **C**

El bucle recorre los pares en el orden de inserción: `Ana` (10, no cumple `> 12`),
`Luis` (25, sí), `Eva` (15, sí). Se imprime `Luis` y luego `Eva`.

_RA: RA-6_

---

## 9️⃣ Error: acceso directo a una clave que puede no existir

`precios["queso"]` lanza `KeyError` porque `"queso"` no está en `precios`. La
corrección es usar `get` con un valor por defecto:

```python
precios = {"pan": 1200, "leche": 950}
print(precios.get("queso", "No disponible"))
```

Salida corregida: `No disponible`.

_RA: RA-3_

---

## 🔟 Solución de referencia

```python
# Un diccionario es adecuado porque cada título de libro es un identificador con
# sentido y se necesita asociarle un conteo, no solo saber si el libro está presente.
prestamos = ["El principito", "1984", "El principito", "Cien años de soledad", "1984", "El principito"]

conteo_por_libro = {}
for titulo in prestamos:
    conteo_por_libro[titulo] = conteo_por_libro.get(titulo, 0) + 1

print(conteo_por_libro)

libro_mas_prestado = None
mayor_conteo = 0
for titulo, cantidad in conteo_por_libro.items():
    if cantidad > mayor_conteo:
        mayor_conteo = cantidad
        libro_mas_prestado = titulo

print("Libro más prestado:", libro_mas_prestado)
```

Salida con estos valores:

```text
{'El principito': 3, '1984': 2, 'Cien años de soledad': 1}
Libro más prestado: El principito
```

**Criterios de corrección**:

| Elemento | Presente en la solución |
|----------|--------------------------|
| Justificación del diccionario | Comentario junto a `conteo_por_libro` |
| Conteo con `get` (o `setdefault`), sin claves fijadas de antemano | `conteo_por_libro.get(titulo, 0) + 1` |
| Determinación del libro más prestado | Bucle sobre `items()` comparando conteos |

Se acepta cualquier variante equivalente (por ejemplo, usar `setdefault` en vez de
`get`, o `max` con una función auxiliar sobre `items()`).

_RA: RA-7, RA-8_
