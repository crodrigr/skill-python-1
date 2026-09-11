# Quiz 01 — Fundamentos de Programación con Python

**Instrucciones**: 10 preguntas. En las de selección múltiple, marca **una** opción. En
las de análisis y de corrección, escribe tu respuesta con una breve justificación. El
problema final se entrega como código.

> Este documento no incluye las respuestas. La clave está en
> `../soluciones/soluciones-quiz.md` (material docente).

---

## 1. [Selección múltiple]

¿Cuál de las siguientes afirmaciones describe **mejor** por qué Python es adecuado para
aprender a programar?

- A) Porque es el único lenguaje que se ejecuta sin errores.
- B) Porque tiene una sintaxis clara y legible y se ejecuta línea por línea sin
  compilar.
- C) Porque no usa variables ni operadores.
- D) Porque solo sirve para hacer páginas web.

_RA: RA-1_

---

## 2. [Selección múltiple]

¿Cuál de estos nombres de variable es **válido** en Python?

- A) `2do_intento`
- B) `precio final`
- C) `promedio_notas`
- D) `for`

_RA: RA-2_

---

## 3. [Selección múltiple]

Dada la asignación `activo = True`, ¿de qué tipo es el valor guardado en `activo`?

- A) `str`
- B) `int`
- C) `float`
- D) `bool`

_RA: RA-2_

---

## 4. [Selección múltiple]

Un problema pide: "leer el precio de un producto y la cantidad comprada, y mostrar el
total a pagar". ¿Cuál es el **proceso** en el análisis entrada–proceso–salida?

- A) El precio y la cantidad.
- B) Multiplicar el precio por la cantidad.
- C) Mostrar el total a pagar.
- D) El nombre del producto.

_RA: RA-3_

---

## 5. [Análisis de código]

Analiza el siguiente programa. Indica **qué valor imprime** y explica **en qué orden**
se aplican los operadores.

```python
resultado = 2 + 3 * 4 ** 2
print(resultado)
```

_RA: RA-4_

---

## 6. [Selección múltiple]

¿Cuál es el valor de la siguiente expresión?

```python
(5 > 3) and (2 >= 4)
```

- A) `True`
- B) `False`
- C) `5`
- D) Error

_RA: RA-4_

---

## 7. [Identificación de resultado]

¿Qué imprime este código?

```python
x = 7
if x > 10:
    print("A")
elif x > 5:
    print("B")
elif x > 0:
    print("C")
else:
    print("D")
```

- A) `A`
- B) `B`
- C) `C`
- D) `B` y `C`

_RA: RA-5_

---

## 8. [Corrección de errores]

El siguiente programa debería imprimir los números del 1 al 5, pero **no termina nunca**
(bucle infinito). Identifica el error y reescribe el código corregido.

```python
numero = 1
while numero <= 5:
    print(numero)
```

_RA: RA-6_

---

## 9. [Análisis de código]

Analiza el siguiente programa. Indica **qué valor imprime**, explica cómo cambia la
variable `total` en cada vuelta y justifica por qué aquí es adecuado un bucle `for` y no
un `while`.

```python
total = 0
for i in range(1, 4):
    total = total + i * 2
print(total)
```

_RA: RA-6, RA-7, RA-8_

---

## 10. [Problema breve de programación]

Escribe un programa que:

1. guarde en variables el precio de **tres** productos (valores fijos en el código);
2. use un bucle para sumar los tres precios en una variable `total`;
3. muestre `total` y, con una estructura condicional, imprima `"caro"` si `total` es
   mayor que `10000` o `"barato"` en caso contrario.

Tu solución debe combinar: variables, un operador aritmético, una repetición y una
decisión.

_RA: RA-8, RA-9_
