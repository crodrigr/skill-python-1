# Ejemplo 01 — Crear listas, indexar y rebanar

**Tema**: creación de listas, indexación positiva/negativa y rebanado · **Resultado de
aprendizaje**: RA-2 · **Nivel**: introductorio (primero de la secuencia)

## Problema

Una tienda de barrio quiere registrar los precios de los cinco productos que más vende
en un solo lugar, poder consultar el precio de un producto por su posición (incluida la
posición del último producto sin contar cuántos hay) y obtener rápidamente los precios
de los tres primeros productos.

## Análisis

- **Entrada**: los cinco precios, en el orden en que se venden más (`int`).
- **Proceso**: guardarlos en una sola estructura; acceder por índice positivo y
  negativo; obtener una porción con rebanado.
- **Salida**: el primer precio, el último precio y los tres primeros precios.

## Solución

1. Crear una lista con los cinco precios, en orden.
2. Acceder al primer elemento con índice `0` y al último con índice `-1`.
3. Obtener los tres primeros con rebanado `lista[:3]`.

## Código

```python
# Precios de los cinco productos más vendidos, ordenados de mayor a menor venta
precios_mas_vendidos = [2500, 1800, 3200, 990, 4700]

# Acceso por índice positivo y negativo
primer_precio = precios_mas_vendidos[0]
ultimo_precio = precios_mas_vendidos[-1]

# Rebanado: los tres primeros precios
tres_mas_vendidos = precios_mas_vendidos[:3]

print("Cantidad de productos registrados:", len(precios_mas_vendidos))
print("Precio del más vendido:", primer_precio)
print("Precio del quinto más vendido:", ultimo_precio)
print("Precios de los tres más vendidos:", tres_mas_vendidos)
```

## Explicación paso a paso

1. `precios_mas_vendidos = [2500, 1800, 3200, 990, 4700]` crea una lista de cinco
   enteros; el índice `0` corresponde a `2500` y el índice `4` (o `-1`) a `4700`.
2. `precios_mas_vendidos[0]` accede al primer elemento sin necesidad de saber cuántos
   hay en total.
3. `precios_mas_vendidos[-1]` accede al último elemento contando desde el final; es
   equivalente a `precios_mas_vendidos[4]`, pero funciona aunque la lista cambie de
   tamaño.
4. `precios_mas_vendidos[:3]` es un rebanado: toma los elementos desde el índice `0`
   (incluido) hasta el índice `3` (excluido), es decir, las posiciones `0`, `1` y `2`.
   Devuelve una lista **nueva**; la original no se modifica.
5. `len(precios_mas_vendidos)` cuenta cuántos elementos tiene la lista.

## Resultado esperado

```text
Cantidad de productos registrados: 5
Precio del más vendido: 2500
Precio del quinto más vendido: 4700
Precios de los tres más vendidos: [2500, 1800, 3200]
```
