# 🔑 Soluciones de los ejercicios — Clase 05

> **Material docente.** No entregar al estudiantado antes de la puesta en común. Todo el
> código se ejecuta sin errores con Python 3.10 o superior.

Cada solución incluye el código, una explicación breve y el resultado esperado
(consola y, cuando corresponde, el contenido del archivo) ya verificado ejecutando el
programa.

---

## 🟢 Básico 01 — Guardar y mostrar una lista de compras

### 💻 Código

```python
with open("compras.txt", "w") as archivo:
    archivo.write("arroz\naceite\nleche\n")

with open("compras.txt", "r") as archivo:
    print(archivo.read())
```

### 📖 Explicación

La primera apertura crea `compras.txt` con los tres productos, uno por línea. La
segunda lo vuelve a abrir, ahora para lectura, y `read()` devuelve todo el contenido tal
como quedó guardado.

### ✅ Resultado esperado

```text
arroz
aceite
leche

```

**Archivo `compras.txt` resultante**:

```text
arroz
aceite
leche
```

### 🔍 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada.

---

## 🟢 Básico 02 — Bitácora de un viaje

### 💻 Código

```python
with open("bitacora.txt", "w") as archivo:
    archivo.write("Día 1: Salida desde la ciudad\n")

with open("bitacora.txt", "a") as archivo:
    archivo.write("Día 2: Llegada al primer destino\n")

with open("bitacora.txt", "a") as archivo:
    archivo.write("Día 3: Regreso\n")

with open("bitacora.txt", "r") as archivo:
    print(archivo.read())
```

### 📖 Explicación

Solo la primera escritura usa `'w'` (crea el archivo); las dos siguientes usan `'a'`
para agregar sin borrar lo anterior. Al leer al final, las tres líneas aparecen en
orden.

### ✅ Resultado esperado

```text
Día 1: Salida desde la ciudad
Día 2: Llegada al primer destino
Día 3: Regreso

```

### 🔍 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada.

---

## 🟡 Intermedio 01 — Separar nombre y precio

### 💻 Código

```python
with open("productos.txt", "w") as archivo:
    archivo.write("arroz,1200\naceite,3500\nazúcar,950\n")

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    nombre, precio = linea.strip().split(",")
    print(nombre + " cuesta " + precio)
```

### 📖 Explicación

Cada línea se limpia con `strip()` antes de dividirla con `split(",")`, para no
arrastrar el salto de línea en ninguna de las dos partes obtenidas.

### ✅ Resultado esperado

```text
arroz cuesta 1200
aceite cuesta 3500
azúcar cuesta 950
```

### 🔍 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada.

---

## 🟡 Intermedio 02 — Contar líneas y palabras

### 💻 Código

```python
with open("parrafo.txt", "w") as archivo:
    archivo.write("Python es un lenguaje de programación\nSe usa para análisis de datos y automatización\nAprenderlo abre muchas puertas\n")

with open("parrafo.txt", "r") as archivo:
    lineas = archivo.readlines()

print("Cantidad de líneas:", len(lineas))

total_palabras = 0
for linea in lineas:
    palabras = linea.split()
    total_palabras = total_palabras + len(palabras)

print("Cantidad total de palabras:", total_palabras)
```

### 📖 Explicación

`len(lineas)` cuenta directamente las líneas de la lista. Para las palabras,
`split()` sin argumento separa cada línea por espacios; se suma la cantidad de
palabras de cada línea a un acumulador.

### ✅ Resultado esperado

```text
Cantidad de líneas: 3
Cantidad total de palabras: 18
```

### 🔍 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada.

---

## 🔴 Avanzado 01 — Calificaciones que podrían no existir

### 💻 Código

```python
def leer_calificaciones(ruta):
    """Muestra cada calificación del archivo, o un mensaje si no existe."""
    try:
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        print("No se encontró el archivo de calificaciones.")
        return

    for linea in lineas:
        nombre, nota = linea.strip().split(",")
        print(nombre + ": " + nota)


# Primer intento: el archivo todavía no existe
leer_calificaciones("calificaciones.txt")

# Se crea el archivo y se vuelve a intentar
with open("calificaciones.txt", "w") as archivo:
    archivo.write("Ana,6.5\nLuis,3.8\nEva,7.0\n")

leer_calificaciones("calificaciones.txt")
```

