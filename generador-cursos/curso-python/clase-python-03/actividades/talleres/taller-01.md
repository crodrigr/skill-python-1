# Taller 01 — Gestor de calificaciones de un curso

**Actividad guiada** · Duración estimada: 40–50 min · **Resultados de aprendizaje**:
RA-2, RA-3, RA-5, RA-8, RA-9

## Objetivo

Construir, paso a paso, un programa que mantenga las calificaciones de un curso como
una lista de registros inmutables (tuplas `nombre, nota`), permita agregar, eliminar y
corregir registros, ordene la lista por distintos criterios usando el ordenamiento
integrado de Python, calcule estadísticas con funciones integradas y obtenga con un
conjunto los nombres únicos de quienes aprobaron (RA-2, RA-3, RA-5, RA-8, RA-9).

## Contexto

Un docente lleva el registro de las notas de su curso. Cada estudiante es un par
`(nombre, nota)` que no debería modificarse por accidente una vez cargado — si hay que
corregir una nota, se reemplaza el registro completo, no un solo valor suelto. El
docente necesita agregar estudiantes nuevos, quitar a quien se dio de baja, ver el
listado ordenado por nota y por nombre, conocer rápidamente cuántos aprobaron y con qué
promedio, y saber cuántos estudiantes **distintos** aprobaron (por si alguien quedó
registrado más de una vez).

La nota mínima de aprobación es `4.0`.

## Pasos

### 1. Representar los registros

Completa la lista inicial de registros, cada uno como una tupla `(nombre, nota)`:

```python
calificaciones = [
    ("Ana", 6.5),
    ("Luis", 3.8),
    ("Eva", 5.0),
    ("Ana", 6.5),   # Ana quedó registrada dos veces por error
]
```

### 2. Agregar, eliminar y modificar registros

- Agrega un nuevo registro al final con `append`: `("Marco", 4.5)`.
- Elimina el registro de `"Luis"` (se dio de baja) con `remove`, pasando la tupla
  completa `("Luis", 3.8)`.
- Corrige la nota de `"Eva"`: reemplaza su registro por `("Eva", 7.0)` usando su
  posición actual en la lista (con `index` sobre la tupla original).

### 3. Ordenar por nota y por nombre

Define una función que reciba un registro y devuelva la nota, y otra que devuelva el
nombre. Usa `sorted` con `key` para obtener:

- La lista ordenada por nota, de mayor a menor (`reverse=True`).
- La lista ordenada alfabéticamente por nombre.

### 4. Calcular estadísticas

A partir de la lista de notas (obtenida recorriendo los registros), usa funciones
integradas para calcular:

- Cuántos estudiantes aprobaron (nota `>= 4.0`) — recorriendo y contando con un
  acumulador, o construyendo primero la lista de aprobados y usando `len`.
- La nota máxima, la nota mínima y el promedio (`sum(...) / len(...)`).

### 5. Nombres únicos de aprobados

Recorre la lista de registros y, para cada uno con nota `>= 4.0`, agrega el nombre a un
conjunto. Muestra el conjunto de nombres únicos de aprobados (ordenado con `sorted`
para que la salida sea predecible).

## Entregable

Un programa Python que:

1. Mantiene la lista de registros `(nombre, nota)` tras aplicar los cambios del paso 2.
2. Muestra la lista ordenada por nota (descendente) y por nombre (alfabético).
3. Muestra la cantidad de aprobados, la nota máxima, la mínima y el promedio.
4. Muestra el conjunto (ordenado) de nombres únicos de quienes aprobaron.

## Casos de prueba

| Estado tras el paso 2 | Salida esperada (resumen) |
|------------------------|----------------------------|
| `[("Ana", 6.5), ("Eva", 7.0), ("Ana", 6.5), ("Marco", 4.5)]` | Por nota (desc): Eva 7.0, Ana 6.5, Ana 6.5, Marco 4.5; por nombre (alfabético): Ana, Ana, Eva, Marco; aprobados: 4; máxima: 7.0; mínima: 4.5; promedio: 6.125; aprobados únicos: ['Ana', 'Eva', 'Marco'] |

## Criterios de evaluación

- Cada estudiante se representa como una tupla inmutable `(nombre, nota)`, no como una
  lista de dos elementos.
- El ordenamiento por nota y por nombre usa `sorted` con una función `key` (y
  `reverse` cuando corresponde), no un algoritmo de ordenamiento escrito a mano.
- Las estadísticas (conteo de aprobados, máxima, mínima, promedio) se obtienen con
  funciones integradas (`len`, `max`, `min`, `sum`), no recalculadas letra por letra sin
  necesidad.
- El conjunto de nombres únicos de aprobados no contiene nombres repetidos, aunque el
  mismo nombre aparezca en más de un registro.
- El programa produce la salida correcta para el caso de prueba indicado.

> Nota para el docente: una versión resuelta y comentada está disponible en
> `../../material/soluciones/soluciones-ejercicios.md` (sección "Taller 01"). No
> compartir con el estudiantado antes de la puesta en común.
