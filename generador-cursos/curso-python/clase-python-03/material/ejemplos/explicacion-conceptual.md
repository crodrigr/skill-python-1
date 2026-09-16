# 📚 Explicación conceptual — Clase 03: Estructuras de datos lineales y algoritmos de ordenamiento

Este documento desarrolla, en orden pedagógico, los ocho bloques temáticos de la clase.
Cada bloque sigue la secuencia **Contexto → Concepto → Explicación**. El lenguaje es
deliberadamente sencillo y solo supone lo visto en las Clases 01 y 02 (variables, tipos
de datos básicos, operadores, condicionales, bucles y funciones).

Convención de código: los nombres de variables, listas, tuplas, conjuntos y funciones, y
los comentarios están en español; solo las palabras reservadas de Python (`if`, `for`,
`in`, `and`, …) están en inglés porque forman parte del lenguaje.

---

## 1️⃣ Estructuras de datos lineales

**Resultado de aprendizaje**: RA-1.

### 🌍 Contexto

Hasta ahora, cada dato de un programa vivía en su propia variable: `nota1`, `nota2`,
`nota3`… Eso funciona con dos o tres valores, pero se vuelve inmanejable con veinte
calificaciones, cien productos o mil registros: habría que crear —y nombrar— una
variable por cada uno, y un bucle no podría recorrerlos porque no comparten un nombre en
común.

### 🧠 Concepto

Una **estructura de datos** es una forma de agrupar varios valores relacionados bajo un
solo nombre, de modo que se puedan crear, recorrer y manipular como un conjunto. Una
estructura de datos **lineal** organiza sus elementos uno detrás de otro, en una
secuencia, igual que los vagones de un tren o los nombres en una lista de asistencia:
cada elemento tiene una posición y un "siguiente".

Python ofrece varias estructuras lineales; en esta clase se estudian tres:

| Estructura | Orden | ¿Se puede modificar? | ¿Permite repetidos? |
|------------|-------|-----------------------|----------------------|
| **Lista** (`list`) | Sí | Sí (mutable) | Sí |
| **Tupla** (`tuple`) | Sí | No (inmutable) | Sí |
| **Conjunto** (`set`) | No | Sí (mutable) | No |

### 📖 Explicación

Piensa en una lista de asistencia de un curso: los nombres están en un orden (el de
llegada, o el alfabético) y se puede tachar a alguien que se retira o añadir a quien
llega tarde — es **mutable**. Una tupla es como la fecha de nacimiento de una persona:
tiene un orden fijo (día, mes, año) que no tiene sentido "editar" una vez registrado — es
**inmutable**. Un conjunto es como la lista de países que alguien ha visitado: solo
importa si un país está o no está, no el orden ni cuántas veces se repite la visita.

Elegir la estructura correcta desde el principio evita errores más adelante: intentar
"editar" una tupla o esperar que un conjunto respete un orden son fuentes comunes de
confusión que se resuelven conociendo, desde ya, para qué sirve cada una. El resto de la
clase profundiza primero en las listas (las más usadas), luego en los algoritmos de
ordenamiento, y cierra con tuplas y conjuntos.

---

## 2️⃣ Creación e indexación de listas

**Resultado de aprendizaje**: RA-2.

**📎 Practicá esto**: [Ejemplo 01 — Crear listas, indexar y rebanar](01-crear-listas-indexar-rebanar.md) ·
[Básico 01](../ejercicios/basico-01.md).

### 🌍 Contexto

Ya sabemos que agrupar datos relacionados bajo un solo nombre resuelve el problema de
las variables sueltas. La lista es la estructura de datos más común de Python para
lograrlo: hay que aprender a crearla y a acceder a los datos que guarda.

### 🧠 Concepto

Una **lista** se escribe entre corchetes `[ ]`, con sus elementos separados por comas:

```python
calificaciones = [4.5, 6.0, 3.8, 5.5]
frutas = ["manzana", "pera", "uva"]
lista_vacia = []
```

Cada elemento tiene una posición, llamada **índice**, que empieza en `0` (no en `1`):

```text
frutas =  ["manzana", "pera", "uva"]
índice:      0          1      2
```

Se accede a un elemento con `lista[indice]`:

```python
print(frutas[0])   # manzana
print(frutas[2])   # uva
```