### 📖 Explicación

La primera llamada falla al abrir el archivo (todavía no existe), así que
`FileNotFoundError` se captura y se muestra el mensaje de aviso, sin detener el
programa. Después de crear el archivo, la segunda llamada sí encuentra el archivo y
muestra las tres calificaciones.

### ✅ Resultado esperado

```text
No se encontró el archivo de calificaciones.
Ana: 6.5
Luis: 3.8
Eva: 7.0
```

### 🔍 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada en los
dos casos (archivo ausente y luego presente).

---

## 🔴 Avanzado 02 — Resumen de gastos por categoría

### 💻 Código

```python
with open("gastos.txt", "w") as archivo:
    archivo.write("comida,15000\ntransporte,8000\ncomida,5000\nocio,12000\ntransporte,3000\n")

with open("gastos.txt", "r") as archivo:
    lineas = archivo.readlines()

total_por_categoria = {}
for linea in lineas:
    categoria, monto_texto = linea.strip().split(",")
    monto = int(monto_texto)
    total_por_categoria[categoria] = total_por_categoria.get(categoria, 0) + monto

with open("resumen_gastos.txt", "w") as archivo:
    for categoria, total in total_por_categoria.items():
        archivo.write(categoria + ":" + str(total) + "\n")

print(total_por_categoria)
```

### 📖 Explicación

Cada línea se limpia y se divide para obtener categoría y monto; `int(...)` convierte
el monto a número. `total_por_categoria.get(categoria, 0)` inicializa en `0` la
primera vez que aparece una categoría y acumula el monto en las siguientes, igual que
el patrón de conteo visto en la Clase 04.

### ✅ Resultado esperado

```text
{'comida': 20000, 'transporte': 11000, 'ocio': 12000}
```

**Archivo `resumen_gastos.txt` resultante**:

```text
comida:20000
transporte:11000
ocio:12000
```

### 🔍 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada.

---

## 🏆 Desafío 01 — Registro de asistencia a un curso

### 💻 Código

```python
def procesar_asistencia(ruta_entrada, ruta_reporte):
    """Genera un reporte de asistencia, o avisa si el archivo no existe."""
    archivo_encontrado = True
    try:
        with open(ruta_entrada, "r") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        archivo_encontrado = False
        print("No se encontró el archivo de asistencia '" + ruta_entrada + "'.")

    if archivo_encontrado:
        presentes = 0
        ausentes = 0
        for linea in lineas:
            nombre, presente = linea.strip().split(",")
            if presente == "si":
                presentes = presentes + 1
            else:
                ausentes = ausentes + 1

        total = presentes + ausentes
        porcentaje = presentes / total * 100

        with open(ruta_reporte, "w") as archivo:
            archivo.write("Presentes: " + str(presentes) + "\n")
            archivo.write("Ausentes: " + str(ausentes) + "\n")
            archivo.write("Porcentaje de asistencia: " + str(porcentaje) + "%\n")

        print("Presentes:", presentes)
        print("Ausentes:", ausentes)
        print("Porcentaje de asistencia:", porcentaje, "%")


# Caso 1: el archivo existe
registros = [("Ana", "si"), ("Luis", "no"), ("Eva", "si"), ("Marco", "si"), ("Sofía", "no")]
with open("asistencia.txt", "w") as archivo:
    for nombre, presente in registros:
        archivo.write(nombre + "," + presente + "\n")

procesar_asistencia("asistencia.txt", "reporte_asistencia.txt")

# Caso 2: el archivo no existe
procesar_asistencia("otro_curso.txt", "reporte_asistencia.txt")
```

### 📖 Explicación

`archivo_encontrado` decide si el resto de la función se ejecuta: si `open` falla con
`FileNotFoundError`, se marca en `False` y se avisa, sin generar un reporte con datos
inventados (FR de la spec de esta clase, restricción explícita del ejercicio). Si el
archivo sí se leyó, se cuentan presentes y ausentes recorriendo las líneas, se calcula
el porcentaje, y se escribe el reporte.

