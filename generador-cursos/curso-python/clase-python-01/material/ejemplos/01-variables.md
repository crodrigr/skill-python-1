# Ejemplo 01 — Variables

**Tema**: variables, tipos de datos básicos y expresiones · **Resultado de aprendizaje**: RA-2
· **Nivel**: introductorio (primero de la secuencia)

## Problema

Una tienda vende cuadernos. Queremos un programa que, a partir del precio de un cuaderno
y de la cantidad comprada, calcule y muestre el total a pagar y un mensaje con el nombre
del cliente.

## Análisis

- **Entrada**: nombre del cliente (`str`), precio unitario del cuaderno (`int`),
  cantidad de cuadernos (`int`). En este ejemplo los fijamos en el código.
- **Proceso**: multiplicar precio unitario por cantidad.
- **Salida**: un mensaje con el nombre del cliente y el total a pagar.

## Solución

1. Crear una variable para cada dato de entrada, con un nombre descriptivo.
2. Calcular el total en una nueva variable usando el operador `*`.
3. Mostrar el resultado con `print`.

## Código

```python
# Datos de entrada (fijos en este ejemplo)
nombre_cliente = "Ana"
precio_unitario = 1200      # int: precio de un cuaderno en pesos
cantidad = 3                # int: cuántos cuadernos compra

# Proceso: calcular el total
total_a_pagar = precio_unitario * cantidad

# Salida
print("Cliente:", nombre_cliente)
print("Total a pagar:", total_a_pagar)
```

## Explicación paso a paso

1. `nombre_cliente = "Ana"` crea una variable de tipo `str` (texto entre comillas).
2. `precio_unitario = 1200` y `cantidad = 3` crean dos variables de tipo `int`.
3. `total_a_pagar = precio_unitario * cantidad` evalúa primero la parte derecha
   (`1200 * 3` = `3600`) y guarda ese valor en la nueva variable `total_a_pagar`.
4. Cada `print(...)` muestra en pantalla el texto y el valor de la variable, separados
   por un espacio.

## Resultado esperado

```text
Cliente: Ana
Total a pagar: 3600
```