### 📖 Explicación

**Índices negativos.** Python también permite contar desde el final: `-1` es el último
elemento, `-2` el anteúltimo, y así sucesivamente:

```python
print(frutas[-1])   # uva (el último)
print(frutas[-2])   # pera
```

**Longitud.** `len(lista)` devuelve cuántos elementos tiene:

```python
print(len(frutas))   # 3
```

**Rebanado (slicing).** `lista[inicio:fin]` devuelve una **sublista nueva** con los
elementos desde `inicio` (incluido) hasta `fin` (excluido):

```python
numeros = [10, 20, 30, 40, 50]
print(numeros[1:3])    # [20, 30]  (índices 1 y 2; el 3 no se incluye)
print(numeros[:2])     # [10, 20]  (desde el inicio hasta el índice 2, sin incluirlo)
print(numeros[2:])     # [30, 40, 50]  (desde el índice 2 hasta el final)
print(numeros[:])      # [10, 20, 30, 40, 50]  (copia completa)
```

Un tercer número opcional indica el **paso**: `lista[inicio:fin:paso]`:

```python
print(numeros[::2])    # [10, 30, 50]  (de dos en dos)
print(numeros[::-1])   # [50, 40, 30, 20, 10]  (la lista invertida)
```

**Acceder fuera de rango.** Pedir un índice que no existe produce un error:

```python
print(frutas[10])   # IndexError: list index out of range
```

Por eso conviene comprobar `len(lista)` antes de acceder a una posición que no se sabe
con certeza que existe.

---

## 3️⃣ Manipulación de listas

**Resultado de aprendizaje**: RA-3.

**📎 Practicá esto**: [Ejemplo 02 — Agregar, eliminar y modificar elementos](02-agregar-eliminar-modificar.md) ·
[Básico 01](../ejercicios/basico-01.md) ·
[Avanzado 02](../ejercicios/avanzado-02.md).

### 🌍 Contexto

Una lista casi nunca es fija: llegan nuevos datos que agregar, otros que ya no
corresponden y hay que quitar, y algunos que hay que corregir. Python ofrece métodos y
operadores para cada una de esas tres acciones.

### 🧠 Concepto

**Agregar elementos:**

```python
tareas = ["comprar pan", "pagar cuentas"]

tareas.append("estudiar Python")        # agrega al final
tareas.insert(1, "llamar al dentista")  # inserta en la posición 1
tareas_extra = tareas + ["hacer ejercicio"]  # concatena; crea una lista nueva
tareas.extend(["leer", "dormir"])       # agrega varios elementos al final
```

**Eliminar elementos:**

```python
tareas.remove("pagar cuentas")   # elimina la PRIMERA aparición de ese valor
ultima = tareas.pop()            # quita y devuelve el último elemento
segunda = tareas.pop(1)          # quita y devuelve el elemento en la posición 1
del tareas[0]                    # elimina por posición, sin devolver nada
```

**Modificar un elemento** (asignación directa por índice):

```python
tareas[0] = "comprar pan integral"
```

### 📖 Explicación

La tabla resume qué hace cada operación y si **modifica la lista original** o **devuelve
una nueva**:

| Operación | Efecto | ¿Modifica la lista original? |
|-----------|--------|-------------------------------|
| `lista.append(x)` | agrega `x` al final | Sí |
| `lista.insert(i, x)` | inserta `x` en la posición `i` | Sí |
| `lista.extend(otra)` | agrega todos los elementos de `otra` al final | Sí |
| `lista + otra` | concatena | No (crea una lista nueva) |
| `lista.remove(x)` | quita la primera aparición de `x` | Sí |
| `lista.pop(i)` | quita y devuelve el elemento en `i` (o el último si se omite `i`) | Sí |
| `del lista[i]` | quita el elemento en `i` | Sí |
| `lista[i] = x` | reemplaza el elemento en `i` por `x` | Sí |

**Errores comunes.** `remove` lanza `ValueError` si el valor no está en la lista; `pop`
lanza `IndexError` si el índice no existe. Por eso conviene comprobar con `in` (se
explica más adelante, en Operaciones integradas) antes de eliminar algo que podría no
estar.

Ejemplo del estado de la lista paso a paso:

