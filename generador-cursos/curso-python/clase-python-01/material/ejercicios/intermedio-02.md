# Intermedio 02 — Descuento por monto

## Problema

Una tienda aplica un descuento sobre el total de la compra según el monto:

- Menos de $20.000: sin descuento.
- De $20.000 a $49.999: 10% de descuento.
- De $50.000 en adelante: 20% de descuento.

Escribe un programa que, a partir del monto de la compra, calcule el descuento aplicado
(en pesos) y el total a pagar.

## Entrada

- `monto` (`int`), fijado en el código.

## Proceso esperado

1. Determinar el porcentaje de descuento con `if` / `elif` / `else`.
2. Calcular el descuento en pesos: `monto * porcentaje / 100`.
3. Calcular el total a pagar: `monto - descuento`.

## Salida

Dos líneas. Ejemplo, para `monto = 50000`:

```text
Descuento: 10000.0
Total a pagar: 40000.0
```

## Restricciones

- Usa operadores aritméticos y de comparación.
- El porcentaje de descuento debe quedar en una variable antes de calcular el monto del
  descuento.
- Identificadores y comentarios en español.

## Dificultad

Intermedio

## Resultados de aprendizaje

- RA-4: usar operadores aritméticos y de comparación respetando la precedencia.
- RA-5: usar estructuras condicionales para tomar decisiones.
