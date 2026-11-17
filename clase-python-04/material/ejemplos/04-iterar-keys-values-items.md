# 💡 Ejemplo 04 — Iterar con keys, values e items

**Tema**: recorrido de un diccionario con `keys()`, `values()` e `items()` ·
**Resultado de aprendizaje**: RA-6 · **Nivel**: intermedio

## 🧩 Problema

Una tienda quiere: listar solo los nombres de los productos que tiene a la venta,
listar solo los precios (por ejemplo, para calcular el precio máximo), y mostrar un
catálogo completo con el nombre y el precio de cada producto en una misma línea.

## 🔍 Análisis

- **Entrada**: diccionario `precios` (`producto -> precio`).
- **Proceso**: recorrer las claves con `keys()`, los valores con `values()`, y ambos a
  la vez con `items()`.
- **Salida**: la lista de nombres, el precio máximo, y el catálogo completo.

## 💡 Solución

1. Recorrer `precios.keys()` para mostrar cada nombre.
2. Recorrer `precios.values()` y usar `max` para el precio más alto.
3. Recorrer `precios.items()` desempaquetando `producto, precio` para el catálogo.

## 💻 Código

```python
precios = {"pan": 1300, "leche": 1000, "huevos": 2600, "queso": 3200}

print("Productos disponibles:")
for producto in precios.keys():
    print("-", producto)

precio_maximo = max(precios.values())
print("Precio más alto:", precio_maximo)

print("Catálogo completo:")
for producto, precio in precios.items():
    print(producto, "-", precio)
```

## 🧭 Explicación paso a paso

1. `precios.keys()` da una vista de las claves; el `for` la recorre una por una,
   mostrando cada nombre de producto con un guion delante.
2. `precios.values()` da una vista de los valores; `max(...)` sobre esa vista encuentra
   el precio más alto sin necesidad de saber a qué producto pertenece.
3. `precios.items()` da una vista de pares `(clave, valor)`; el `for producto, precio in
   ...` desempaqueta cada par en dos variables en el mismo paso, permitiendo mostrar
   ambos datos juntos.
4. El orden de recorrido en los tres casos es el orden en que las claves se agregaron al
   diccionario.

## ✅ Resultado esperado

```text
Productos disponibles:
- pan
- leche
- huevos
- queso
Precio más alto: 3200
Catálogo completo:
pan - 1300
leche - 1000
huevos - 2600
queso - 3200
```
