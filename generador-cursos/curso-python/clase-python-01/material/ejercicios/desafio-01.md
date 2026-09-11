# Desafío 01 — Cajero de billetes

## Problema

Un cajero automático entrega dinero usando la **menor cantidad de billetes** posible,
con billetes de `20000`, `10000`, `5000`, `2000` y `1000` pesos. El monto solicitado
siempre es múltiplo de `1000`.

Escribe un programa que, dado un monto, muestre cuántos billetes de cada tipo entrega y
el total de billetes.

Este desafío se resuelve en cuatro pasos: **analizar** el problema, **diseñar el
algoritmo**, **escribir el programa** y **probarlo** con los casos de prueba dados.

## Entrada

- `monto` (`int`, múltiplo de 1000, mayor o igual a 0), fijado en el código.

## Proceso esperado

1. Para cada tipo de billete, de mayor a menor valor:
   - calcular cuántos billetes caben en el monto restante (`monto // valor_billete`),
   - restar ese dinero del monto restante (`monto % valor_billete`).
2. Ir acumulando el total de billetes entregados.

Se recomienda diseñar primero el algoritmo en pseudocódigo y luego traducirlo. Puede
resolverse repitiendo el mismo razonamiento para cada billete (con o sin bucle).

## Salida

Una línea por tipo de billete con cantidad distinta de cero, y una línea final con el
total. Ejemplo para `monto = 47000`:

```text
Billetes de 20000: 2
Billetes de 5000: 1
Billetes de 2000: 1
Total de billetes: 4
```

## Restricciones

- El resultado debe usar la menor cantidad de billetes posible.
- No mostrar los tipos de billete cuya cantidad sea `0`.
- Deben combinarse operadores (`//`, `%`, `+`) con al menos una estructura de control.
- Identificadores y comentarios en español.

## Dificultad

Desafío

## Casos de prueba

| `monto` | Salida esperada |
|---------|-----------------|
| `47000` | `Billetes de 20000: 2` · `Billetes de 5000: 1` · `Billetes de 2000: 1` · `Total de billetes: 4` |
| `1000` | `Billetes de 1000: 1` · `Total de billetes: 1` |
| `0` | `Total de billetes: 0` |
| `38000` | `Billetes de 20000: 1` · `Billetes de 10000: 1` · `Billetes de 5000: 1` · `Billetes de 2000: 1` · `Billetes de 1000: 1` · `Total de billetes: 5` |

## Resultados de aprendizaje

- RA-3: analizar un problema (entrada/proceso/salida) y expresarlo como algoritmo antes
  de programar.
- RA-8: combinar operadores y estructuras de control.
- RA-9: escribir y ejecutar un programa que resuelve el problema y probarlo con casos.
