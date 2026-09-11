# Intermedio 01 — Función con decisión

## Problema

Escribe una función `es_aprobado(nota, minimo)` que reciba la nota de un estudiante y la
nota mínima de aprobación, y **devuelva** el texto `"Aprobado"` si la nota alcanza el
mínimo o `"Reprobado"` en caso contrario.

En el programa principal, imprime el resultado para `es_aprobado(65, 60)` y
`es_aprobado(40, 60)`.

## Entrada

- `nota` (`int`): la nota obtenida.
- `minimo` (`int`): la nota mínima para aprobar.

## Proceso esperado

1. Definir `es_aprobado(nota, minimo)` con dos parámetros.
2. Con `if`, comparar `nota` con `minimo`.
3. Devolver `"Aprobado"` o `"Reprobado"` con `return`.
4. En el programa principal, imprimir las dos llamadas.

## Salida

```text
Aprobado
Reprobado
```

## Restricciones

- La función devuelve un texto con `return`; no imprime.
- Usa una estructura condicional dentro de la función.
- Identificadores y comentarios en español.

## Dificultad

Intermedio

## Resultados de aprendizaje

- RA-3: usar varios parámetros para recibir datos.
- RA-4: devolver un valor con `return`.
- RA-5: escribir una función reutilizable en varias llamadas.