```python
numeros = [1, 2, 3]
numeros.append(4)      # [1, 2, 3, 4]
numeros.insert(0, 0)   # [0, 1, 2, 3, 4]
numeros.remove(2)      # [0, 1, 3, 4]
numeros.pop()          # devuelve 4; queda [0, 1, 3]
numeros[0] = 100       # [100, 1, 3]
```

---

## 4️⃣ Recorrido y transformación

**Resultado de aprendizaje**: RA-4.

**📎 Practicá esto**: [Ejemplo 03 — Recorrer y transformar una lista](03-recorrer-y-transformar.md) ·
[Intermedio 01](../ejercicios/intermedio-01.md) ·
[Avanzado 02](../ejercicios/avanzado-02.md).

### 🌍 Contexto

Muchas tareas requieren revisar **todos** los elementos de una lista, uno por uno:
sumarlos, mostrarlos, o construir una lista nueva a partir de ellos (por ejemplo, solo
los que cumplen una condición). Para eso se combina la lista con el bucle `for` que ya
se conoce de la Clase 01.

### 🧠 Concepto

**Recorrer por elemento** (la forma más común):

```python
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)
```

**Recorrer por índice**, útil cuando además de cada valor se necesita su posición:

```python
for indice in range(len(frutas)):
    print(indice, "->", frutas[indice])
```

**Comprobar si un valor está presente** con `in`:

```python
if "pera" in frutas:
    print("Sí hay pera")
```

### 📖 Explicación

**Construir una lista nueva a partir de otra.** Un patrón muy frecuente: recorrer una
lista y, según una condición o una transformación, ir agregando elementos a una lista
nueva con `append`:

```python
numeros = [4, 7, 10, 13, 18]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)   # [4, 10, 18]
```

La lista `numeros` **no cambió**: `pares` es una lista distinta construida a partir de
ella. Esta idea de "recorrer y construir una lista nueva" es la base de tareas como
filtrar, transformar o resumir datos.

**Asignación vs. copia (tratamiento mínimo).** Cuidado: asignar una lista a otra
variable no crea una copia independiente, sino que ambos nombres apuntan a la misma
lista:

```python
original = [1, 2, 3]
referencia = original      # NO es una copia; es el mismo objeto
referencia.append(4)
print(original)            # [1, 2, 3, 4]  <- también cambió
```

Para obtener una copia independiente se usa `lista[:]` o `lista.copy()`:

```python
copia = original[:]        # o: original.copy()
copia.append(100)
print(original)            # [1, 2, 3, 4]      <- sin cambios
print(copia)                # [1, 2, 3, 4, 100]
```

No se profundiza más en este tema por ahora: basta con reconocer la diferencia para
evitar el error de "modifiqué una lista y otra cambió sin que yo lo pidiera".

---

## 5️⃣ Operaciones integradas

**Resultado de aprendizaje**: RA-5.

**📎 Practicá esto**: [Ejemplo 04 — Ordenar con sort, sorted y key](04-ordenar-sort-sorted-key.md) ·
[Ejemplo 05 — Buscar y contar con funciones integradas](05-buscar-y-contar.md) ·
[Básico 02](../ejercicios/basico-02.md) ·
[Intermedio 01](../ejercicios/intermedio-01.md) ·
[Desafío 01](../ejercicios/desafio-01.md).

### 🌍 Contexto

Ordenar una lista, contar cuántas veces aparece un valor o buscar si algo está presente
son tareas tan comunes que Python ya las resuelve con métodos y funciones integradas.
Antes de escribir un algoritmo propio (lo que se hace en el siguiente bloque, con fines
de comprensión), conviene conocer las herramientas listas para usar.

### 🧠 Concepto

**Ordenar.** Hay dos formas de ordenar una lista:

```python
numeros = [5, 2, 9, 1]

numeros.sort()          # ordena la lista ORIGINAL; no devuelve nada útil (None)
print(numeros)          # [1, 2, 5, 9]

otros = [5, 2, 9, 1]
ordenados = sorted(otros)   # devuelve una lista NUEVA; 'otros' no cambia
print(otros)                 # [5, 2, 9, 1]  (sin cambios)
print(ordenados)             # [1, 2, 5, 9]
```

Ambas aceptan `reverse=True` para ordenar de mayor a menor:

```python
print(sorted(otros, reverse=True))   # [9, 5, 2, 1]
```

