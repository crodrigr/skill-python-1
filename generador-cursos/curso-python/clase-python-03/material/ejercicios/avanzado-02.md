# Avanzado 02 — Etiquetas de productos por categoría

## Problema

Una tienda guarda sus productos como una lista de registros `(nombre_producto,
categoria, lista_de_etiquetas)`, donde `lista_de_etiquetas` es una lista de textos que
describen el producto:

```python
productos = [
    ("Zapatillas", "Deporte", ["running", "cómodo", "unisex"]),
    ("Balón", "Deporte", ["fútbol", "cómodo"]),
    ("Mochila", "Viaje", ["resistente", "unisex"]),
]
```

Escribe un programa que, para cada categoría distinta presente en `productos`:

1. Recorra la lista de productos con un bucle, y dentro de cada vuelta recorra las
   etiquetas de ese producto con otro bucle (bucle anidado).
2. Construya un conjunto con **todas** las etiquetas de los productos que pertenecen a
   esa categoría, sin repetir.
3. Muestre la categoría y su conjunto de etiquetas, ordenado alfabéticamente.

## Entrada

La lista `productos` dada arriba, fija en el código.

## Proceso esperado

Obtener primero el conjunto de categorías distintas (con un conjunto construido a
partir de la lista de productos). Para cada categoría, recorrer `productos` con un
bucle `for`; cuando la categoría del producto coincida, recorrer sus etiquetas con un
segundo bucle `for` (anidado) y agregarlas a un conjunto de etiquetas de esa categoría
con `add`. Mostrar el resultado ordenado con `sorted`.

## Salida

Una línea por categoría, con sus etiquetas únicas ordenadas alfabéticamente, por
ejemplo: `Deporte: ['cómodo', 'fútbol', 'running', 'unisex']`.

## Restricciones

- Debe usarse al menos un bucle anidado (un `for` de etiquetas dentro de un `for` de
  productos).
- Las etiquetas de cada categoría deben acumularse en un conjunto, no en una lista con
  comprobación manual de duplicados.
- Los identificadores y comentarios deben estar en español.

## Dificultad

Avanzado

## Resultados de aprendizaje

- RA-3, RA-4: recorrer listas de registros con bucles, incluidos bucles anidados.
- RA-8: acceder a los campos de un registro representado como tupla.
- RA-9: construir un conjunto de valores únicos a partir de datos repartidos en varios
  registros.
