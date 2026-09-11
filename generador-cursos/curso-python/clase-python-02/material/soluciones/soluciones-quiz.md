# Clave del Quiz 02 — Clase 02: Funciones

> **Material docente.** No entregar al estudiantado. Referencia rápida:
> 1-B · 2-C · 3-B · 4-B · 5-D · 6→12 · 7→"negativo" · 8-A · 9→falta `return resultado` ·
> 10→función `promedio`

---

## 1. Respuesta: **B**

Una función encapsula una tarea con un nombre para poder reutilizarla y organizar el
código en piezas. A) es falso (una función no acelera por sí misma); C) es falso (las
funciones usan variables); D) no tiene sentido.

_RA: RA-1_

---

## 2. Respuesta: **C**

`registrar()` (nombre seguido de paréntesis, fuera de la definición) es la llamada. A) es
la definición; B) es una instrucción del cuerpo; D) es falso.

_RA: RA-2_

---

## 3. Respuesta: **B**

`monto` y `propina` aparecen en la definición: son **parámetros**. En la llamada
`cobrar(1000, 150)`, `1000` y `150` son los argumentos.

_RA: RA-3_

---

## 4. Respuesta: **B**

`return` entrega un valor al punto donde se llamó la función (y la termina); `print` solo
muestra texto en pantalla y no entrega nada que el programa pueda reutilizar.

_RA: RA-4_

---

## 5. Respuesta: **D**

`entrada()` falla con `TypeError`: falta el argumento obligatorio `nombre`. A) usa el
valor por defecto de `saludo`; B) pasa ambos; C) pasa `nombre` por nombre. Todas menos D
son válidas.

_RA: RA-3_

---

## 6. Respuesta: imprime **12**

Primero se evalúa `doble(5)` → `10`. Ese `10` se pasa a `mas_uno(10)` → `11`.

Corrección: `mas_uno(doble(5))` = `mas_uno(10)` = `11`. **Imprime `11`.** El orden es:
funciones internas primero (`doble`), luego las externas (`mas_uno`), luego `print`.

_RA: RA-4, RA-7_

---

## 7. Respuesta: imprime **`negativo`**

`signo(-4)`: `-4 > 0` es falso, se salta el primer `return`. `-4 < 0` es verdadero, se
ejecuta `return "negativo"` y la función **termina ahí**: nunca llega a
`return "cero"`. `return` corta la ejecución de la función.

_RA: RA-4_

---

## 8. Respuesta: **A**

`entrada("Ana")` usa el valor por defecto `saludo="Hola"` → `Hola, Ana`.
`entrada("Luis", "Buenas")` reemplaza el valor por defecto → `Buenas, Luis`.

_RA: RA-3_

---

## 9. Respuesta: falta `return`

La función calcula `resultado` pero no lo devuelve, así que `area_triangulo(10, 4)`
vale `None`. Código corregido:

```python
def area_triangulo(base, altura):
    resultado = base * altura / 2
    return resultado

print("Área:", area_triangulo(10, 4))
```

Salida: `Área: 20.0`.

_RA: RA-2, RA-4_

---

## 10. Respuesta: función `promedio`

```python
def promedio(a, b, c):
    """Devuelve el promedio de tres números."""
    return (a + b + c) / 3

print("Ana:", promedio(7, 8, 9))
print("Luis:", promedio(5, 6, 10))
print("Eva:", promedio(9, 9, 6))
```

Salida (idéntica a la del programa original):

```text
Ana: 8.0
Luis: 7.0
Eva: 8.0
```

Se acepta cualquier solución equivalente en la que el cálculo del promedio aparezca una
sola vez, dentro de la función.

_RA: RA-5, RA-6_
