# Intermedio 02 — Función con varias condiciones

## Problema

Escribe una función `clasificar_imc(peso, altura)` que calcule el índice de masa corporal
(IMC = `peso / (altura * altura)`) y **devuelva** una categoría:

- `"bajo"` si el IMC es menor que `18.5`;
- `"normal"` si el IMC es menor que `25`;
- `"alto"` en cualquier otro caso.

En el programa principal, imprime el resultado para `clasificar_imc(50, 1.70)` y
`clasificar_imc(80, 1.75)`.

## Entrada

- `peso` (`int` o `float`): peso en kilogramos.
- `altura` (`float`): altura en metros.

## Proceso esperado

1. Definir `clasificar_imc(peso, altura)` con dos parámetros.
2. Calcular el IMC en una variable local.
3. Con `if` / `elif` / `else`, decidir la categoría y devolverla con `return`.
4. En el programa principal, imprimir las dos llamadas.

## Salida

```text
bajo
alto
```

## Restricciones

- El cálculo del IMC va **dentro** de la función.
- La función devuelve solo la categoría (un texto), con `return`.
- Identificadores y comentarios en español.

## Dificultad

Intermedio

## Resultados de aprendizaje

- RA-3: usar varios parámetros para recibir y procesar datos.
- RA-4: devolver un valor con `return`.
- RA-5: escribir una función modular y reutilizable.
