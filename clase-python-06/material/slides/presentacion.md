# 📘 Clase 06 — Módulos y manejo de excepciones

Introducción a la Programación con Python

---

## 🎯 Objetivos

- Crear e importar módulos propios.
- Usar `collections` y el protocolo `iter()`/`next()`.
- Manejar errores con `try`/`except`/`else`/`finally`.

---

## 📦 ¿Qué es un módulo?

Un archivo `.py` que agrupa funciones y variables relacionadas, como una caja de
herramientas ordenada por tipo de herramienta.

---

## 🧠 ¿Por qué modularizar?

- 🗂️ Organización: cada archivo tiene un propósito claro.
- 🔧 Mantenibilidad: se sabe dónde buscar y corregir.
- ♻️ Reusabilidad: se importa desde cualquier programa nuevo.

---

## 📥 Formas de importar

| Forma | Uso |
|---|---|
| `import modulo` | `modulo.funcion()` |
| `from modulo import nombre` | `nombre()` |
| `import modulo as alias` | `alias.funcion()` |
| `from modulo import nombre as alias` | `alias()` |

---

## 💡 Ejemplo: módulo propio

```python
# operaciones_basicas.py
def sumar(a, b):
    return a + b
```

```python
# principal.py
import operaciones_basicas
print(operaciones_basicas.sumar(4, 3))
```

---

## 🗂️ Módulo `collections`

- `deque`: agregar/quitar eficiente por ambos extremos.
- `Counter`: cuenta apariciones de cada elemento.
- Ambos son **iterables**, como una lista.

---

## 🔁 Iterables e iteradores

| Iterable | Iterador |
|---|---|
| Se puede recorrer (`for`) | Tiene estado: recuerda por dónde va |
| Lista, tupla, `deque`... | Se obtiene con `iter(iterable)` |

---

## ➡️ Protocolo `iter()` / `next()`

```python
cola = collections.deque(["a", "b"])
it = iter(cola)
next(it)  # "a"
next(it)  # "b"
next(it)  # StopIteration
```

`for` hace esto mismo por dentro, y maneja `StopIteration` automáticamente.

---

## 🚨 Manejo de errores: `try`/`except`

```python
try:
    numero = int(entrada)
except ValueError:
    print("No es un numero valido")
```

Captura tipos específicos: `ValueError`, `KeyError`, `ZeroDivisionError`.

---

## 🧩 Los bloques `else` y `finally`

- `else` → corre **solo si no hubo error** en el `try`.
- `finally` → corre **siempre**, haya o no error.

---

## ✅ Buena práctica

- ❌ `except:` sin tipo — oculta errores inesperados.
- ✅ `except ValueError:` — captura solo lo que sabes manejar.

---

## 🛠️ Actividad práctica: Menú para comprar

- 📦 Módulo `catalogo.py` (producto → precio).
- 🔁 Mostrar el catálogo iterando sobre él.
- 🚨 `try`/`except`/`else`/`finally` para cantidad inválida o producto inexistente.

---

## 📌 Resumen

- 📦 Módulo: archivo `.py` reutilizable; `import`, `from...import`, alias.
- 🗂️➡️🔁 `collections` (`deque`, `Counter`) como base de `iter()`/`next()`.
- 🚨 `try`/`except`/`else`/`finally` para manejar errores con claridad.

---

## 📝 Evaluación

- 🧪 Quiz de 10 ítems (individual).
- 🛠️ Taller guiado: menú para comprar.
- 🎓 Se evalúan los 7 resultados de aprendizaje de la clase.
