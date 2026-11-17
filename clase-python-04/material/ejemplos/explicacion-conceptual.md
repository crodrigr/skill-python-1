# 📚 Explicación conceptual — Clase 04: Diccionarios

Este documento desarrolla, en orden pedagógico, los siete bloques temáticos de la clase.
Cada bloque sigue la secuencia **Contexto → Concepto → Explicación**. El lenguaje es
deliberadamente sencillo y solo supone lo visto en las Clases 01, 02 y 03 (variables,
tipos de datos básicos, operadores, condicionales, bucles, funciones, listas, tuplas y
conjuntos).

Convención de código: los nombres de variables, diccionarios y funciones, y los
comentarios están en español; solo las palabras reservadas de Python (`if`, `for`, `in`,
`del`, …) están en inglés porque forman parte del lenguaje.

---

## 1️⃣ Introducción a los diccionarios

**Resultado de aprendizaje**: RA-1.

### 🌍 Contexto

Con listas, tuplas y conjuntos ya sabemos guardar varios datos bajo un solo nombre y
acceder a ellos por posición (índice) o por pertenencia (`in`). Pero muchos datos del
mundo real no se identifican por su posición, sino por un **nombre o código propio**: el
precio de un producto se busca por su nombre, no por si es "el tercero de la lista"; una
palabra de un idioma se busca por la palabra misma, no por su posición en la página.

### 🧠 Concepto

Un **diccionario** es una colección de pares **clave-valor**: cada valor se guarda
asociado a una **clave** que sirve para encontrarlo directamente, sin recorrer nada.

```text
precios = {"pan": 1200, "leche": 950, "huevos": 2600}
           clave   valor   clave  valor   clave    valor
```

Es la misma idea que un diccionario de idioma: buscas una palabra (la clave) y obtienes
su definición (el valor), sin leer el libro entero desde el principio.

Comparación rápida con lo ya visto:

| Estructura | Se accede por... | Uso típico |
|------------|-------------------|------------|
| Lista | posición (índice) | una colección ordenada que cambia |
| Tupla | posición (índice) | un registro fijo |
| Conjunto | pertenencia (`in`) | valores únicos, sin importar el orden |
| **Diccionario** | **clave** | asociar un dato con un identificador con sentido |

### 📖 Explicación

**Cuándo conviene un diccionario.** Si los datos se identifican naturalmente por un
nombre, un código o cualquier otro identificador —y ese identificador es lo que se usa
para buscarlos—, un diccionario es la estructura adecuada. Ejemplos: precios por
producto, calificaciones por estudiante, capitales por país, configuración de un
programa (`{"volumen": 80, "brillo": 50}`).

Si, en cambio, el orden de llegada importa y no hay un identificador natural, sigue
conviniendo una lista; si el dato es un registro fijo con posiciones conocidas, una
tupla; si solo importa qué valores están presentes, sin asociarlos a nada más, un
conjunto. El resto de la clase desarrolla cómo crear, consultar, modificar, eliminar y
recorrer un diccionario, y cierra con un problema práctico que solo un diccionario
resuelve con naturalidad: contar cuántas veces aparece cada valor distinto en una
colección.

---

## 2️⃣ Crear diccionarios

**Resultado de aprendizaje**: RA-2.

**📎 Practicá esto**: [Ejemplo 01 — Crear un diccionario, acceder y usar get](01-crear-acceder-get.md) ·
[Básico 01](../ejercicios/basico-01.md).

### 🌍 Contexto

Antes de usar un diccionario hay que saber crearlo: vacío (para llenarlo después) o con
sus datos iniciales ya conocidos.

### 🧠 Concepto

Un diccionario se escribe entre llaves `{ }`, con pares `clave: valor` separados por
comas:

```python
precios = {"pan": 1200, "leche": 950, "huevos": 2600}
inventario_vacio = {}
```

También puede crearse con la función `dict()`:

```python
otro_diccionario = dict(pan=1200, leche=950)   # equivalente, con claves de texto simple
```

### 📖 Explicación

**Reglas sobre las claves.** Una clave debe ser de un tipo **inmutable** (texto,
número, tupla); no puede ser una lista ni otro diccionario. Las claves son **únicas**:
si se repite una clave al crear el diccionario, solo queda el último valor asignado a
esa clave.

```python
duplicado = {"pan": 1200, "pan": 1500}
print(duplicado)   # {'pan': 1500}  (solo queda el último valor)
```

**Los valores sí pueden repetirse** y ser de cualquier tipo (incluso listas u otros
diccionarios), a diferencia de las claves.

```python
stock = {"pan": 30, "leche": 30}   # el valor 30 se repite; no hay ningún problema
```

Desde Python 3.7, un diccionario **conserva el orden** en que se agregaron sus claves
(a diferencia de un conjunto, que no garantiza ningún orden).

---

## 3️⃣ Acceder a valores

**Resultado de aprendizaje**: RA-3.

