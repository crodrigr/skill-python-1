# 🔑 Soluciones de los ejercicios — Clase 04

> **Material docente.** No entregar al estudiantado antes de la puesta en común. Todo el
> código se ejecuta sin errores con Python 3.10 o superior.

Cada solución incluye el código, una explicación breve y el resultado esperado ya
verificado ejecutando el programa.

---

## 🟢 Básico 01 — Agenda de contactos

### 💻 Código

```python
agenda = {"Ana": "555-1234", "Luis": "555-5678", "Eva": "555-9012"}

agenda["Marco"] = "555-3456"
agenda["Ana"] = "555-0000"

print("Agenda final:", agenda)
print("Cantidad de contactos:", len(agenda))
```

### 📖 Explicación

`agenda["Marco"] = "555-3456"` agrega una clave nueva porque `"Marco"` no existía.
`agenda["Ana"] = "555-0000"` modifica el valor de `"Ana"`, que ya existía; el
diccionario sigue teniendo cuatro contactos, no cinco.

### ✅ Resultado esperado

```text
Agenda final: {'Ana': '555-0000', 'Luis': '555-5678', 'Eva': '555-9012', 'Marco': '555-3456'}
Cantidad de contactos: 4
```

### 🔎 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada.

---

## 🟢 Básico 02 — Consultas sobre un diccionario de capitales

### 💻 Código

```python
capitales = {"Chile": "Santiago", "Perú": "Lima", "Argentina": "Buenos Aires"}

print("Cantidad de países registrados:", len(capitales))
print("¿Está Bolivia?:", "Bolivia" in capitales)
print("Capital de Perú:", capitales.get("Perú", "Desconocida"))
print("Capital de Bolivia:", capitales.get("Bolivia", "Desconocida"))
```

### 📖 Explicación

`len` cuenta los tres países; `in` comprueba la pertenencia de la clave `"Bolivia"`
(`False`, no está); `get("Perú", ...)` encuentra el valor porque la clave existe;
`get("Bolivia", ...)` devuelve el valor por defecto `"Desconocida"` porque la clave no
existe, sin lanzar `KeyError`.

### ✅ Resultado esperado

```text
Cantidad de países registrados: 3
¿Está Bolivia?: False
Capital de Perú: Lima
Capital de Bolivia: Desconocida
```

### 🔎 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada.

---

## 🟡 Intermedio 01 — Depurar una lista de tareas pendientes

### 💻 Código

```python
tareas_pendientes = {
    "lavar el auto": "baja",
    "pagar cuentas": "alta",
    "estudiar Python": "media",
    "llamar al dentista": "media",
}

prioridad_pagar_cuentas = tareas_pendientes.pop("pagar cuentas")
print("Prioridad de 'pagar cuentas':", prioridad_pagar_cuentas)

resultado_ejercicio = tareas_pendientes.pop("hacer ejercicio", "no encontrada")
print("Resultado al buscar 'hacer ejercicio':", resultado_ejercicio)

del tareas_pendientes["lavar el auto"]

print("Tareas pendientes finales:", tareas_pendientes)
```

### 📖 Explicación

`pop("pagar cuentas")` elimina esa clave y devuelve su prioridad (`"alta"`).
`pop("hacer ejercicio", "no encontrada")` no encuentra la clave, pero como se dio un
valor por defecto, no falla: devuelve `"no encontrada"`. `del` elimina
`"lavar el auto"` sin devolver nada. Al final solo quedan dos tareas.

### ✅ Resultado esperado

```text
Prioridad de 'pagar cuentas': alta
Resultado al buscar 'hacer ejercicio': no encontrada
Tareas pendientes finales: {'estudiar Python': 'media', 'llamar al dentista': 'media'}
```

### 🔎 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada.

---

## 🟡 Intermedio 02 — Reporte de calificaciones

### 💻 Código

```python
calificaciones = {"Ana": 6.5, "Luis": 3.8, "Eva": 5.0}
calificaciones_nuevas = {"Eva": 7.0, "Marco": 4.5}

calificaciones.update(calificaciones_nuevas)

aprobados = 0
for nombre, nota in calificaciones.items():
    if nota >= 4.0:
        estado = "Aprobado"
        aprobados += 1
    else:
        estado = "Reprobado"
    print(nombre + ":", nota, "-", estado)

print("Total de aprobados:", aprobados)
```

### 📖 Explicación

`update` corrige la nota de `"Eva"` (de `5.0` a `7.0`) y agrega a `"Marco"`. El bucle
recorre `items()` desempaquetando nombre y nota, decide el estado con un `if`, y suma
`1` al acumulador `aprobados` cada vez que la nota alcanza `4.0`.

### ✅ Resultado esperado

```text
Ana: 6.5 - Aprobado
Luis: 3.8 - Reprobado
Eva: 7.0 - Aprobado
Marco: 4.5 - Aprobado
Total de aprobados: 3
```

### 🔎 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada.

---

## 🔴 Avanzado 01 — Agrupar palabras por su letra inicial

### 💻 Código

```python
palabras = ["python", "perro", "casa", "carro", "banana", "barco", "python"]

palabras_por_letra = {}
for palabra in palabras:
    letra_inicial = palabra[0]
    palabras_por_letra.setdefault(letra_inicial, [])
    palabras_por_letra[letra_inicial].append(palabra)

print(palabras_por_letra)
```

### 📖 Explicación

`setdefault(letra_inicial, [])` asegura que exista una lista vacía la primera vez que
aparece una letra; las veces siguientes no la reinicia, porque la clave ya existe.
`append` agrega la palabra a la lista de su letra en cada vuelta, incluida la
repetición de `"python"`.

