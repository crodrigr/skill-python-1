# 🔑 Clave del Quiz 01 — Clase 05

> **Material docente.** No entregar al estudiantado. Referencia rápida:
> 1-B · 2-B · 3-B · 4-B · 5-B · 6→"Fin\n" · 7→Clave no configurada/Programa terminado ·
> 8-B · 9→falta try/except · 10→programa

---

## 1️⃣ Respuesta: **B**

Una variable vive solo en la memoria mientras el programa se ejecuta; un archivo queda
guardado en el disco y sigue existiendo después de que el programa termina. Ninguna de
las otras opciones describe correctamente para qué sirve un archivo.

_RA: RA-1_

---

## 2️⃣ Respuesta: **B**

`with` cierra el archivo automáticamente al salir del bloque, incluso si ocurre un
error dentro. Con `open()`/`close()` manual, un error entre ambas líneas dejaría el
archivo sin cerrar porque `close()` nunca se ejecutaría.

_RA: RA-2_

---

## 3️⃣ Respuesta: **B**

`readlines()` devuelve una lista con cada línea del archivo como un elemento separado.
`read()` (no `readlines()`) devuelve todo como un solo texto; `readline()` devuelve una
sola línea.

_RA: RA-3_

---

## 4️⃣ Respuesta: **B**

El modo `'w'` sobrescribe el archivo por completo al abrirlo, sin aviso previo. Para
conservar el contenido anterior y agregar algo nuevo se necesita el modo `'a'`.

_RA: RA-4_

---

## 5️⃣ Respuesta: **B**

`try`/`except` anticipa un error posible: si ocurre dentro del bloque `try`, Python
salta al bloque `except` correspondiente en vez de detener el programa con una traza de
error.

_RA: RA-6_

---

## 6️⃣ `registro.txt` queda con `"Fin\n"`

La primera apertura en `'w'` crea el archivo con `"Inicio\n"`. La apertura en `'a'`
agrega `"Proceso\n"` sin borrar lo anterior, dejando `"Inicio\nProceso\n"`. La tercera
apertura, de nuevo en `'w'`, **sobrescribe todo** el contenido anterior y deja el
archivo solo con `"Fin\n"`.

_RA: RA-4_

---

## 7️⃣ Imprime `Clave no configurada` y luego `Programa terminado`

Como `"clave.txt"` no existe, `open("clave.txt", "r")` lanza `FileNotFoundError` dentro
del `try`; Python salta de inmediato al `except`, que imprime
`"Clave no configurada"`. El programa continúa con normalidad después del bloque
`try`/`except`, así que también se imprime `"Programa terminado"`.

_RA: RA-6_

---

## 8️⃣ Respuesta: **B**

`readline()` devuelve `"10,20,30\n"`; `strip()` quita el salto de línea, dejando
`"10,20,30"`; `split(",")` la divide en `['10', '20', '30']`, una lista de 3 elementos.

_RA: RA-3, RA-5_

---

## 9️⃣ Error: no se maneja el caso de que el archivo no exista

`open("perfil.txt", "r")` lanza `FileNotFoundError` si el archivo no existe, y como no
hay ningún `try`/`except` alrededor, el programa se detiene. La corrección es envolver
la apertura y lectura en `try`/`except FileNotFoundError`:

```python
try:
    with open("perfil.txt", "r") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("No se encontró el archivo de perfil.")
```

_RA: RA-6_

---

## 🔟 Solución de referencia

```python
archivo_encontrado = True
try:
    with open("pedidos.txt", "r") as archivo:
        lineas = archivo.readlines()
except FileNotFoundError:
    archivo_encontrado = False
    print("No se encontró el archivo de pedidos.")

if archivo_encontrado:
    total = 0
    for linea in lineas:
        producto, cantidad_texto = linea.strip().split(",")
        total = total + int(cantidad_texto)

    with open("total_pedidos.txt", "w") as archivo:
        archivo.write("Total: " + str(total) + "\n")

    print("Total:", total)
```

Con `pedidos.txt` conteniendo `"lápiz,4\ncuaderno,2\nborrador,10\n"`, salida esperada:

```text
Total: 16
```

y `total_pedidos.txt` con:

```text
Total: 16
```

**Criterios de corrección**:

| Elemento | Presente en la solución |
|----------|--------------------------|
| Manejo de `FileNotFoundError` | bloque `try`/`except` alrededor de la lectura |
| Mensaje claro si el archivo no existe | `print("No se encontró el archivo de pedidos.")` |
| Suma correcta de cantidades | `int(cantidad_texto)` acumulado en `total` |
| Escritura del resultado | `total_pedidos.txt` con el formato `"Total: <suma>"` |

Se acepta cualquier variante equivalente (por ejemplo, usar una función en vez de una
variable de control), siempre que maneje `FileNotFoundError` con `try`/`except` y
calcule el total correctamente.

_RA: RA-6, RA-7_
