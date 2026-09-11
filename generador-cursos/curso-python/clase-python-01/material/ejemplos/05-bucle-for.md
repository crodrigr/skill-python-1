# Ejemplo 05 — Bucle `for`

**Tema**: repetición con un número conocido de vueltas; patrón acumulador ·
**Resultados de aprendizaje**: RA-6, RA-7 · **Nivel**: intermedio-avanzado (quinto de la secuencia)

## Problema

Una tienda registró las ventas (en pesos) de los primeros 5 días de la semana. Con esos
valores fijos en el código, el programa debe mostrar el total vendido y el promedio
diario.

## Análisis

- **Entrada**: 5 montos de venta. En este ejemplo los recorremos con `range` sumando un
  monto fijo por día para mantenerlo simple; el foco es el bucle.
- **Proceso**: repetir 5 veces (número **conocido** → `for`), acumulando la suma.
- **Salida**: total y promedio.

## Solución

Usamos un `for` con `range(1, 6)` para las 5 vueltas y una variable **acumuladora**
`total_ventas` que empieza en 0 y crece en cada vuelta. Al final dividimos entre 5.

## Código

```python
# Venta de cada día: 10000 el día 1, 20000 el día 2, ... (dia * 10000)
dias = 5
total_ventas = 0

for dia in range(1, dias + 1):
    venta_del_dia = dia * 10000
    total_ventas = total_ventas + venta_del_dia
    print("Día", dia, "- venta:", venta_del_dia)

promedio = total_ventas / dias

print("Total de la semana:", total_ventas)
print("Promedio diario:", promedio)
```

## Explicación paso a paso

1. `total_ventas = 0`: la acumuladora parte en cero.
2. `range(1, 6)` produce `1, 2, 3, 4, 5`. La variable `dia` toma uno de esos valores en
   cada vuelta.
3. En cada vuelta: `venta_del_dia = dia * 10000` y luego
   `total_ventas = total_ventas + venta_del_dia`.
   - Vuelta 1: `total_ventas` pasa de `0` a `10000`.
   - Vuelta 2: de `10000` a `30000`. … Vuelta 5: de `100000` a `150000`.
4. Al salir del bucle, `promedio = 150000 / 5` → `30000.0`.
5. Elegimos `for` (no `while`) porque sabíamos de antemano que eran **5** vueltas.

## Resultado esperado

```text
Día 1 - venta: 10000
Día 2 - venta: 20000
Día 3 - venta: 30000
Día 4 - venta: 40000
Día 5 - venta: 50000
Total de la semana: 150000
Promedio diario: 30000.0
```