**Ordenar por un criterio (`key`).** Cuando los elementos son más complejos (por
ejemplo, tuplas), `key` indica **qué** usar para comparar. Se le pasa una función que,
dado un elemento, devuelve el valor por el que ordenar:

```python
def obtener_nota(registro):
    """Devuelve la nota (segundo valor) de un registro (nombre, nota)."""
    return registro[1]

estudiantes = [("Ana", 6.5), ("Luis", 3.8), ("Eva", 8.0)]
por_nota = sorted(estudiantes, key=obtener_nota)
print(por_nota)   # [('Luis', 3.8), ('Ana', 6.5), ('Eva', 8.0)]
```

Nótese que a `key` se le pasa la función **sin paréntesis** (`obtener_nota`, no
`obtener_nota()`): `sorted` es quien la llama, una vez por cada elemento, para saber por
qué valor comparar.

### 📖 Explicación

**Buscar y contar:**

| Operación | Qué hace | Ejemplo |
|-----------|----------|---------|
| `valor in lista` | ¿está el valor? Devuelve `True`/`False` | `"Ana" in nombres` |
| `lista.index(valor)` | posición de la primera aparición | `nombres.index("Ana")` |
| `lista.count(valor)` | cuántas veces aparece | `nombres.count("Ana")` |
| `len(lista)` | cantidad de elementos | `len(nombres)` |
| `min(lista)` | el valor más pequeño | `min(notas)` |
| `max(lista)` | el valor más grande | `max(notas)` |
| `sum(lista)` | la suma de los valores | `sum(notas)` |

```python
notas = [4.5, 6.0, 3.8, 6.0, 5.5]
print(6.0 in notas)        # True
print(notas.index(6.0))    # 1 (la primera aparición)
print(notas.count(6.0))    # 2
print(min(notas), max(notas), sum(notas))   # 3.8 6.0 25.8
```

**Cuidado con lo que no existe.** `lista.index(valor)` lanza `ValueError` si el valor no
está; por eso conviene comprobar antes con `in`:

```python
if 100 in notas:
    print(notas.index(100))
else:
    print("Ese valor no está en la lista")
```

**Resumen de qué modifica y qué no**, para no confundirse:

| Operación | ¿Modifica la lista original? |
|-----------|-------------------------------|
| `lista.sort()` | Sí |
| `sorted(lista)` | No |
| `lista.reverse()` | Sí |
| `in`, `index`, `count`, `len`, `min`, `max`, `sum` | No (solo consultan) |

---

## 6️⃣ Algoritmos de ordenamiento

**Resultados de aprendizaje**: RA-6, RA-7.

**📎 Practicá esto**: [Ejemplo 06 — Ordenamiento por burbuja, paso a paso](06-ordenamiento-burbuja.md) ·
[Avanzado 01](../ejercicios/avanzado-01.md) ·
[Desafío 01](../ejercicios/desafio-01.md).

### 🌍 Contexto

`sorted()` ordena cualquier lista en una sola línea. Entonces, ¿por qué estudiar cómo
ordenar "a mano"? Porque entender **cómo** se ordena por dentro desarrolla la capacidad
de analizar un problema paso a paso, descubre por qué algunas soluciones hacen más
trabajo que otras, y es la base para reconocer cuándo conviene un algoritmo simple y
cuándo conviene apoyarse en la herramienta que ya trae el lenguaje.

### 🧠 Concepto

Un **algoritmo de ordenamiento** es un procedimiento que reorganiza los elementos de una
lista según un criterio (por ejemplo, de menor a mayor), comparando e intercambiando
elementos repetidamente hasta que quedan en orden. Se estudian tres, todos con bucles
anidados (uno dentro de otro):

**Burbuja.** En cada pasada, se comparan pares de elementos **vecinos**; si están en el
orden incorrecto, se intercambian. Al final de cada pasada, el elemento más grande no
colocado "sube" hasta su posición final, como una burbuja que sube a la superficie.

```text
Lista: [5, 1, 4, 2]

Pasada 1:
  compara (5,1) -> intercambia -> [1, 5, 4, 2]
  compara (5,4) -> intercambia -> [1, 4, 5, 2]
  compara (5,2) -> intercambia -> [1, 4, 2, 5]   <- el 5 ya llegó a su lugar final

Pasada 2:
  compara (1,4) -> no intercambia
  compara (4,2) -> intercambia -> [1, 2, 4, 5]   <- el 4 ya llegó a su lugar

Pasada 3:
  compara (1,2) -> no intercambia -> [1, 2, 4, 5]   (ordenada)
```

