<!--
Presentación — Clase 03: Estructuras de datos lineales y algoritmos de ordenamiento
Formato: Markdown compatible con Marp. Cada diapositiva va separada por una línea "---".
Regla: una sola idea clave por diapositiva; primero el apoyo visual, después poco texto.
Rango permitido: 15-25 diapositivas.
-->

# 📘 Clase 03
## Estructuras de datos lineales y algoritmos de ordenamiento

Curso: Introducción a la Programación con Python · Duración: 3 horas

---

## 🎯 Qué vas a lograr hoy

- Crear, indexar, rebanar y manipular listas.
- Ordenar, contar y buscar con herramientas integradas.
- Entender e implementar algoritmos de ordenamiento clásicos.
- Usar tuplas para datos inmutables y conjuntos para valores únicos.

---

## ¿Qué es una estructura de datos lineal?

```text
frutas = ["manzana", "pera", "uva"]
          ↑pos. 0     ↑pos. 1  ↑pos. 2
```

Datos del mismo grupo, guardados uno tras otro bajo un solo nombre, en vez de muchas
variables sueltas.

---

## Crear una lista

```python
calificaciones = [4.5, 6.0, 3.8, 5.5]
```

Entre corchetes, elementos separados por comas. El índice empieza en `0`.

---

## Indexar y rebanar

```python
frutas[0]      # manzana (primero)
frutas[-1]     # uva (último)
frutas[:2]     # ['manzana', 'pera']
```

Índice positivo desde el inicio; índice negativo desde el final; `[inicio:fin]` da una
sublista nueva.

---

## Manipular listas: agregar

```python
tareas.append("estudiar")     # al final
tareas.insert(0, "urgente")   # en una posición
```

Ambos modifican la lista original.

---

## Manipular listas: eliminar y modificar

```python
tareas.remove("pagar cuentas")  # por valor
tareas.pop()                     # el último
tareas[0] = "nuevo texto"        # por índice
```

`remove` busca por valor; `pop`/`del` por posición.

---

## Recorrer una lista

```python
for fruta in frutas:
    print(fruta)
```

Visita cada elemento, en orden, uno por uno.

---

## Construir una lista nueva

```python
aprobados = []
for nota in calificaciones:
    if nota >= 6.0:
        aprobados.append(nota)
```

Recorrer + `if` + `append`: la original no cambia.

---

## Ordenar: sort vs sorted

```python
numeros.sort()          # modifica la lista; devuelve None
sorted(numeros)          # devuelve una lista nueva
sorted(numeros, reverse=True)
```

`sort` cambia el original; `sorted` deja el original intacto.

---

## Ordenar por un criterio: key

```python
def obtener_nota(registro):
    return registro[1]

sorted(estudiantes, key=obtener_nota)
```

`key` recibe una función que dice **por qué valor** comparar.

---

## Buscar y contar

```python
"Ana" in nombres        # True/False
nombres.index("Ana")    # posición de la primera aparición
nombres.count("Ana")    # cuántas veces aparece
min(notas), max(notas), sum(notas)
```

Ninguna de estas modifica la lista original.

---

## Ordenamiento por burbuja

```text
[5, 1, 4, 2]
compara vecinos, intercambia si hace falta
el mayor restante "sube" al final en cada pasada
```

Varias pasadas de comparar-e-intercambiar vecinos.

---

## Ordenamiento por selección e inserción

```text
Selección:  busca el mínimo restante, lo pone al frente
Inserción:  toma cada elemento e inserta en su lugar
```

Dos estrategias distintas para el mismo resultado: una lista ordenada.

---

## ¿Algoritmo clásico o `sorted`?

| Objetivo | Usar |
|----------|------|
| Comprender cómo se ordena | burbuja / selección / inserción |
| Resolver un problema real | `sort()` / `sorted()` |

Los clásicos hacen más trabajo cuanto más crece la lista; `sorted` está optimizado.

---

## Tuplas: datos que no cambian

```python
coordenada = (10, 20)
coordenada[0] = 99   # TypeError
```

Igual que una lista, pero **inmutable**: una vez creada, no se modifica.

---

## Desempaquetar una tupla

```python
nombre, nota = ("Ana", 6.5)
```

Asigna cada valor de la tupla a una variable, en una sola línea.

---

## Conjuntos: valores únicos

```python
set([1, 2, 2, 3, 3, 3])   # {1, 2, 3}
```

Sin orden, sin duplicados. Ideal para "¿está?" y "¿cuántos distintos?".

---

## Operaciones de conjuntos

```python
a | b    # unión: todos, sin repetir
a & b    # intersección: en ambos
a - b    # diferencia: solo en a
```

---

## Lista, tupla o conjunto: ¿cuál uso?

| | Lista | Tupla | Conjunto |
|---|---|---|---|
| Orden | Sí | Sí | No |
| Mutable | Sí | No | Sí |
| Duplicados | Sí | Sí | No |

---

## Actividad práctica

**Taller 01 — Gestor de calificaciones de un curso**

Registros como tuplas `(nombre, nota)`; ordenar con `key`, calcular estadísticas y
obtener el conjunto de aprobados únicos.

---

## Resumen

- Lista: colección ordenada y mutable; se crea, indexa, rebana y manipula con métodos.
- `sort`/`sorted`, `key` y `reverse`: ordenar sin escribir un algoritmo a mano.
- Burbuja, selección e inserción: para **comprender** el ordenamiento; `sorted` para
  **resolver** un problema real.
- Tupla: registro fijo e inmutable. Conjunto: valores únicos, sin orden.

---

## Evaluación

**Quiz 01** — 10 preguntas: selección múltiple, análisis de código, identificación de
resultado, corrección de errores y un problema breve de programación.
