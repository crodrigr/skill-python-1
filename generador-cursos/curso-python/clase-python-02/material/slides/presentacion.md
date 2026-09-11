<!--
Presentación — Clase 02: Funciones en Python
Formato: Markdown compatible con Marp. Cada diapositiva va separada por una línea "---".
Regla: una sola idea clave por diapositiva; primero el apoyo visual, después poco texto.
Total: 23 diapositivas (rango permitido 15-25).
-->

# 📘 Clase 02
## Funciones en Python

Curso: Introducción a la Programación con Python · Duración: 3 horas

---

## 🎯 Qué vas a lograr hoy

- Explicar qué es una función y para qué sirve.
- Definir funciones, llamarlas y pasarles datos con parámetros.
- Devolver resultados con `return`.
- Refactorizar código repetido usando funciones.

---

## 📋 El problema: código repetido

```python
print("Promedio de Ana:", (60 + 70 + 80) / 3)
print("Promedio de Luis:", (50 + 90 + 100) / 3)
print("Promedio de Eva:", (80 + 85 + 90) / 3)
```

El mismo cálculo, escrito tres veces. Si cambia, hay que corregirlo en tres sitios.

---

## 🧩 ¿Qué es una función?

```python
def promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3
```

Un fragmento de código **con nombre** que resuelve una tarea. Se escribe una vez y se
usa muchas.

---

## 📦 Encapsular y abstraer

```text
promedio(60, 70, 80)   →   70.0
```

- **Encapsular**: los pasos quedan dentro; desde fuera solo ves el nombre y el resultado.
- **Abstraer**: piensas "calcular el promedio", no la fórmula.

---

## ✏️ Definir con `def`

```python
def mostrar_bienvenida():
    """Muestra el encabezado del sistema."""
    print("Sistema de biblioteca")
```

`def` · nombre · `()` · `:` · cuerpo con sangría. Definir **no ejecuta** el cuerpo.

---

## 📞 Llamar a la función

```python
mostrar_bienvenida()
```

El nombre seguido de `()` **ejecuta** el cuerpo. Se puede llamar tantas veces como haga
falta.

---

## 🔄 Flujo de ejecución

```text
mostrar_bienvenida()  ─┐  (1) salta al cuerpo
  print(...)  ←────────┘  (2) ejecuta el cuerpo
  print(...)  ──────────┐
print("Fin")  ←─────────┘  (3) vuelve y sigue
```

---

## ⏫ Definir antes de llamar

```python
saludar()          # error: aún no existe
def saludar():
    print("Hola")
```

La definición debe aparecer **antes** de la llamada.

---

## 🎛️ Parámetros y argumentos

```python
def area(base, altura):     # parámetros
    return base * altura

area(3, 4)                   # argumentos
```

Parámetro: en la definición. Argumento: el valor en la llamada.

---

## 🎛️ Posicionales y por nombre

```python
area(3, 4)
area(altura=4, base=3)
```

Por posición, el orden importa. Por nombre, no: cada valor dice a qué parámetro va.

---

## 🎛️ Valores por defecto

```python
def precio_con_impuesto(precio, iva=0.19):
    return precio + precio * iva

precio_con_impuesto(1000)        # iva = 0.19
precio_con_impuesto(1000, 0.10)  # iva = 0.10
```

---

## ↩️ `return`: entregar un valor

```python
def area(base, altura):
    return base * altura

total = area(3, 4) + area(10, 2)
```

`return` termina la función y **devuelve** un valor que el programa puede usar.

---

## ↩️ `return` frente a `print`

| | `print(...)` | `return ...` |
|---|---|---|
| Hace | muestra en pantalla | entrega un valor |
| ¿Reutilizable? | no | sí |

---

## 🔳 Sin `return` → `None`

```python
def area_triangulo(base, altura):
    resultado = base * altura / 2   # no devuelve nada

print(area_triangulo(10, 4))   # None
```

Falta `return resultado`.

---

## 🔒 Alcance: variables locales

```python
def calcular():
    resultado = 42     # local

calcular()
print(resultado)       # error: no existe aquí
```

Lo que se crea dentro de la función no vive fuera. Para sacarlo: `return`.

---

## 🔧 Refactorizar: antes

```python
print("Ana:", (60 + 70 + 80) / 3)
print("Luis:", (50 + 90 + 100) / 3)
print("Eva:", (80 + 85 + 90) / 3)
```

Cálculo repetido tres veces.

---

## 🔧 Refactorizar: después

```python
def promedio(a, b, c):
    return (a + b + c) / 3

print("Ana:", promedio(60, 70, 80))
print("Luis:", promedio(50, 90, 100))
```

Misma salida, un solo lugar que mantener.

---

## ✨ Buenas prácticas

- Nombre con **verbo**: `calcular_total`, `mostrar_boleta`.
- **Una responsabilidad** por función.
- Un **docstring** breve que diga qué hace.

---

## 🧬 Componer funciones

```python
def total_a_pagar(precio, cantidad, dcto):
    return con_descuento(subtotal(precio, cantidad), dcto)
```

Una función usa el resultado de otra; un bloque principal las coordina.

---

## 🛠️ Actividad práctica

**Taller 01 — Calculadora de cuenta con propina**

Descomponer en funciones (propina, total, división por comensales, formato), componerlas
en `main()` y refactorizar el formato repetido.

---

## 📌 Resumen

- Función = tarea con nombre, reutilizable.
- Datos entran por **parámetros**; resultados salen con **`return`**.
- Valores por defecto y argumentos por nombre dan flexibilidad.
- Refactorizar = mover lo repetido a una función, sin cambiar la salida.

---

## 📝 Evaluación

**Quiz 02** — 10 preguntas:

5 de selección múltiple · 2 de análisis de código · 1 de identificación de resultado ·
1 de corrección de errores · 1 problema breve (escribir/refactorizar una función).
