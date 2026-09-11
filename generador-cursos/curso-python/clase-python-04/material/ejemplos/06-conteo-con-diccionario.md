# 💡 Ejemplo 06 — Contar repeticiones con un diccionario

**Tema**: resolver un problema de conteo construyendo un diccionario con `get` o
`setdefault` · **Resultado de aprendizaje**: RA-7, RA-8 · **Nivel**: avanzado

## 🧩 Problema

Una tienda registra, para cada venta del día, el producto vendido. La misma lista tiene
productos repetidos porque cada venta es una unidad. Se necesita saber cuántas unidades
se vendieron de cada producto distinto, sin haber declarado antes qué productos existen.

## 🔍 Análisis

- **Entrada**: lista `ventas_del_dia` con un producto por cada unidad vendida
  (con repetidos).
- **Proceso**: recorrer la lista y, por cada producto, sumar uno a su contador en un
  diccionario, inicializando el contador en cero (o directamente en uno) la primera vez
  que aparece.
- **Salida**: el diccionario de conteo por producto, y el producto más vendido.

## 💡 Solución

1. Crear un diccionario vacío `conteo_por_producto`.
2. Recorrer `ventas_del_dia`; por cada producto, usar `get(producto, 0)` para obtener
   el conteo actual (o `0` si es la primera vez) y sumarle `1`.
3. Encontrar el producto con mayor conteo recorriendo `items()`.

## 💻 Código

```python
ventas_del_dia = ["pan", "leche", "pan", "huevos", "pan", "leche", "queso", "pan"]

conteo_por_producto = {}
for producto in ventas_del_dia:
    conteo_por_producto[producto] = conteo_por_producto.get(producto, 0) + 1

print("Unidades vendidas por producto:", conteo_por_producto)

producto_mas_vendido = None
mayor_conteo = 0
for producto, cantidad in conteo_por_producto.items():
    if cantidad > mayor_conteo:
        mayor_conteo = cantidad
        producto_mas_vendido = producto

print("Producto más vendido:", producto_mas_vendido, "con", mayor_conteo, "unidades")
```

## 🧭 Explicación paso a paso

1. `conteo_por_producto = {}` empieza vacío: no hace falta saber de antemano qué
   productos se van a vender.
2. En cada vuelta, `conteo_por_producto.get(producto, 0)` devuelve el conteo actual del
   producto, o `0` si todavía no tiene entrada; sumarle `1` y volver a asignarlo con
   `conteo_por_producto[producto] = ...` incrementa el contador (o lo crea en `1` la
   primera vez).
3. `"pan"` aparece cuatro veces en la lista, así que termina con conteo `4`; `"leche"`
   aparece dos veces; `"huevos"` y `"queso"` una vez cada uno.
4. El segundo bucle recorre `conteo_por_producto.items()` comparando cada conteo contra
   el mayor visto hasta el momento, para encontrar el producto más vendido sin ordenar
   el diccionario.

## ✅ Resultado esperado

```text
Unidades vendidas por producto: {'pan': 4, 'leche': 2, 'huevos': 1, 'queso': 1}
Producto más vendido: pan con 4 unidades
```