### ✅ Resultado esperado (caso 1: archivo presente)

```text
Presentes: 3
Ausentes: 2
Porcentaje de asistencia: 60.0 %
```

**Archivo `reporte_asistencia.txt` resultante**:

```text
Presentes: 3
Ausentes: 2
Porcentaje de asistencia: 60.0%
```

### ✅ Resultado esperado (caso 2: archivo ausente)

```text
No se encontró el archivo de asistencia 'otro_curso.txt'.
```

No se genera (ni se modifica) `reporte_asistencia.txt` en este caso: conserva el
reporte del caso 1.

### 🔍 Verificación

Ejecutado con Python 3.10+ para los dos casos de prueba del enunciado; ambos coinciden
con la salida esperada.

---

## 🛠️ Taller 01 — Registro de ventas de un día

### 💻 Código (`registro_ventas.py`)

```python
def generar_reporte_ventas(ruta_ventas, ruta_reporte):
    """Lee un archivo de ventas y escribe un reporte, o avisa si no existe."""
    archivo_encontrado = True
    try:
        with open(ruta_ventas, "r") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        archivo_encontrado = False
        print("No se encontró el archivo de ventas '" + ruta_ventas + "'.")

    if archivo_encontrado:
        cantidad_por_producto = {}
        total_general = 0
        for linea in lineas:
            producto, cantidad_texto, precio_texto = linea.strip().split(",")
            cantidad = int(cantidad_texto)
            precio = int(precio_texto)

            cantidad_por_producto[producto] = cantidad_por_producto.get(producto, 0) + cantidad
            total_general = total_general + cantidad * precio

        with open(ruta_reporte, "w") as archivo:
            for producto, cantidad_vendida in cantidad_por_producto.items():
                archivo.write(producto + ": " + str(cantidad_vendida) + " unidades\n")
            archivo.write("Total general: " + str(total_general) + "\n")

        print("Reporte de ventas:")
        for producto, cantidad_vendida in cantidad_por_producto.items():
            print(producto + ":", cantidad_vendida, "unidades")
        print("Total general:", total_general)


# Paso 1: crear el archivo de ventas del día
ventas = [("pan", 10, 1300), ("leche", 5, 1000), ("pan", 3, 1300), ("queso", 2, 3200)]
with open("ventas.txt", "w") as archivo:
    for producto, cantidad, precio in ventas:
        archivo.write(producto + "," + str(cantidad) + "," + str(precio) + "\n")

# Caso de prueba 1: el archivo existe
generar_reporte_ventas("ventas.txt", "reporte_ventas.txt")

# Caso de prueba 2: el archivo no existe
generar_reporte_ventas("ventas_de_ayer.txt", "reporte_ventas.txt")
```

### 📖 Explicación

`archivo_encontrado` evita que el resto de la función se ejecute si `ventas.txt` no
existe. Cuando el archivo sí existe, cada línea se limpia y se divide en producto,
cantidad y precio; `cantidad_por_producto.get(producto, 0)` acumula la cantidad vendida
de cada producto (patrón de conteo de la Clase 04), y `total_general` suma
`cantidad * precio` de cada línea. El reporte final se escribe recorriendo el
diccionario con `items()`.

### ✅ Resultado esperado (caso 1: archivo presente)

```text
Reporte de ventas:
pan: 13 unidades
leche: 5 unidades
queso: 2 unidades
Total general: 28300
```

**Archivo `reporte_ventas.txt` resultante**:

```text
pan: 13 unidades
leche: 5 unidades
queso: 2 unidades
Total general: 28300
```

### ✅ Resultado esperado (caso 2: archivo ausente)

```text
No se encontró el archivo de ventas 'ventas_de_ayer.txt'.
```

`reporte_ventas.txt` no se modifica en este caso: conserva el reporte del caso 1.

### 🔍 Verificación

Ejecutado con Python 3.10+ para los dos casos de prueba del taller; ambos coinciden
con la salida esperada.
