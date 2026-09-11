# 💡 Ejemplo 05 — Buscar y contar con funciones integradas

**Tema**: `in`, `index`, `count`, `min`, `max`, `sum` · **Resultado de aprendizaje**:
RA-5 · **Nivel**: intermedio

## 🧩 Problema

Un pequeño inventario guarda las cantidades vendidas de un producto durante seis días.
Se necesita saber: si hubo algún día con exactamente `0` ventas, en qué posición ocurrió
la primera vez, cuántos días se repitió esa cantidad, y el total, el mínimo y el máximo
de ventas del período.

## 🔍 Análisis

- **Entrada**: lista de ventas diarias (`int`).
- **Proceso**: comprobar pertenencia con `in`; ubicar con `index`; contar repeticiones
  con `count`; resumir con `min`, `max`, `sum`.
- **Salida**: si hubo un día sin ventas, su posición, cuántos días se repitió, y el
  resumen (mínimo, máximo, total).

## 💡 Solución

1. Usar `in` para comprobar si `0` está en la lista.
2. Si está, usar `index` para la primera posición y `count` para el total de
   repeticiones.
3. Usar `min`, `max` y `sum` sobre la lista completa.

## 💻 Código

```python
# Ventas diarias durante una semana de seis días hábiles
ventas = [12, 0, 8, 0, 15, 5]

hubo_dia_sin_ventas = 0 in ventas
print("¿Hubo un día sin ventas?:", hubo_dia_sin_ventas)

if hubo_dia_sin_ventas:
    primera_posicion = ventas.index(0)
    cantidad_dias = ventas.count(0)
    print("Primera vez en la posición:", primera_posicion)
    print("Cantidad de días sin ventas:", cantidad_dias)

print("Ventas mínimas:", min(ventas))
print("Ventas máximas:", max(ventas))
print("Total de ventas:", sum(ventas))
```

## 🧭 Explicación paso a paso

1. `0 in ventas` recorre la lista y devuelve `True` porque el valor `0` aparece dos
   veces.
2. Como `hubo_dia_sin_ventas` es `True`, se entra al bloque `if`.
3. `ventas.index(0)` devuelve `1`: la primera vez que aparece `0` es en la posición 1
   (segundo día).
4. `ventas.count(0)` devuelve `2`: el valor `0` aparece dos veces en la lista completa.
5. `min(ventas)`, `max(ventas)` y `sum(ventas)` recorren la lista para dar el menor
   valor, el mayor valor y la suma de todos, sin necesidad de escribir un bucle a mano.

## ✅ Resultado esperado

```text
¿Hubo un día sin ventas?: True
Primera vez en la posición: 1
Cantidad de días sin ventas: 2
Ventas mínimas: 0
Ventas máximas: 15
Total de ventas: 40
```
