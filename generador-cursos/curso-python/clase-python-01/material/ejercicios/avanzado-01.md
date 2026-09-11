# Avanzado 01 — Suma de los primeros números

## Problema

Escribe un programa que calcule la suma de todos los números enteros del 1 al `n`
(incluyéndolo) y cuente cuántos de esos números son pares.

Por ejemplo, para `n = 5`: la suma es `1 + 2 + 3 + 4 + 5 = 15` y hay `2` pares (el 2 y
el 4).

## Entrada

- `n` (`int`, mayor o igual a 1), fijado en el código.

## Proceso esperado

1. Crear dos acumuladores: `suma` (en 0) y `cantidad_pares` (en 0).
2. Recorrer los números del 1 al `n` con un bucle `for` y `range`.
3. En cada vuelta, sumar el número a `suma` y, si el número es par (`numero % 2 == 0`),
   aumentar `cantidad_pares`.

## Salida

Dos líneas. Ejemplo, para `n = 5`:

```text
Suma: 15
Cantidad de pares: 2
```

## Restricciones

- Debe usarse un bucle `for` (el número de vueltas se conoce: son `n`).
- Se permite un `if` dentro del bucle para contar los pares.
- Identificadores y comentarios en español.

## Dificultad

Avanzado

## Resultados de aprendizaje

- RA-6: usar un bucle `for` para repetir un proceso.
- RA-7: reconocer que `for` es adecuado cuando se conoce el número de repeticiones.
