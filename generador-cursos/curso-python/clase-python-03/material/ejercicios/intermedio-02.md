# Intermedio 02 — Ingredientes de varias recetas

## Problema

Un recetario guarda cada receta como una tupla `(nombre_receta, lista_de_ingredientes)`,
donde `lista_de_ingredientes` es una lista de textos:

```python
receta_ensalada = ("Ensalada", ["lechuga", "tomate", "cebolla", "aceite"])
receta_sandwich = ("Sándwich", ["pan", "jamón", "queso", "tomate", "aceite"])
```

Escribe un programa que:

1. Acceda al nombre y a la lista de ingredientes de cada receta usando desempaquetado
   de la tupla.
2. Construya un conjunto con los ingredientes de la ensalada y otro con los del
   sándwich.
3. Muestre los ingredientes que ambas recetas tienen en común (intersección).
4. Muestre todos los ingredientes distintos que se necesitarían para preparar las dos
   recetas (unión), ordenados alfabéticamente con `sorted`.

## Entrada

Las dos tuplas `receta_ensalada` y `receta_sandwich` dadas arriba, fijas en el código.

## Proceso esperado

Desempaquetar cada tupla en dos variables (nombre e ingredientes); construir un
conjunto a partir de cada lista de ingredientes con `set(...)`; usar `&` para la
intersección y `|` para la unión; usar `sorted` sobre el resultado de la unión antes de
mostrarlo.

## Salida

Los ingredientes en común entre ambas recetas, y la lista ordenada de todos los
ingredientes distintos necesarios para las dos.

## Restricciones

- Cada receta debe seguir siendo una tupla `(nombre, lista_de_ingredientes)`; no
  convertirla a otra estructura.
- Los conjuntos deben construirse con `set(...)` a partir de las listas de
  ingredientes, no escribiendo los ingredientes comunes "a mano".
- Los identificadores y comentarios deben estar en español.

## Dificultad

Intermedio

## Resultados de aprendizaje

- RA-8: usar una tupla para representar un registro y desempaquetarla.
- RA-9: construir conjuntos a partir de listas y aplicar intersección y unión.
