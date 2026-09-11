# 🛠️ Taller 01 — Registro de ventas de un día

**Actividad guiada** · Duración estimada: 40–50 min · **Resultados de aprendizaje**:
RA-2, RA-3, RA-5, RA-6, RA-7

## 🎯 Objetivo

Construir, paso a paso, un programa que registre las ventas de un día en un archivo de
texto, lo lea de forma segura (manejando el caso de que no exista), procese cada línea,
acumule el total vendido por producto en un diccionario, y genere un archivo de reporte
con el resumen y el total general de ventas (RA-2, RA-3, RA-5, RA-6, RA-7).

## 🌍 Contexto

Un negocio anota cada venta del día en un archivo de texto: una línea por venta, con el
producto, la cantidad y el precio unitario. Al final del día hay que generar un reporte
con el total vendido de cada producto y el total general, sin que el programa falle si
el archivo de ventas todavía no existe (por ejemplo, si todavía no se registró ninguna
venta).

## 🪜 Pasos

### 1️⃣ Crear el archivo de ventas

Mediante código, crea `ventas.txt` con varias líneas
`producto,cantidad,precio_unitario`, por ejemplo:

```text
pan,10,1300
leche,5,1000
pan,3,1300
queso,2,3200
```

### 2️⃣ Leer el archivo de forma segura

Abre `ventas.txt` para lectura dentro de un `try`/`except FileNotFoundError`. Si el
archivo no existe, muestra un mensaje claro y no continúes con el resto del programa
(usa una variable de control, por ejemplo `archivo_encontrado`, para decidir si sigue).

### 3️⃣ Procesar cada línea

Para cada línea leída, quita el salto de línea con `strip()` y divide por comas con
`split(",")` para obtener el producto, la cantidad y el precio unitario. Convierte
cantidad y precio a número con `int(...)`.

### 4️⃣ Acumular por producto y calcular el total

Usando un diccionario `producto -> cantidad_vendida` (como en la Clase 04), acumula la
cantidad vendida de cada producto con `get(producto, 0)`. Además, calcula el total
general de ventas sumando, para cada línea, `cantidad * precio_unitario`.

### 5️⃣ Escribir el reporte

Escribe `reporte_ventas.txt` con una línea por producto (`producto: cantidad_vendida
unidades`) y una última línea con el total general de ventas.

## 📦 Entregable

Un programa Python que crea `ventas.txt`, lo procesa manejando el caso de que no
exista, y escribe `reporte_ventas.txt` con el resumen por producto y el total general.

## 🧪 Casos de prueba

| Situación | Resultado esperado |
|-----------|----------------------|
| `ventas.txt` existe con las 4 líneas del ejemplo | `reporte_ventas.txt` con `pan: 13 unidades`, `leche: 5 unidades`, `queso: 2 unidades` y `Total general: 28300` |
| `ventas.txt` no existe (se usa una ruta que nunca se creó) | El programa muestra un mensaje comprensible y no se detiene con un error sin manejar; no se genera un reporte con datos inventados |

## 📏 Criterios de evaluación

- El archivo se abre con `with` y la lectura está protegida con
  `try`/`except FileNotFoundError`.
- Cada línea se limpia con `strip()` antes de dividirla con `split(",")`.
- El total vendido por producto se acumula en un diccionario, no en variables sueltas
  por producto.
- El total general de ventas es correcto (cantidad × precio de cada línea, sumado).
- El reporte se escribe correctamente cuando el archivo existe, y el programa avisa
  con claridad —sin generar un reporte con datos inventados— cuando no existe.

> Nota para el docente: una versión resuelta y comentada está disponible en
> `../../material/soluciones/soluciones-ejercicios.md` (sección "Taller 01"). No
> compartir con el estudiantado antes de la puesta en común.
