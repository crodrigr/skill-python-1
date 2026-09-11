# ❓ Quiz 01 — Módulos y manejo de excepciones

Sin respuestas. Las soluciones están en `material/soluciones/soluciones-quiz.md`.

**1. [seleccion_multiple]**
¿Cuál es la razón principal para dividir un programa grande en varios módulos en vez
de escribirlo todo en un solo archivo?

| Opción | Respuesta |
|---|---|
| A | Porque Python obliga a usar más de un archivo a partir de cierto tamaño |
| B | Para organizar el código en partes coherentes, facilitar su mantenimiento y poder reutilizarlo |
| C | Porque los archivos `.py` no pueden superar cierto número de líneas |
| D | Para que el programa se ejecute más rápido |

_RA: RA-1_

---

**2. [seleccion_multiple]**
Un módulo `operaciones.py` define una función `sumar`. ¿Cuál línea importa **solo**
esa función y le asigna el nombre `add` en el script principal?

| Opción | Respuesta |
|---|---|
| A | `import operaciones as add` |
| B | `from operaciones import sumar as add` |
| C | `import operaciones.sumar as add` |
| D | `from operaciones import add as sumar` |

_RA: RA-2_

---

**3. [seleccion_multiple]**
¿Qué es `collections.deque`?

| Opción | Respuesta |
|---|---|
| A | Una lista inmutable que no se puede modificar |
| B | Una colección optimizada para agregar y quitar elementos por ambos extremos |
| C | Una estructura que solo cuenta elementos repetidos |
| D | Un tipo especial de número entero |

_RA: RA-3_

---

**4. [seleccion_multiple]**
¿Qué excepción lanza `next(iterador)` cuando el iterador ya se agotó?

| Opción | Respuesta |
|---|---|
| A | `ValueError` |
| B | `IndexError` |
| C | `StopIteration` |
| D | `KeyError` |

_RA: RA-4_

---

**5. [seleccion_multiple]**
¿Cuál es el principal problema de escribir `except:` sin indicar un tipo de
excepción?

| Opción | Respuesta |
|---|---|
| A | Python no permite esa sintaxis |
| B | Solo funciona dentro de funciones |
| C | Atrapa cualquier error, incluso los que no anticipamos, y puede ocultar bugs reales |
| D | Es más lento de ejecutar que un `except` con tipo |

_RA: RA-5_

---

**6. [analisis_codigo]**
Analiza el siguiente código:

```python
cola = collections.deque(["x", "y"])
iterador = iter(cola)
print(next(iterador))
print(next(iterador))
print(next(iterador))
```

¿Qué ocurre al ejecutar la tercera línea `print(next(iterador))`? Explica por qué.

_RA: RA-4_

---

**7. [analisis_codigo]**
Analiza el siguiente código y describe, en orden, todo lo que se imprime en consola:

```python
try:
    resultado = 10 / 0
except ValueError:
    print("A")
except ZeroDivisionError:
    print("B")
else:
    print("C")
finally:
    print("D")
```

_RA: RA-5, RA-6_

---

**8. [identificacion_resultado]**
Dado este fragmento (parte de un programa de menú para comprar), con
`catalogo.buscar_precio("pan")` devolviendo `1500`:

```python
try:
    cantidad = int("dos")
    precio = catalogo.buscar_precio("pan")
except ValueError:
    print("Cantidad invalida")
except KeyError:
    print("Producto no encontrado")
else:
    print("Compra realizada")
finally:
    print("Fin del intento")
```

¿Qué dos líneas se imprimen, en qué orden?

_RA: RA-6, RA-7_

---

**9. [correccion_errores]**
El siguiente código intenta manejar dos errores distintos, pero tiene un problema.
Identifícalo y explica cómo corregirlo:

```python
try:
    cantidad = int(entrada)
    precio = catalogo.buscar_precio(producto)
except:
    print("Ocurrio un error")
```

_RA: RA-5_

---

**10. [problema_breve]**
Escribe un programa breve que dentro de un `try` convierta un texto a entero
(`int(texto)`) y, si la conversión falla, muestre el mensaje `"Valor invalido"`
capturando el tipo de excepción correcto; si la conversión tiene éxito, muestra el
número convertido usando un bloque `else`.

_RA: RA-2, RA-5_
