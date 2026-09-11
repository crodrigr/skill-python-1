# Básico 02 — Conversión de temperatura

## Problema

Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit
y también indique si esa temperatura corresponde a "bajo cero" mostrando el valor
booleano de la comparación.

La fórmula es: `fahrenheit = celsius * 9 / 5 + 32`.

## Entrada

- `celsius`: número con decimales (`float`), fijado en el código.

## Proceso esperado

1. Guardar la temperatura en Celsius en una variable.
2. Calcular la temperatura en Fahrenheit con la fórmula (respeta la precedencia: primero
   `*` y `/`, luego `+`).
3. Calcular la expresión de comparación `celsius < 0`.

## Salida

Dos líneas. Por ejemplo, para `celsius = 25.0`:

```text
25.0 °C equivalen a 77.0 °F
¿Está bajo cero?: False
```

## Restricciones

- Usa variables, operadores aritméticos y un operador de comparación.
- No uses estructuras condicionales (`if`): la segunda línea muestra directamente el
  resultado de la comparación.
- Identificadores y comentarios en español.

## Dificultad

Básico

## Resultados de aprendizaje

- RA-2: usar variables, tipos de datos y expresiones.
- RA-4: usar operadores aritméticos y de comparación, respetando la precedencia.