**Selección.** En cada pasada, se busca el elemento **más pequeño** de la parte aún no
ordenada y se lo intercambia con el primero de esa parte.

```text
Lista: [5, 1, 4, 2]

Pasada 1: el menor de [5,1,4,2] es 1 -> intercambia con la posición 0 -> [1, 5, 4, 2]
Pasada 2: el menor de [5,4,2] es 2 -> intercambia con la posición 1  -> [1, 2, 4, 5]
Pasada 3: el menor de [4,5] es 4 -> ya está en su lugar              -> [1, 2, 4, 5]
```

**Inserción.** Se toma cada elemento, empezando por el segundo, y se lo **inserta** en
la posición correcta dentro de la parte ya ordenada, desplazando lo que haga falta —
como ordenar cartas de una mano, una a la vez.

```text
Lista: [5, 1, 4, 2]

Parte ordenada: [5]
Tomar 1: 1 < 5 -> insertar antes -> [1, 5]
Tomar 4: 4 < 5, 4 > 1 -> insertar entre -> [1, 4, 5]
Tomar 2: 2 < 5, 2 < 4, 2 > 1 -> insertar entre -> [1, 2, 4, 5]
```

### 📖 Explicación

**Comparación de estrategias:**

| Algoritmo | Idea central | Qué "avanza" en cada pasada |
|-----------|---------------|------------------------------|
| Burbuja | comparar vecinos y a veces intercambiar | el mayor restante llega a su posición final |
| Selección | buscar el mínimo restante | el menor restante llega a su posición final |
| Inserción | insertar cada elemento donde corresponde | la parte ordenada crece de a un elemento |

**Criterios de selección (RA-7).** Los tres algoritmos anteriores existen para
**comprender** cómo funciona el ordenamiento: recorren la lista varias veces y hacen
comparaciones e intercambios explícitos, por lo que hacen **más trabajo** cuanto más
crece la lista. En cambio, `sort()`/`sorted()` de Python está optimizado internamente y
es, en la práctica, siempre la opción recomendada para resolver un problema real. La
regla para decidir es sencilla:

- ¿El objetivo es **entender** o **enseñar** cómo se ordena una lista, paso a paso? →
  usar un algoritmo clásico (burbuja, selección o inserción).
- ¿El objetivo es **obtener** una lista ordenada para resolver un problema? → usar
  `sort()`/`sorted()`, que hace menos trabajo y es menos propenso a errores de
  implementación, sin necesidad de compararlos con fórmulas ni notación matemática.

Existen algoritmos más avanzados (por ejemplo, mezcla y rápido) que ordenan haciendo
todavía menos trabajo que burbuja, selección e inserción cuando la lista es grande; esta
clase solo los menciona por nombre, sin implementarlos, porque su estrategia (dividir la
lista en partes más pequeñas) requiere más base de la que se tiene hasta ahora.

---

## 7️⃣ Tuplas

**Resultado de aprendizaje**: RA-8.

**📎 Practicá esto**: [Ejemplo 07 — Tuplas y desempaquetado](07-tuplas-desempaquetado.md) ·
[Intermedio 02](../ejercicios/intermedio-02.md) ·
[Avanzado 02](../ejercicios/avanzado-02.md) ·
[Desafío 01](../ejercicios/desafio-01.md).

### 🌍 Contexto

Algunos datos, una vez creados, no deberían cambiar: la fecha de nacimiento de una
persona, una coordenada `(x, y)`, el mes y el año de un pago ya realizado. Usar una
lista para esos casos permitiría, por error, modificarlos más adelante en el programa.
Para esos datos, Python ofrece una estructura pensada para no cambiar: la tupla.

### 🧠 Concepto

Una **tupla** se escribe entre paréntesis `( )`, con sus elementos separados por comas:

```python
coordenada = (10, 20)
registro_estudiante = ("Ana", 6.5)
```

Se accede a sus elementos igual que en una lista, por índice:

```python
print(registro_estudiante[0])   # Ana
print(registro_estudiante[1])   # 6.5
```

