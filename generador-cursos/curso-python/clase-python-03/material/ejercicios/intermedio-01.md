# Intermedio 01 — Ranking de un videojuego

## Problema

Un videojuego guarda los resultados de una partida como una lista de registros
`(nombre_jugador, puntaje)`:

```python
resultados = [("Nico", 1200), ("Dani", 3400), ("Sofi", 2100), ("Max", 3400)]
```

Escribe un programa que:

1. Ordene los registros por puntaje, de mayor a menor, usando `sorted` con una función
   como `key` y `reverse=True`.
2. Muestre el ranking ordenado, una línea por jugador, con el formato
   `1. Dani - 3400 puntos`.
3. Recorra el ranking ordenado y construya una lista nueva solo con los nombres de
   quienes superaron los `2000` puntos.

## Entrada

La lista `resultados` dada arriba, fija en el código.

## Proceso esperado

Definir una función que reciba un registro y devuelva su puntaje, para usarla como
`key` de `sorted`; recorrer la lista ya ordenada con un bucle `for` y su índice para
numerar el ranking; construir la lista de nombres destacados con `append`.

## Salida

El ranking numerado (de mayor a menor puntaje) y, al final, la lista de nombres de
quienes superaron los 2000 puntos.

## Restricciones

- Usar `sorted` con `key` y `reverse=True`; no ordenar "a mano".
- El ranking se numera desde `1`, no desde `0`.
- Los identificadores y comentarios deben estar en español.

## Dificultad

Intermedio

## Resultados de aprendizaje

- RA-5: ordenar una lista de registros con `sorted`, `key` y `reverse`.
- RA-4: recorrer una lista y construir una lista nueva derivada de ella.
