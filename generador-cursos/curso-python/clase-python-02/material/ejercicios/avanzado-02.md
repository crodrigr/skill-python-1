# Avanzado 02 — Combinar funciones y un bucle

## Problema

Escribe dos funciones:

1. `factorial(n)` — devuelve el factorial de `n` (`n! = 1 · 2 · 3 · … · n`), calculado
   con un **bucle**. Por definición, `factorial(1)` es `1`.
2. `mostrar_factoriales(desde, hasta)` — recorre con un bucle los enteros de `desde` a
   `hasta` (ambos incluidos) e imprime, para cada uno, la línea `numero -> factorial`,
   llamando a `factorial`.

En el programa principal, llama a `mostrar_factoriales(1, 5)`.

## Entrada

- `desde` y `hasta` (`int`, con `desde <= hasta`), pasados en la llamada.

## Proceso esperado

1. En `factorial(n)`, partir de `resultado = 1` y multiplicarlo por cada entero de `2`
   a `n` con un bucle `for`; devolver `resultado`.
2. En `mostrar_factoriales(desde, hasta)`, usar un bucle `for` sobre el rango y, en cada
   vuelta, imprimir `numero`, `"->"` y `factorial(numero)`.
3. Llamar a `mostrar_factoriales(1, 5)`.

## Salida

```text
1 -> 1
2 -> 2
3 -> 6
4 -> 24
5 -> 120
```

## Restricciones

- `factorial` calcula con un bucle (no con una fórmula cerrada) y usa `return`.
- `mostrar_factoriales` **llama** a `factorial`; no repite el cálculo.
- Identificadores y comentarios en español.

## Dificultad

Avanzado

## Resultados de aprendizaje

- RA-5: escribir funciones reutilizables y modulares.
- RA-7: descomponer un problema en varias funciones y combinarlas.
