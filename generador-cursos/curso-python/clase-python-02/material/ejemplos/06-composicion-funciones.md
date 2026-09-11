# Ejemplo 06 — Composición de funciones

**Tema**: descomponer un problema en varias funciones; una función usa el resultado de
otra · **Resultados de aprendizaje**: RA-7 · **Nivel**: intermedio-avanzado (último de la
secuencia)

## Problema

Una tienda calcula el **total a pagar** de una compra: primero el subtotal (precio por
cantidad) y luego un descuento porcentual sobre ese subtotal. Queremos resolverlo con
piezas pequeñas y reutilizables, no con una fórmula larga.

## Análisis

- **Entrada**: precio unitario, cantidad y porcentaje de descuento.
- **Proceso**: (1) subtotal = precio × cantidad; (2) total = subtotal − descuento.
- **Salida**: el total a pagar.

## Solución

1. `subtotal(precio_unitario, cantidad)` — devuelve el costo sin descuento.
2. `con_descuento(monto, porcentaje)` — devuelve un monto tras aplicarle un descuento.
3. `total_a_pagar(...)` — **combina** las dos anteriores: pasa el resultado de `subtotal`
   como argumento de `con_descuento`.

## Código

```python
def subtotal(precio_unitario, cantidad):
    """Devuelve el costo de 'cantidad' unidades."""
    return precio_unitario * cantidad

def con_descuento(monto, porcentaje):
    """Devuelve 'monto' tras aplicarle un descuento porcentual entero."""
    descuento = monto * porcentaje // 100
    return monto - descuento

def total_a_pagar(precio_unitario, cantidad, porcentaje):
    """Combina el subtotal y el descuento para obtener el total."""
    return con_descuento(subtotal(precio_unitario, cantidad), porcentaje)

print("Total:", total_a_pagar(1000, 3, 10))
print("Total:", total_a_pagar(2500, 2, 0))
```

## Explicación paso a paso

1. En `total_a_pagar(1000, 3, 10)` se evalúa primero `subtotal(1000, 3)` → `3000`.
2. Ese `3000` se pasa como primer argumento a `con_descuento(3000, 10)`.
3. `con_descuento` calcula `descuento = 3000 * 10 // 100` = `300` y devuelve
   `3000 - 300` = `2700`.
4. Ese valor es lo que devuelve `total_a_pagar`, y `print` lo muestra.
5. En la segunda llamada, `porcentaje` es `0`: `subtotal(2500, 2)` = `5000` y el
   descuento es `0`, así que el total es `5000`.

Ninguna función repite el trabajo de otra: cada una hace su parte y `total_a_pagar` solo
las **coordina**. Este es el método para el [Desafío 01](../ejercicios/desafio-01.md) y el
[Taller 01](../../actividades/talleres/taller-01.md).

## Resultado esperado

```text
Total: 2700
Total: 5000
```
