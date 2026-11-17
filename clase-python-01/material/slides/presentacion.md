<!--
Presentación — Clase 01: Fundamentos de Programación con Python
Formato: Markdown compatible con Marp. Cada diapositiva va separada por una línea "---".
Regla: una sola idea clave por diapositiva; primero el apoyo visual, después poco texto.
Total: 22 diapositivas (rango permitido 15-25).
-->

# 📘 Clase 01
## Fundamentos de Programación con Python

Curso: Introducción a la Programación con Python · Duración: 4 horas

---

## 🎯 Qué vas a lograr hoy

- Entender cómo un problema se convierte en un programa.
- Usar variables, operadores, decisiones y repeticiones.
- Escribir y ejecutar tus primeros programas en Python.

---

## 🐍 ¿Qué es Python?

```python
print("Hola, mundo")
```

Un lenguaje de programación de **sintaxis clara**: el código se lee casi como una frase.

---

## 🐍 Características de Python

```text
programa.py  →  intérprete  →  resultado
```

- Legible y ordenado (la sangría es parte del lenguaje).
- **Interpretado**: se ejecuta línea por línea, sin compilar.
- De propósito general: datos, web, automatización, IA…

---

## 📦 Variables: la idea

```python
edad = 20
saldo = 1000
saldo = saldo - 250   # ahora saldo vale 750
```

Una **variable** es un nombre que guarda un valor. `=` significa "guarda este valor"
(comparar es otra cosa: `==`).

---

## 🏷️ Reglas para nombrar variables

| Válido | No válido |
|--------|-----------|
| `precio_total` | `precio-total` |
| `nota1` | `1nota` |
| `_temp` | `for` |

Un buen nombre describe lo que guarda.

---

## 🏷️ Tipos de datos básicos

| Tipo | Ejemplo |
|------|---------|
| `int` | `20` |
| `float` | `3.14` |
| `str` | `"Ana"` |
| `bool` | `True` |

---

## 📦 Variables en expresiones

```python
precio_unitario = 1200
cantidad = 3
precio_total = precio_unitario * cantidad   # 3600
```

El nombre se reemplaza por su valor al calcular.

---

## 🧠 ¿Qué es un algoritmo?

```text
1. Leer nota1
2. Leer nota2
3. promedio ← (nota1 + nota2) / 2
4. Mostrar promedio
```

Secuencia **finita**, **ordenada** y **precisa** de pasos que termina.

---

## 🔄 Entrada — Proceso — Salida

| Pregunta | Parte |
|----------|-------|
| ¿Qué datos tengo? | Entrada |
| ¿Qué hago con ellos? | Proceso |
| ¿Qué muestro? | Salida |

---

## 📜 De algoritmo a programa

```python
nota1 = float(input("Primera nota: "))
nota2 = float(input("Segunda nota: "))
promedio = (nota1 + nota2) / 2
print("El promedio es:", promedio)
```

Cada paso del algoritmo → una instrucción.

---

## ➕ Operadores aritméticos

| `+` `-` `*` | `/` → `3.0` |
|-------------|-------------|
| `//` entero | `7 // 2` → `3` |
| `%` resto | `7 % 2` → `1` |
| `**` potencia | `2 ** 3` → `8` |

---

## ⚖️ Operadores de comparación

```python
edad = 17
print(edad >= 18)   # False
```

`==` `!=` `<` `>` `<=` `>=` → siempre dan `True` o `False`.

---

## 🔗 Operadores lógicos

```python
print(True and False)   # False
print(True or False)    # True
print(not False)        # True
```

`and`: ambos · `or`: al menos uno · `not`: invierte. Ante la duda con el orden, usa
**paréntesis**: `(2 + 3) * 4` → `20`.

---

## 🔀 Tomar decisiones: `if` / `else`

```python
edad = 16
if edad >= 18:
    print("Puede ingresar")
else:
    print("No puede ingresar")
```

El bloque indentado se ejecuta solo si la condición es `True`.

---

## 🔀 Varios caminos: `if` / `elif` / `else`

```python
nota = 5.2
if nota >= 6.0:
    print("Aprobado")
elif nota >= 4.0:
    print("Recuperación")
else:
    print("Reprobado")
```

Se ejecuta el **primer** bloque cuya condición es verdadera.

---

## 🔁 Repetir: bucle `for`

```python
for numero in range(1, 6):
    print(numero)   # 1, 2, 3, 4, 5
```

Se usa cuando **sé cuántas veces** repetir.

---

## 🔁 Repetir: bucle `while`

```python
contador = 1
while contador <= 5:
    print(contador)
    contador = contador + 1
```

Se repite **mientras** la condición sea verdadera. Algo debe cambiar dentro.

---

## ⚖️ `for` vs `while`

| Sé cuántas veces | No lo sé; depende de una condición |
|------------------|-----------------------------------|
| `for` | `while` |
| "para cada…" | "hasta que…" / "mientras…" |

---

## 🛠️ Actividad práctica

**Taller 01 — Calculadora de propina**

Analiza → algoritmo → programa → prueba con casos.
Combina variables, operadores, una decisión y una repetición.

---

## 📌 Resumen

- Problema → análisis (entrada/proceso/salida) → algoritmo → programa → prueba.
- Variables guardan datos; operadores calculan y comparan.
- `if` decide; `for` y `while` repiten.

---

## 📝 Evaluación

**Quiz 01** — 10 preguntas: selección múltiple, análisis de código, identificación de
resultados, corrección de errores y un problema breve de programación.
