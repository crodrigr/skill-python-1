# Ejemplo 07 — Tuplas y desempaquetado

**Tema**: creación de tuplas, acceso por índice, desempaquetado e inmutabilidad ·
**Resultado de aprendizaje**: RA-8 · **Nivel**: intermedio

## Problema

Se quiere registrar la ubicación de un punto en un mapa como un par de coordenadas
`(x, y)` que no debe modificarse una vez creado, acceder a cada coordenada por separado
y desempaquetarlas en dos variables con nombre.

## Análisis

- **Entrada**: dos números que representan `x` e `y`.
- **Proceso**: crear una tupla, acceder por índice, desempaquetarla en variables.
- **Salida**: los valores de `x` e `y` accedidos de las dos formas.

## Solución

1. Crear la tupla `(x, y)`.
2. Acceder a cada valor con `[0]` y `[1]`.
3. Desempaquetar la tupla en dos variables con nombre en una sola línea.

## Código

```python
coordenada = (10, 25)

# Acceso por índice
print("Coordenada completa:", coordenada)
print("x (índice 0):", coordenada[0])
print("y (índice 1):", coordenada[1])

# Desempaquetado en variables con nombre
x, y = coordenada
print("x desempaquetada:", x)
print("y desempaquetada:", y)

# coordenada[0] = 99   # si se descomenta esta línea, Python detiene el programa con:
                        # TypeError: 'tuple' object does not support item assignment
```

## Explicación paso a paso

1. `coordenada = (10, 25)` crea una tupla de dos elementos.
2. `coordenada[0]` y `coordenada[1]` acceden a cada valor exactamente igual que en una
   lista.
3. `x, y = coordenada` es el **desempaquetado**: Python asigna el primer elemento de la
   tupla a `x` y el segundo a `y`, en una sola línea. El número de variables a la
   izquierda debe coincidir con la cantidad de elementos de la tupla.
4. La línea comentada muestra qué pasaría al intentar modificar la tupla: las tuplas
   son **inmutables**, así que Python detiene el programa con
   `TypeError: 'tuple' object does not support item assignment` en vez de permitir el
   cambio.

## Resultado esperado

```text
Coordenada completa: (10, 25)
x (índice 0): 10
y (índice 1): 25
x desempaquetada: 10
y desempaquetada: 25
```
