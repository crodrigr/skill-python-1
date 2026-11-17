# 🔑 Soluciones de los ejercicios — Clase 03

> **Material docente.** No entregar al estudiantado antes de la puesta en común. Todo el
> código se ejecuta sin errores con Python 3.10 o superior.

Cada solución incluye el código, una explicación breve y el resultado esperado ya
verificado ejecutando el programa.

---

## 🟢 Básico 01 — Lista de compras

### 💻 Código

```python
productos = ["arroz", "aceite", "leche"]

productos.append("pan")
productos.insert(1, "azúcar")
productos.remove("aceite")

indice_leche = productos.index("leche")
productos[indice_leche] = "leche descremada"

print("Lista final:", productos)
print("Cantidad de productos:", len(productos))
```

### 📖 Explicación

- `append("pan")` agrega al final; `insert(1, "azúcar")` inserta en la posición 1,
  desplazando el resto.
- `remove("aceite")` quita ese valor donde esté.
- `index("leche")` ubica la posición actual de `"leche"` (cambió tras el `insert`) antes
  de reemplazarla por índice.

### ✅ Resultado esperado

```text
Lista final: ['arroz', 'azúcar', 'leche descremada', 'pan']
Cantidad de productos: 4
```

### 🔎 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada.

---

## 🟢 Básico 02 — Consultas sobre una lista de edades

### 💻 Código

```python
edades = [15, 22, 15, 30, 18, 22, 22]

print("Cantidad total de edades:", len(edades))
print("¿Está 40?:", 40 in edades)
print("Primera posición de 22:", edades.index(22))
print("Veces que se repite 22:", edades.count(22))
```

### 📖 Explicación

`len` cuenta los siete elementos; `40 in edades` es `False` porque ese valor no está;
`index(22)` da `1` (primera aparición); `count(22)` da `3` (aparece en las posiciones
1, 5 y 6).

### ✅ Resultado esperado

```text
Cantidad total de edades: 7
¿Está 40?: False
Primera posición de 22: 1
Veces que se repite 22: 3
```

### 🔎 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada.

---

## 🟡 Intermedio 01 — Ranking de un videojuego

### 💻 Código

```python
resultados = [("Nico", 1200), ("Dani", 3400), ("Sofi", 2100), ("Max", 3400)]


def obtener_puntaje(registro):
    """Devuelve el puntaje (segundo valor) de un registro (nombre, puntaje)."""
    return registro[1]


ranking = sorted(resultados, key=obtener_puntaje, reverse=True)

for posicion in range(len(ranking)):
    nombre, puntaje = ranking[posicion]
    print(str(posicion + 1) + ". " + nombre + " - " + str(puntaje) + " puntos")

destacados = []
for nombre, puntaje in ranking:
    if puntaje > 2000:
        destacados.append(nombre)

print("Superaron los 2000 puntos:", destacados)
```

### 📖 Explicación

`sorted(..., key=obtener_puntaje, reverse=True)` ordena los registros de mayor a menor
puntaje. El bucle `for posicion in range(len(ranking))` numera el ranking desde 1. El
segundo bucle recorre el ranking ya ordenado y construye `destacados` con quienes
superaron 2000 puntos (Dani y Max empatan en 3400: ambos quedan antes que Sofi, en el
orden en que aparecían en `resultados`, porque `sorted` es estable).

### ✅ Resultado esperado

```text
1. Dani - 3400 puntos
2. Max - 3400 puntos
3. Sofi - 2100 puntos
4. Nico - 1200 puntos
Superaron los 2000 puntos: ['Dani', 'Max', 'Sofi']
```

### 🔎 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada.

---

## 🟡 Intermedio 02 — Ingredientes de varias recetas

### 💻 Código

```python
receta_ensalada = ("Ensalada", ["lechuga", "tomate", "cebolla", "aceite"])
receta_sandwich = ("Sándwich", ["pan", "jamón", "queso", "tomate", "aceite"])

nombre_1, ingredientes_1 = receta_ensalada
nombre_2, ingredientes_2 = receta_sandwich

set_ensalada = set(ingredientes_1)
set_sandwich = set(ingredientes_2)

print("Ingredientes en común:", sorted(set_ensalada & set_sandwich))
print("Todos los ingredientes necesarios:", sorted(set_ensalada | set_sandwich))
```

### 📖 Explicación

