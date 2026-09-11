# 🛠️ Taller 01 — Gestor de inventario de una tienda

**Actividad guiada** · Duración estimada: 40–50 min · **Resultados de aprendizaje**:
RA-2, RA-4, RA-5, RA-6, RA-7

## 🎯 Objetivo

Construir, paso a paso, un programa que mantenga el inventario de una tienda como un
diccionario `producto -> cantidad`, permita agregar productos y actualizar cantidades,
elimine un producto agotado devolviendo la cantidad que tenía, genere un reporte
recorriendo el inventario, y registre la venta de un producto que podría no estar
todavía registrado (RA-2, RA-4, RA-5, RA-6, RA-7).

## 🌍 Contexto

Una tienda lleva su inventario como un diccionario: cada producto es una clave y su
cantidad disponible es el valor. A lo largo del día llegan productos nuevos, se
actualizan cantidades, un producto se agota y hay que darlo de baja, y se registran
ventas de productos que podrían no estar todavía en el inventario.

## 🪜 Pasos

### 1️⃣ Crear el inventario inicial

```python
inventario = {"lápices": 50, "cuadernos": 20}
```

### 2️⃣ Agregar y actualizar

- Agrega `"gomas": 30` al inventario con asignación por clave.
- Imagina que llega una actualización de varios productos a la vez (por ejemplo, un
  reconteo); aplícala con `update`.

### 3️⃣ Eliminar un producto agotado

`"cuadernos"` se agotó. Elimínalo con `pop`, guardando la cantidad que tenía justo
antes de eliminarlo (para el registro de bajas).

### 4️⃣ Generar el reporte

Recorre el inventario con `items()` y muestra cada producto con su cantidad, una línea
por producto.

### 5️⃣ Registrar una venta de un producto nuevo

Define una función `registrar_venta(inventario_actual, producto)` que reste una unidad
al producto vendido. Si el producto todavía no está en el inventario (por ejemplo,
`"marcadores"`, que nunca se había registrado), debe inicializarse en `0` con
`setdefault` antes de sumar la unidad vendida (en este caso, sumar en vez de restar,
para registrar que entró una unidad al mostrador de venta rápida). Pruébala vendiendo
una unidad de `"marcadores"`.

## 📦 Entregable

Un programa Python que aplica los pasos 1 a 5 sobre `inventario` y muestra: la cantidad
que tenía `"cuadernos"` antes de eliminarlo, y el reporte final (producto y cantidad,
uno por línea).

## 🧪 Casos de prueba

| Estado inicial | Cambios aplicados | Reporte final esperado |
|-----------------|--------------------|--------------------------|
| `{"lápices": 50, "cuadernos": 20}` | agregar `"gomas": 30`; eliminar `"cuadernos"` con `pop`; registrar venta de `"marcadores"` (nuevo) | `lápices: 50`, `gomas: 30`, `marcadores: 1` (`cuadernos` ya no aparece) |

## 📏 Criterios de evaluación

- El inventario se agrega y actualiza con asignación por clave y con `update`, no
  recreando el diccionario completo.
- `pop` se usa para eliminar `"cuadernos"`, y la cantidad que devuelve se aprovecha o
  se muestra (no se descarta).
- El reporte se genera recorriendo con `items()`, no accediendo clave por clave a mano.
- La venta de `"marcadores"` (producto nuevo) se maneja con `setdefault` (o `get`) sin
  que el programa falle con `KeyError`.
- El programa produce la salida correcta para el caso de prueba indicado.

> Nota para el docente: una versión resuelta y comentada está disponible en
> `../../material/soluciones/soluciones-ejercicios.md` (sección "Taller 01"). No
> compartir con el estudiantado antes de la puesta en común.
