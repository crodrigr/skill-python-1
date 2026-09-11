# Clave del Quiz 01 — Clase 01

> **Material docente.** No entregar al estudiantado. Referencia rápida:
> 1-B · 2-C · 3-D · 4-B · 5→50 · 6-B · 7-B · 8→falta incrementar `numero` · 9→12 · 10→programa

---

## 1. Respuesta: **B**

Python es adecuado para aprender porque su sintaxis es clara y legible y es un lenguaje
interpretado (se ejecuta línea por línea, sin un paso de compilación). A) es falso
(ningún lenguaje evita todos los errores); C) es falso (sí usa variables y operadores);
D) es falso (es de propósito general).

_RA: RA-1_

---

## 2. Respuesta: **C**

`promedio_notas` cumple las reglas: empieza por letra y solo tiene letras y guion bajo.
A) empieza por dígito; B) tiene un espacio; D) `for` es una palabra reservada.

_RA: RA-2_

---

## 3. Respuesta: **D**

`True` (y `False`) son valores de tipo `bool`.

_RA: RA-2_

---

## 4. Respuesta: **B**

El **proceso** es lo que se hace con los datos: multiplicar precio por cantidad. A) es la
entrada; C) es la salida; D) no forma parte del problema.

_RA: RA-3_

---

## 5. Imprime **50**

Orden de evaluación por precedencia:

1. `4 ** 2` → `16` (la potencia primero).
2. `3 * 16` → `48` (multiplicación antes que la suma).
3. `2 + 48` → `50`.

Se acepta como correcta la respuesta que indique `50` y describa el orden
potencia → multiplicación → suma.

_RA: RA-4_

---

## 6. Respuesta: **B** (`False`)

`5 > 3` → `True`; `2 >= 4` → `False`. `True and False` → `False`.

_RA: RA-4_

---

## 7. Respuesta: **B**

`x = 7`. `x > 10` → `False`; `x > 5` → `True`, por lo que se ejecuta `print("B")` y se
ignoran el resto de `elif` y el `else`. En un `if/elif/else` se ejecuta **un solo**
bloque, por eso D es incorrecta.

_RA: RA-5_

---

## 8. Error: el bucle no modifica `numero`

La condición `numero <= 5` siempre es verdadera porque `numero` nunca cambia dentro del
bucle. Falta incrementarlo. Código corregido:

```python
numero = 1
while numero <= 5:
    print(numero)
    numero = numero + 1   # esta línea hace que el bucle avance y termine
```

Salida corregida: los números `1, 2, 3, 4, 5`, uno por línea.

_RA: RA-6_

---

## 9. Imprime **12**

- Vuelta con `i = 1`: `total = 0 + 1 * 2` → `2`.
- Vuelta con `i = 2`: `total = 2 + 2 * 2` → `6`.
- Vuelta con `i = 3`: `total = 6 + 3 * 2` → `12`.

`range(1, 4)` produce `1, 2, 3`. Es adecuado un `for` porque el número de repeticiones se
conoce de antemano (tres); un `while` obligaría a crear y actualizar manualmente un
contador y a escribir la condición de término.

_RA: RA-6, RA-7, RA-8_

---

## 10. Solución de referencia

```python
# 1. Variables con los tres precios
precio1 = 3000
precio2 = 4500
precio3 = 5000

# 2. Repetición: sumar los tres precios
total = 0
for precio in (precio1, precio2, precio3):
    total = total + precio

# 3. Decisión
print("Total:", total)
if total > 10000:
    print("caro")
else:
    print("barato")
```

Salida con estos valores:

```text
Total: 12500
caro
```

**Criterios de corrección** (se cumplen los cuatro elementos pedidos):

| Elemento | Presente en la solución |
|----------|-------------------------|
| Variables | `precio1`, `precio2`, `precio3`, `total` |
| Operador aritmético | `total + precio` |
| Repetición | bucle `for` |
| Decisión | `if total > 10000 / else` |

Se acepta cualquier variante equivalente (por ejemplo, sumar con tres líneas dentro de
un `for` sobre `range(3)` y una lista de precios, o usar `elif`). Debe imprimir `caro`
para un total mayor que 10000 y `barato` en caso contrario.

_RA: RA-8, RA-9_