La diferencia clave: una tupla es **inmutable**. Una vez creada, no se puede agregar,
eliminar ni modificar ningún elemento:

```python
registro_estudiante[1] = 7.0
# TypeError: 'tuple' object does not support item assignment
```

### 📖 Explicación

**Desempaquetado.** Una tupla se puede "abrir" en varias variables a la vez, una
asignación muy usada con registros:

```python
nombre, nota = registro_estudiante
print(nombre)   # Ana
print(nota)     # 6.5
```

El número de variables a la izquierda debe coincidir con la cantidad de elementos de la
tupla.

**Tupla vs. lista — cuándo usar cada una:**

| Se necesita... | Usar |
|-----------------|------|
| Agregar, quitar o modificar elementos con el tiempo | Lista |
| Un registro fijo que no debe cambiar (coordenada, fecha, un par nombre-valor) | Tupla |
| Usar el valor como elemento de un conjunto (ver bloque 8) | Tupla (las listas no pueden ir dentro de un conjunto) |

En la práctica: si los datos representan una **colección que crece y cambia**, se usa
una lista; si representan un **registro fijo con una forma conocida**, se usa una
tupla.

---

## 8️⃣ Conjuntos y comparación de estructuras

**Resultado de aprendizaje**: RA-9.

**📎 Practicá esto**: [Ejemplo 08 — Conjuntos y sus operaciones](08-conjuntos-operaciones.md) ·
[Intermedio 02](../ejercicios/intermedio-02.md) ·
[Avanzado 02](../ejercicios/avanzado-02.md) ·
[Desafío 01](../ejercicios/desafio-01.md).

### 🌍 Contexto

Algunas tareas no necesitan orden ni permiten repeticiones: la lista de países visitados
por una persona, las etiquetas únicas de un artículo, los códigos de curso en los que
un estudiante ya está inscrito. Repetir un valor en esos casos no aporta nada y, si se
usa una lista, hay que revisarla entera cada vez para evitar duplicados. Para esto
existe el conjunto.

### 🧠 Concepto

Un **conjunto** se escribe entre llaves `{ }`, o se construye a partir de otra
colección con `set(...)`:

```python
colores = {"rojo", "verde", "azul"}
numeros_con_repetidos = [1, 2, 2, 3, 3, 3]
numeros_unicos = set(numeros_con_repetidos)
print(numeros_unicos)   # {1, 2, 3}  (sin duplicados)
```

Un conjunto **no tiene orden** (no se puede acceder por índice) y **no admite
duplicados**: si se intenta agregar un valor que ya está, simplemente no pasa nada.

```python
colores.add("rojo")     # ya estaba: el conjunto no cambia
colores.add("amarillo") # se agrega
colores.discard("verde")  # se quita si está (no da error si no está)
print("rojo" in colores)  # True
```

### 📖 Explicación

**Operaciones de conjuntos.** Comparar dos conjuntos es una de las razones principales
para usarlos:

```python
inscritos_python = {"Ana", "Luis", "Eva"}
inscritos_bases_datos = {"Luis", "Marco"}

print(inscritos_python | inscritos_bases_datos)   # unión: todos, sin repetir
print(inscritos_python & inscritos_bases_datos)   # intersección: en ambos cursos
print(inscritos_python - inscritos_bases_datos)   # diferencia: solo en Python
```

| Operación | Símbolo | Resultado |
|-----------|---------|-----------|
| Unión | `\|` | todos los elementos de ambos conjuntos, sin repetir |
| Intersección | `&` | solo los elementos que están en los dos |
| Diferencia | `-` | los elementos del primero que no están en el segundo |

**Comparación entre lista, tupla y conjunto:**

| | Lista | Tupla | Conjunto |
|---|-------|-------|----------|
| Orden | Sí (por índice) | Sí (por índice) | No |
| Mutable | Sí | No | Sí (agregar/quitar, no por índice) |
| Duplicados | Sí | Sí | No |
| Uso típico | colección que cambia con el tiempo | registro fijo | valores únicos, pertenencia |

**Criterio de decisión.** Al modelar un problema, conviene preguntarse: ¿el orden
importa? ¿los datos pueden repetirse? ¿necesito modificar la colección después de
crearla? Las respuestas apuntan directamente a lista, tupla o conjunto.
