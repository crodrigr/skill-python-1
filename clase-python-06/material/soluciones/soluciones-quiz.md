# 🔑 Soluciones — Quiz 01 (Clase 06)

Material docente. No compartir con el estudiante.

**1.** Respuesta: **B**. Modularizar organiza el código en partes coherentes, facilita
mantenerlo y permite reutilizarlo desde otros programas; no es una restricción de
Python ni afecta la velocidad de ejecución.

**2.** Respuesta: **B**. Un módulo se importa completo con `import`, y para traer solo
un elemento con un nombre distinto se usa `from modulo import elemento as alias`.
`from operaciones import sumar as add` cumple exactamente eso.

**3.** Respuesta: **B**. `collections.deque` es una colección optimizada para agregar
y quitar elementos eficientemente por ambos extremos (principio y final).

**4.** Respuesta: **C**. `StopIteration` es la excepción que indica que un iterador ya
entregó todos sus elementos.

**5.** Respuesta: **C**. `except:` sin tipo captura cualquier excepción, incluidas las
que no anticipamos, lo que puede ocultar errores reales del programa en vez de
ayudarnos a manejarlos.

**6.** La tercera llamada `print(next(iterador))` lanza `StopIteration`, porque el
iterador ya entregó los dos únicos elementos de la `deque` (`"x"` y `"y"`) en las dos
llamadas anteriores. Como el código no captura esa excepción con `try`/`except`, el
programa se detiene mostrando la traza del error `StopIteration`.

**7.** Se imprime, en este orden:

```text
B
D
```

`10 / 0` lanza `ZeroDivisionError` (no `ValueError`), por lo que se ejecuta el segundo
`except` (imprime `"B"`). El `else` se salta porque sí hubo una excepción. El `finally`
se ejecuta siempre, al final (imprime `"D"`).

**8.** Se imprimen, en este orden:

```text
Cantidad invalida
Fin del intento
```

`int("dos")` lanza `ValueError` de inmediato, antes de llegar a
`catalogo.buscar_precio("pan")` (esa línea nunca se ejecuta). Se captura con
`except ValueError`, y el `finally` se ejecuta siempre.

**9.** El problema es que `except:` sin tipo captura **cualquier** excepción de forma
genérica: si `int(entrada)` falla por `ValueError` o si `catalogo.buscar_precio(...)`
falla por `KeyError`, ambos casos muestran el mismo mensaje genérico "Ocurrio un
error", sin distinguir cuál fue el problema real ni permitir un mensaje específico
para cada uno. La corrección es usar cláusulas `except` separadas y con tipo:

```python
try:
    cantidad = int(entrada)
    precio = catalogo.buscar_precio(producto)
except ValueError:
    print("Cantidad invalida")
except KeyError:
    print("Producto no encontrado")
```

**10.** Ejemplo de solución válida:

```python
texto = "7"

try:
    numero = int(texto)
except ValueError:
    print("Valor invalido")
else:
    print("Numero convertido:", numero)
```

Cualquier solución equivalente es válida si: (a) usa `try`/`int(texto)`, (b) captura
`ValueError` y muestra exactamente el mensaje `"Valor invalido"` cuando la conversión
falla, y (c) muestra el número convertido dentro de un bloque `else` cuando la
conversión tiene éxito.