**📎 Practicá esto**: [Ejemplo 01 — Crear un diccionario, acceder y usar get](01-crear-acceder-get.md) ·
[Básico 02](../ejercicios/basico-02.md).

### 🌍 Contexto

Una vez creado el diccionario, hace falta consultar sus valores. La forma directa
funciona bien si se está seguro de que la clave existe, pero en la práctica no siempre
es así: hay que saber qué pasa cuando se pregunta por una clave que no está.

### 🧠 Concepto

Se accede a un valor con `diccionario[clave]`:

```python
precios = {"pan": 1200, "leche": 950}
print(precios["pan"])   # 1200
```

Si la clave no existe, Python detiene el programa con un error:

```python
print(precios["huevos"])
# KeyError: 'huevos'
```

### 📖 Explicación

**Evitar el error de dos formas.** Primero, con `get(clave, valor_por_defecto)`, que
devuelve el valor si la clave existe, o el valor por defecto (sin lanzar error) si no
existe; si se omite el valor por defecto, `get` devuelve `None`:

```python
print(precios.get("huevos", 0))       # 0 (huevos no está; se usa el valor por defecto)
print(precios.get("pan", 0))          # 1200 (sí está)
```

Segundo, comprobando antes con `in`:

```python
if "huevos" in precios:
    print(precios["huevos"])
else:
    print("Ese producto no tiene precio registrado")
```

**Cuándo usar cada una.** `get` es más directo cuando se quiere un valor "de respaldo"
inmediato (por ejemplo, `0` para un conteo); `in` es más claro cuando las dos ramas
(existe / no existe) necesitan hacer cosas distintas.

---

## 4️⃣ Agregar y modificar

**Resultado de aprendizaje**: RA-4.

**📎 Practicá esto**: [Ejemplo 02 — Agregar y modificar elementos](02-agregar-modificar.md) ·
[Básico 01](../ejercicios/basico-01.md) ·
[Intermedio 02](../ejercicios/intermedio-02.md) ·
[Avanzado 02](../ejercicios/avanzado-02.md).

### 🌍 Contexto

Un diccionario casi nunca queda fijo desde el inicio: llegan claves nuevas que agregar
y valores que corregir. Python usa la misma operación —la asignación por clave— para
ambos casos.

### 🧠 Concepto

```python
precios = {"pan": 1200, "leche": 950}

precios["huevos"] = 2600     # agrega una clave nueva (no existía)
precios["pan"] = 1300        # modifica el valor de una clave que ya existía

print(precios)   # {'pan': 1300, 'leche': 950, 'huevos': 2600}
```

La regla es simple: si la clave **no existía**, `diccionario[clave] = valor` la agrega;
si la clave **ya existía**, la misma instrucción reemplaza su valor. Las claves son
únicas, así que nunca se duplica una clave por asignar dos veces.

### 📖 Explicación

**Actualizar varias claves a la vez con `update`.** Cuando hay que agregar o modificar
más de una clave, `update` evita escribir una asignación por cada una:

```python
nuevos_precios = {"leche": 1000, "queso": 3200}
precios.update(nuevos_precios)
print(precios)   # {'pan': 1300, 'leche': 1000, 'huevos': 2600, 'queso': 3200}
```

`update` agrega las claves que faltaban (`"queso"`) y actualiza las que ya existían
(`"leche"` pasó de `950` a `1000`), en una sola llamada. `update` **modifica** el
diccionario sobre el que se llama; no crea uno nuevo.

---

## 5️⃣ Eliminar elementos

**Resultado de aprendizaje**: RA-5.

**📎 Practicá esto**: [Ejemplo 03 — Eliminar con del, pop y popitem](03-eliminar-del-pop-popitem.md) ·
[Intermedio 01](../ejercicios/intermedio-01.md).

### 🌍 Contexto

Así como se agregan claves, también hay que poder quitarlas: un producto que se
descontinúa, un contacto que ya no corresponde. Python ofrece tres formas, según si se
necesita o no el valor que se está eliminando.

### 🧠 Concepto

```python
precios = {"pan": 1300, "leche": 1000, "huevos": 2600}

del precios["huevos"]           # elimina la clave; no devuelve nada
precio_leche = precios.pop("leche")   # elimina y DEVUELVE el valor eliminado
print(precio_leche)             # 1000
print(precios)                  # {'pan': 1300}
```

### 📖 Explicación

**Las tres formas de eliminar:**

| Operación | Qué hace | ¿Qué devuelve? | ¿Qué pasa si la clave no existe? |
|-----------|----------|------------------|-------------------------------------|
| `del diccionario[clave]` | elimina la clave | nada | `KeyError` |
| `diccionario.pop(clave)` | elimina la clave | el valor eliminado | `KeyError` |
| `diccionario.pop(clave, valor_por_defecto)` | elimina la clave si existe | el valor eliminado, o el valor por defecto | no lanza error |
| `diccionario.popitem()` | elimina el **último** par agregado | una tupla `(clave, valor)` | `KeyError` si el diccionario está vacío |

