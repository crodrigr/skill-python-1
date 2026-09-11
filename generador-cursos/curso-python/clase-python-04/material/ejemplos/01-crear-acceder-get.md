# 💡 Ejemplo 01 — Crear un diccionario, acceder y usar get

**Tema**: creación de diccionarios, acceso por clave y manejo de clave inexistente con
`get` · **Resultado de aprendizaje**: RA-2, RA-3 · **Nivel**: introductorio (primero de
la secuencia)

## 🧩 Problema

Una tienda quiere registrar el precio de tres productos en un solo lugar, consultar el
precio de un producto por su nombre, y evitar que el programa se detenga si alguien
pregunta por el precio de un producto que todavía no tiene precio registrado.

## 🔍 Análisis

- **Entrada**: nombre y precio de tres productos (`str` → `int`).
- **Proceso**: crear un diccionario `nombre_producto -> precio`; acceder a un precio
  conocido; consultar un producto que no está, usando `get` con un valor por defecto.
- **Salida**: el precio de un producto conocido y el resultado de consultar uno que no
  está registrado.

## 💡 Solución

1. Crear el diccionario con los tres productos y sus precios.
2. Acceder al precio de un producto conocido con `[clave]`.
3. Consultar un producto que no está usando `get(clave, valor_por_defecto)`.

## 💻 Código

```python
# Precios registrados por nombre de producto
precios = {"pan": 1200, "leche": 950, "huevos": 2600}

# Acceso directo a un producto que sí está registrado
precio_pan = precios["pan"]
print("Precio del pan:", precio_pan)

# Consulta de un producto que podría no estar registrado
precio_queso = precios.get("queso", 0)
print("Precio del queso:", precio_queso)

print("¿Hay precio para el pan?:", "pan" in precios)
print("¿Hay precio para el queso?:", "queso" in precios)
```

## 🧭 Explicación paso a paso

1. `precios = {"pan": 1200, "leche": 950, "huevos": 2600}` crea un diccionario con tres
   pares clave-valor: cada nombre de producto es la clave, y su precio es el valor.
2. `precios["pan"]` accede directamente al valor asociado a la clave `"pan"`; como esa
   clave sí existe, devuelve `1200` sin error.
3. `precios.get("queso", 0)` busca la clave `"queso"`; como no existe, devuelve el
   valor por defecto `0` en vez de detener el programa con `KeyError`.
4. `"pan" in precios` y `"queso" in precios` comprueban la pertenencia de una clave sin
   acceder a su valor: la primera es `True`, la segunda es `False`.

## ✅ Resultado esperado

```text
Precio del pan: 1200
Precio del queso: 0
¿Hay precio para el pan?: True
¿Hay precio para el queso?: False
```
