# 🛠️ Taller 01 — Menú para comprar

## 🎯 Objetivo

Construir un mini programa de menú para comprar en una tienda, combinando un módulo
propio con el catálogo, la iteración para mostrarlo, y el manejo de errores con
`try`/`except`/`else`/`finally` ante entradas inválidas. Ejercita RA-2, RA-3, RA-4,
RA-5, RA-6 y RA-7.

## 🌍 Contexto

Una tienda genérica tiene un catálogo de productos con su precio. Se quiere un pequeño
programa de menú que muestre el catálogo (definido en un módulo propio) y permita
"comprar" un producto y una cantidad, avisando con un mensaje claro si la cantidad no
es un número o si el producto no existe, en vez de detenerse con un error.

## 🪜 Pasos

1. Crear un módulo propio `catalogo.py` con un diccionario `producto -> precio` y
   funciones para mostrar el catálogo completo y buscar el precio de un producto por
   su nombre.
2. Importar `catalogo` desde el script principal (con o sin alias, a tu elección).
3. Mostrar el catálogo completo iterando sobre él (con `for` o, si quieres practicar
   más, con `iter()`/`next()`).
4. Pedir un producto y una cantidad; convertir la cantidad a número dentro de un
   `try`/`except ValueError`, y buscar el producto manejando el caso de que no exista
   (`except KeyError` o una validación equivalente).
5. Usar `else` para calcular y mostrar el total de la compra cuando no hubo ningún
   error, y `finally` para mostrar un mensaje de cierre que se vea siempre.

## 📦 Entregable

Dos archivos Python: `catalogo.py` (el módulo con el catálogo) y el script principal
que lo importa, muestra el catálogo, pide la compra y maneja los errores descritos.

## 🧪 Casos de prueba

| Situación | Resultado esperado |
|-----------|----------------------|
| Producto existente y cantidad numérica válida | Se muestra el total de la compra (cantidad × precio) y el mensaje de cierre |
| Cantidad no numérica (por ejemplo, texto en vez de un número) | Mensaje claro de cantidad inválida, sin detener el programa con un error sin manejar, y el mensaje de cierre igual se muestra |
| Producto que no está en el catálogo | Mensaje claro de producto no encontrado, sin detener el programa con un error sin manejar, y el mensaje de cierre igual se muestra |

## 📏 Criterios de evaluación

- El catálogo vive en un módulo propio (`catalogo.py`) importado correctamente desde
  el script principal.
- El catálogo se muestra iterando sobre él (con `for` o con `iter()`/`next()`).
- La cantidad se valida con `try`/`except ValueError`.
- El producto inexistente se maneja sin detener el programa (`except KeyError` o
  validación equivalente).
- El total de la compra solo se calcula y muestra si no hubo error (`else`), y el
  mensaje de cierre se muestra siempre (`finally`).
