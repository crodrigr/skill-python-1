<!--
Presentación — Clase 04: Diccionarios
Formato: Markdown compatible con Marp. Cada diapositiva va separada por una línea "---".
Regla: una sola idea clave por diapositiva; primero el apoyo visual, después poco texto.
Rango permitido: 15-25 diapositivas.
-->

# 📘 Clase 04
## Diccionarios

Curso: Introducción a la Programación con Python · Duración: 3 horas

---

## 🎯 Qué vas a lograr hoy

- Crear diccionarios y acceder a sus valores por clave.
- Agregar, modificar y eliminar elementos.
- Recorrer diccionarios y usar sus métodos comunes.
- Resolver un problema práctico (conteo/agrupación) con un diccionario.

---

## 📖 ¿Qué es un diccionario?

```text
precios = {"pan": 1200, "leche": 950}
            clave    valor  clave  valor
```

Una colección de pares **clave-valor**: cada valor se busca por su clave, no por
posición.

---

## 📐 Lista, tupla, conjunto o diccionario

| Estructura | Se accede por... |
|------------|-------------------|
| Lista / Tupla | posición (índice) |
| Conjunto | pertenencia (`in`) |
| **Diccionario** | **clave** |

Usa un diccionario cuando los datos se identifican por un nombre o código.

---

## 📝 Crear un diccionario

```python
precios = {"pan": 1200, "leche": 950}
vacio = {}
```

Entre llaves `{ }`, pares `clave: valor` separados por comas.

---

## 🔑 Acceder por clave

```python
precios["pan"]        # 1200
precios["queso"]       # KeyError: no existe
```

Acceder a una clave que no existe detiene el programa.

---

## 🛡️ Evitar el error: get e in

```python
precios.get("queso", 0)   # 0 (valor por defecto)
"queso" in precios          # False
```

---

## ➕ Agregar y modificar

```python
precios["huevos"] = 2600   # agrega (no existía)
precios["pan"] = 1300       # modifica (ya existía)
```

La misma operación: agrega si la clave no está, modifica si ya está.

---

## 🔄 Actualizar varias claves: update

```python
precios.update({"leche": 1000, "queso": 3200})
```

Agrega las que faltan y actualiza las que ya existían, en una sola llamada.

---

## 🗑️ Eliminar: del, pop, popitem

```python
del precios["huevos"]        # elimina; no devuelve nada
precios.pop("leche")          # elimina y devuelve el valor
precios.pop("queso", 0)       # elimina seguro; 0 si no existía
precios.popitem()             # elimina el último par agregado
```

---

## 🔁 Recorrer un diccionario

```text
for producto in precios:            # recorre claves
for precio in precios.values():     # recorre valores
for p, precio in precios.items():   # recorre pares
```

---

## 🧰 Métodos comunes

| Método | Modifica |
|--------|----------|
| `get`, `keys`, `values`, `items`, `len` | No |
| `update`, `pop`, `popitem`, `setdefault`, `clear` | Sí |

---

## 🆕 setdefault: crear solo si falta

```python
conteo.setdefault("manzana", 0)
conteo["manzana"] += 1
```

Si la clave no existe, la crea con el valor inicial; si ya existe, no la toca.

---

## 🛠️ Actividad práctica

**Taller 01 — Gestor de inventario de una tienda**

Diccionario `producto -> cantidad`; agregar/actualizar, eliminar con `pop`, reporte con
`items()`, registrar venta de un producto nuevo con `setdefault`.

---

## 📌 Resumen

- Diccionario: pares clave-valor; se accede, agrega y modifica por clave, no por
  posición.
- `get`/`in` evitan `KeyError`; `pop`/`del` eliminan; `update` actualiza varias claves.
- `keys()`, `values()`, `items()`: las tres formas de recorrer un diccionario.
- `setdefault`: crea solo si falta — la base para contar y agrupar con diccionarios.

---

## 📝 Evaluación

**Quiz 01** — 10 preguntas: selección múltiple, análisis de código, identificación de
resultado, corrección de errores y un problema breve de programación.