El desempaquetado `nombre_1, ingredientes_1 = receta_ensalada` separa el nombre de la
receta de su lista de ingredientes. `set(...)` convierte cada lista en un conjunto;
`&` da los ingredientes presentes en ambas recetas y `|` da la unión de todos, sin
repetir. `sorted(...)` ordena el resultado para una salida predecible.

### ✅ Resultado esperado

```text
Ingredientes en común: ['aceite', 'tomate']
Todos los ingredientes necesarios: ['aceite', 'cebolla', 'jamón', 'lechuga', 'pan', 'queso', 'tomate']
```

### 🔎 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada.

---

## 🔴 Avanzado 01 — Corregir un ordenamiento por selección (versión corregida)

### 💻 Código

```python
numeros = [7, 2, 9, 1, 5]
cantidad = len(numeros)

for pasada in range(cantidad - 1):
    posicion_minimo = pasada
    for posicion in range(pasada + 1, cantidad):
        if numeros[posicion] < numeros[posicion_minimo]:
            posicion_minimo = posicion   # CORRECCIÓN: recordar la nueva posición mínima
    numeros[pasada], numeros[posicion_minimo] = numeros[posicion_minimo], numeros[pasada]

print(numeros)
```

### 📖 Explicación

El error del código de partida era no actualizar `posicion_minimo` dentro del bucle
interior, por lo que el intercambio final no hacía nada. La corrección agrega
`posicion_minimo = posicion` cada vez que se encuentra un valor menor que el mínimo
registrado hasta el momento; al terminar el bucle interior, `posicion_minimo` apunta a
la posición real del menor elemento restante, y el intercambio sí reordena la lista.

### ✅ Resultado esperado

```text
[1, 2, 5, 7, 9]
```

### 🔎 Verificación

Ejecutado con Python 3.10+; la salida coincide con la documentada (a diferencia del
código de partida, que imprimía `[7, 2, 9, 1, 5]` sin cambios).

---

## 🔴 Avanzado 02 — Etiquetas de productos por categoría

### 💻 Código

```python
productos = [
    ("Zapatillas", "Deporte", ["running", "cómodo", "unisex"]),
    ("Balón", "Deporte", ["fútbol", "cómodo"]),
    ("Mochila", "Viaje", ["resistente", "unisex"]),
]

categorias = set()
for producto in productos:
    nombre, categoria, etiquetas = producto
    categorias.add(categoria)

for categoria_actual in sorted(categorias):
    etiquetas_categoria = set()
    for producto in productos:
        nombre, categoria, etiquetas = producto
        if categoria == categoria_actual:
            for etiqueta in etiquetas:
                etiquetas_categoria.add(etiqueta)
    print(categoria_actual + ":", sorted(etiquetas_categoria))
```

### 📖 Explicación

El primer bucle construye el conjunto de categorías distintas. El bucle exterior del
segundo bloque recorre esas categorías (ordenadas); el bucle interior recorre todos los
productos, y cuando la categoría coincide, un **tercer** bucle (anidado dentro del
interior) agrega cada etiqueta del producto a `etiquetas_categoria`. Al ser un conjunto,
las etiquetas repetidas (como `"cómodo"` o `"unisex"`) quedan una sola vez.

### ✅ Resultado esperado

```text
Deporte: ['cómodo', 'fútbol', 'running', 'unisex']
Viaje: ['resistente', 'unisex']
```

### 🔎 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada.

---

## 🏆 Desafío 01 — Organizador de una carrera de atletismo

### 💻 Código

```python
resultados = [
    ("Camila", 62.4),
    ("Tomás", 58.9),
    ("Valeria", 60.1),
    ("Camila", 62.4),
    ("Benjamín", 57.3),
    ("Diego", 65.0),
    ("Diego", 65.0),
]


def obtener_tiempo(registro):
    """Devuelve el tiempo (segundo valor) de un registro (nombre, tiempo)."""
    return registro[1]


# Elección: cada resultado es una tupla (nombre, tiempo) porque es un registro fijo;
# el ordenamiento se hace con sorted() y key porque el objetivo es obtener un resultado
# ordenado para el podio, no comprender el mecanismo de ordenamiento.
ordenados = sorted(resultados, key=obtener_tiempo)
podio = ordenados[:3]

print("Podio:")
for posicion in range(len(podio)):
    nombre, tiempo = podio[posicion]
    print(str(posicion + 1) + ". " + nombre + " - " + str(tiempo) + " s")

# Elección: un conjunto para contar corredores distintos, porque no interesa el orden
# ni la cantidad de repeticiones, solo si un nombre está o no está.
nombres = []
for nombre, tiempo in resultados:
    nombres.append(nombre)

nombres_unicos = set(nombres)
print("Corredores distintos:", len(nombres_unicos))
```