```python
# pop con valor por defecto: seguro aunque la clave no exista
precio_eliminado = precios.pop("queso", None)
print(precio_eliminado)   # None (no existía "queso")

ultimo_par = precios.popitem()
print(ultimo_par)          # ('pan', 1300) — el único par que quedaba
```

**`pop` frente a `del`**: usar `pop` cuando el valor eliminado todavía sirve para algo
(por ejemplo, mostrarlo o sumarlo a un total); usar `del` cuando solo interesa quitar la
clave.

---

## 6️⃣ Iterar diccionarios

**Resultado de aprendizaje**: RA-6.

**📎 Practicá esto**: [Ejemplo 04 — Iterar con keys, values e items](04-iterar-keys-values-items.md) ·
[Intermedio 02](../ejercicios/intermedio-02.md).

### 🌍 Contexto

Consultar una clave a la vez sirve cuando ya se sabe cuál se necesita. Pero muchas
tareas requieren revisar **todo** el diccionario: mostrar todos los productos, sumar
todos los valores, buscar quién cumple una condición. Para eso se recorre con un bucle.

### 🧠 Concepto

Recorrer un diccionario con `for` visita, por defecto, sus **claves**:

```python
precios = {"pan": 1200, "leche": 950, "huevos": 2600}

for producto in precios:
    print(producto)
# pan
# leche
# huevos
```

Esto es equivalente a `for producto in precios.keys()`, que lo deja explícito.

### 📖 Explicación

**Recorrer valores** con `values()`, cuando no importa a qué clave pertenecen:

```python
for precio in precios.values():
    print(precio)
```

**Recorrer clave y valor a la vez** con `items()`, desempaquetando cada par en dos
variables — la forma más usada cuando se necesitan ambos datos:

```python
for producto, precio in precios.items():
    print(producto, "cuesta", precio)
```

Las tres formas recorren el diccionario en el **orden de inserción** de sus claves
(desde Python 3.7), lo que hace el resultado predecible.

---

## 7️⃣ Métodos comunes y aplicación

**Resultados de aprendizaje**: RA-7, RA-8.

**📎 Practicá esto**: [Ejemplo 05 — update y setdefault](05-update-setdefault.md) ·
[Ejemplo 06 — Contar repeticiones con un diccionario](06-conteo-con-diccionario.md) ·
[Avanzado 01](../ejercicios/avanzado-01.md) ·
[Avanzado 02](../ejercicios/avanzado-02.md) ·
[Desafío 01](../ejercicios/desafio-01.md).

### 🌍 Contexto

Ya se vieron, uno por uno, los métodos para crear, acceder, modificar, eliminar y
recorrer un diccionario. Conviene reunirlos en una sola tabla de referencia, y ver un
método más —`setdefault`— que combina "consultar" con "crear si falta", muy útil para
resolver problemas de conteo o agrupación.

### 🧠 Concepto

| Método | Qué hace | ¿Modifica el diccionario? |
|--------|----------|------------------------------|
| `get(clave, valor_por_defecto)` | devuelve el valor, o el valor por defecto si no existe | No |
| `update(otro)` | agrega/actualiza varias claves a la vez | Sí |
| `pop(clave, valor_por_defecto)` | elimina y devuelve el valor (o el valor por defecto) | Sí |
| `popitem()` | elimina y devuelve el último par `(clave, valor)` | Sí |
| `setdefault(clave, valor_inicial)` | si la clave existe, devuelve su valor; si no, la crea con `valor_inicial` y lo devuelve | Sí, solo si la clave faltaba |
| `keys()` | vista de todas las claves | No |
| `values()` | vista de todos los valores | No |
| `items()` | vista de todos los pares `(clave, valor)` | No |
| `len(diccionario)` | cantidad de pares | No |
| `clear()` | elimina todos los pares | Sí |

### 📖 Explicación

**`setdefault` para inicializar solo si falta.** A diferencia de `get` (que solo
consulta), `setdefault` además **crea** la clave si no existía:

```python
conteo = {}
conteo.setdefault("manzana", 0)   # "manzana" no existía: se crea con 0
conteo["manzana"] += 1
print(conteo)   # {'manzana': 1}
```

Este patrón —"si la clave no existe, dale un valor inicial; luego actualízala"— es la
base para resolver problemas de **conteo** (cuántas veces aparece cada valor) o
**agrupación** (qué elementos pertenecen a cada categoría) con un diccionario, sin tener
que declarar de antemano todas las claves posibles.

**Criterio de decisión.** Frente a lo ya visto en la Clase 03: si los datos deben
identificarse por clave (no por posición ni solo por presencia), y en particular si se
necesita **contar o agrupar** algo por categoría, un diccionario es la estructura
adecuada — una lista obligaría a buscar linealmente cada categoría, y un conjunto no
permite asociar un valor a cada elemento.