### ✅ Resultado esperado

```text
{'p': ['python', 'perro', 'python'], 'c': ['casa', 'carro'], 'b': ['banana', 'barco']}
```

### 🔎 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada.

---

## 🔴 Avanzado 02 — De lista de tuplas a diccionario

### 💻 Código

```python
registros = [("Ana", 6.5), ("Luis", 3.8), ("Eva", 5.0), ("Ana", 7.0)]

calificaciones = {}
for nombre, nota in registros:
    calificaciones[nombre] = nota

# La segunda tupla de Ana reemplaza el valor de la primera: las claves de un
# diccionario son únicas, así que solo queda la nota más reciente (7.0).
print("Calificaciones:", calificaciones)

print("Nota de Marco:", calificaciones.get("Marco", "sin registro"))
```

### 📖 Explicación

El bucle recorre cada tupla `(nombre, nota)` y la usa para asignar
`calificaciones[nombre] = nota`; cuando `"Ana"` aparece una segunda vez, la asignación
simplemente reemplaza su valor anterior (`6.5`) por el nuevo (`7.0`), sin duplicar la
clave. `"Marco"` nunca apareció en `registros`, así que `get` devuelve el valor por
defecto.

### ✅ Resultado esperado

```text
Calificaciones: {'Ana': 7.0, 'Luis': 3.8, 'Eva': 5.0}
Nota de Marco: sin registro
```

### 🔎 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada.

---

## 🏆 Desafío 01 — Inscripciones a los talleres de un evento

### 💻 Código

```python
inscripciones = [
    ("Ana", "Yoga"),
    ("Luis", "Pilates"),
    ("Eva", "Yoga"),
    ("Ana", "Pilates"),
    ("Marco", "Yoga"),
    ("Eva", "Yoga"),
]

# Un diccionario es la estructura adecuada para contar inscripciones por taller: cada
# taller es un identificador con sentido (su nombre), no una posición.
conteo_por_taller = {}
for nombre, taller in inscripciones:
    conteo_por_taller[taller] = conteo_por_taller.get(taller, 0) + 1

print("Inscripciones por taller:", conteo_por_taller)

taller_mas_popular = None
mayor_conteo = 0
for taller, cantidad in conteo_por_taller.items():
    if cantidad > mayor_conteo:
        mayor_conteo = cantidad
        taller_mas_popular = taller

print("Taller más popular:", taller_mas_popular, "con", mayor_conteo, "inscripciones")

# Un conjunto es la estructura adecuada para las personas distintas: solo interesa
# quién está, sin asociarle ningún valor ni conservar repeticiones u orden.
nombres = []
for nombre, taller in inscripciones:
    nombres.append(nombre)

personas_distintas = set(nombres)
print("Personas distintas inscritas:", len(personas_distintas))
```

### 📖 Explicación

El primer bucle cuenta cada inscripción (tupla) sumándola al conteo de su taller,
incluida la de Eva repetida en Yoga (4 inscripciones, no 3). El segundo bucle recorre
el conteo ya construido para encontrar el máximo. El conjunto `personas_distintas`
elimina automáticamente los duplicados de nombre, dando 4 personas distintas aunque
haya 6 inscripciones en total.

### ✅ Resultado esperado (caso del enunciado)

```text
Inscripciones por taller: {'Yoga': 4, 'Pilates': 2}
Taller más popular: Yoga con 4 inscripciones
Personas distintas inscritas: 4
```

### 🔎 Verificación

Ejecutado con Python 3.10+ para los dos casos de prueba del enunciado (el de 6
registros con una repetición, y el de una sola inscripción); ambos coinciden con la
salida esperada.

---

## 🛠️ Taller 01 — Gestor de inventario de una tienda

### 💻 Código (`gestor_inventario.py`)

```python
# Paso 1: inventario inicial
inventario = {"lápices": 50, "cuadernos": 20}

# Paso 2: agregar y actualizar
inventario["gomas"] = 30

# Paso 3: eliminar un producto agotado, guardando la cantidad que tenía
cantidad_cuadernos = inventario.pop("cuadernos")
print("Cuadernos tenía en stock:", cantidad_cuadernos)


def registrar_venta(inventario_actual, producto):
    """Registra la entrada de una unidad de 'producto', creándolo en 0 si es nuevo."""
    inventario_actual.setdefault(producto, 0)
    inventario_actual[producto] += 1


# Paso 5: registrar la venta de un producto que todavía no estaba en el inventario
registrar_venta(inventario, "marcadores")

# Paso 4: reporte final
print("Reporte final:")
for producto, cantidad in inventario.items():
    print(producto + ":", cantidad)
```

### 📖 Explicación

`inventario["gomas"] = 30` agrega el producto nuevo por asignación. `pop("cuadernos")`
elimina el producto agotado y devuelve la cantidad que tenía, que se muestra antes de
continuar. `registrar_venta` usa `setdefault` para que un producto nunca antes visto
(`"marcadores"`) se inicialice en `0` sin lanzar `KeyError`, y luego le suma una unidad.
El reporte final recorre el inventario con `items()`.

### ✅ Resultado esperado (caso del enunciado)

```text
Cuadernos tenía en stock: 20
Reporte final:
lápices: 50
gomas: 30
marcadores: 1
```

### 🔎 Verificación

Ejecutado con Python 3.10+; la salida coincide exactamente con la documentada en el
caso de prueba del taller.
