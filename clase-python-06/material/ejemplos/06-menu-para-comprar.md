# 💡 Ejemplo 06 — Menú para comprar

## 🧩 Problema

Una tienda quiere un pequeño programa que muestre su catálogo de productos y permita
"comprar" un producto y una cantidad, avisando con un mensaje claro si la cantidad no
es un número o si el producto no existe, en vez de detenerse con un error.

## 🔍 Análisis

- **Entrada**: el catálogo vive en un módulo propio (`producto -> precio`); se prueban
  tres compras: una válida (`"pan"`, `"2"`), una con cantidad inválida (`"pan"`,
  `"dos"`), y una con producto inexistente (`"queso"`, `"1"`).
- **Proceso**: mostrar el catálogo iterando sobre él; para cada compra, convertir la
  cantidad a número y buscar el precio del producto, manejando ambos posibles errores.
- **Salida**: el catálogo completo, y el resultado de cada intento de compra.

## 💡 Solución

El módulo `catalogo.py` guarda los productos y sus precios, y expone
`mostrar_catalogo()` y `buscar_precio(producto)`. El script principal importa el
módulo, muestra el catálogo, y define `comprar(producto, cantidad_texto)` con
`try`/`except`/`else`/`finally` para manejar la cantidad inválida (`ValueError`) y el
producto inexistente (`KeyError`).

## 💻 Código

Archivo `catalogo.py` (el módulo):

```python
"""Modulo con el catalogo de productos de la tienda."""

PRODUCTOS = {
    "manzana": 800,
    "pan": 1500,
    "leche": 1200,
}


def mostrar_catalogo():
    """Muestra el catalogo completo, un producto por linea."""
    print("Catalogo disponible:")
    for producto in PRODUCTOS:
        print(f"- {producto}: ${PRODUCTOS[producto]}")


def buscar_precio(producto):
    """Devuelve el precio de producto o lanza KeyError si no existe."""
    return PRODUCTOS[producto]
```

Archivo `principal.py` (el script que usa el módulo):

```python
import catalogo


def comprar(producto, cantidad_texto):
    print(f"\nIntentando comprar: {cantidad_texto} de '{producto}'")
    try:
        cantidad = int(cantidad_texto)
        precio_unitario = catalogo.buscar_precio(producto)
    except ValueError:
        print(f"'{cantidad_texto}' no es una cantidad valida")
    except KeyError:
        print(f"El producto '{producto}' no esta en el catalogo")
    else:
        total = cantidad * precio_unitario
        print(f"Compra realizada: {cantidad} x {producto} = ${total}")
    finally:
        print("Fin del intento de compra")


catalogo.mostrar_catalogo()

comprar("pan", "2")
comprar("pan", "dos")
comprar("queso", "1")
```

## 🧭 Explicación paso a paso

1. `catalogo.py` es un módulo propio: guarda los datos (`PRODUCTOS`) y las funciones
   relacionadas con ellos, separado del script principal (Modularidad, RA-2).
2. `catalogo.mostrar_catalogo()` recorre `PRODUCTOS` con `for producto in PRODUCTOS:`,
   es decir, iterando sobre el diccionario (RA-3/RA-4).
3. Dentro de `comprar()`, el `try` agrupa las dos operaciones que pueden fallar: la
   conversión de la cantidad (`int(cantidad_texto)`) y la búsqueda del precio
   (`catalogo.buscar_precio(producto)`).
4. Si la cantidad no es numérica, `int()` lanza `ValueError`; si el producto no existe
   en `PRODUCTOS`, `buscar_precio()` lanza `KeyError` al indexar el diccionario. Cada
   una se captura por separado, con un mensaje distinto (RA-5).
5. Cuando ambas operaciones tienen éxito, no se lanza ninguna excepción: se ejecuta el
   `else`, que calcula y muestra el total de la compra (RA-6).
6. El `finally` se ejecuta siempre, en los tres casos, mostrando que el intento de
   compra terminó.

## ✅ Resultado esperado

```text
Catalogo disponible:
- manzana: $800
- pan: $1500
- leche: $1200

Intentando comprar: 2 de 'pan'
Compra realizada: 2 x pan = $3000
Fin del intento de compra

Intentando comprar: dos de 'pan'
'dos' no es una cantidad valida
Fin del intento de compra

Intentando comprar: 1 de 'queso'
El producto 'queso' no esta en el catalogo
Fin del intento de compra
```