### 📖 Explicación

Se justifican dos decisiones de diseño: (1) tupla para cada resultado individual,
porque nombre y tiempo no deben cambiar una vez registrados; (2) `sorted` con `key`
para el podio, porque la tarea es obtener un resultado (no comprender el algoritmo), y
un conjunto para contar corredores distintos, porque los duplicados de registro
("Camila" y "Diego" aparecen dos veces) no deben contarse dos veces.

### ✅ Resultado esperado

```text
Podio:
1. Benjamín - 57.3 s
2. Tomás - 58.9 s
3. Valeria - 60.1 s
Corredores distintos: 5
```

### 🔎 Verificación

Ejecutado con Python 3.10+ para los dos casos de prueba del enunciado (el de 7
registros con duplicados, y el de 2 corredores sin duplicados); ambos coinciden con la
salida esperada.

---

## 🛠️ Taller 01 — Gestor de calificaciones de un curso

### 💻 Código (`gestor_calificaciones.py`)

```python
# Paso 1: registros iniciales como tuplas (nombre, nota)
calificaciones = [
    ("Ana", 6.5),
    ("Luis", 3.8),
    ("Eva", 5.0),
    ("Ana", 6.5),  # Ana quedó registrada dos veces por error
]

# Paso 2: agregar, eliminar y modificar
calificaciones.append(("Marco", 4.5))
calificaciones.remove(("Luis", 3.8))
indice_eva = calificaciones.index(("Eva", 5.0))
calificaciones[indice_eva] = ("Eva", 7.0)


def obtener_nota(registro):
    """Devuelve la nota (segundo valor) de un registro (nombre, nota)."""
    return registro[1]


def obtener_nombre(registro):
    """Devuelve el nombre (primer valor) de un registro (nombre, nota)."""
    return registro[0]


# Paso 3: ordenar por nota (descendente) y por nombre
por_nota = sorted(calificaciones, key=obtener_nota, reverse=True)
por_nombre = sorted(calificaciones, key=obtener_nombre)

print("Por nota (de mayor a menor):", por_nota)
print("Por nombre (alfabético):", por_nombre)

# Paso 4: estadísticas con funciones integradas
notas = []
for nombre, nota in calificaciones:
    notas.append(nota)

aprobados = 0
for nota in notas:
    if nota >= 4.0:
        aprobados += 1

print("Cantidad de aprobados:", aprobados)
print("Nota máxima:", max(notas))
print("Nota mínima:", min(notas))
print("Promedio:", sum(notas) / len(notas))

# Paso 5: nombres únicos de aprobados
aprobados_unicos = set()
for nombre, nota in calificaciones:
    if nota >= 4.0:
        aprobados_unicos.add(nombre)

print("Aprobados únicos:", sorted(aprobados_unicos))
```

### 📖 Explicación

Cada estudiante es una tupla `(nombre, nota)`: inmutable, para que una corrección de
nota (paso 2) se haga reemplazando el registro completo por índice, no "editando" la
tupla. `sorted` con `key=obtener_nota`/`key=obtener_nombre` resuelve los dos
ordenamientos sin escribir un algoritmo a mano. Las estadísticas usan `max`, `min` y
`sum` sobre la lista de notas extraída de los registros. El conjunto final evita contar
dos veces a "Ana", que quedó registrada por error en dos tuplas idénticas.

### ✅ Resultado esperado (caso del enunciado)

```text
Por nota (de mayor a menor): [('Eva', 7.0), ('Ana', 6.5), ('Ana', 6.5), ('Marco', 4.5)]
Por nombre (alfabético): [('Ana', 6.5), ('Ana', 6.5), ('Eva', 7.0), ('Marco', 4.5)]
Cantidad de aprobados: 4
Nota máxima: 7.0
Nota mínima: 4.5
Promedio: 6.125
Aprobados únicos: ['Ana', 'Eva', 'Marco']
```

### 🔎 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada en el
caso de prueba del taller.
