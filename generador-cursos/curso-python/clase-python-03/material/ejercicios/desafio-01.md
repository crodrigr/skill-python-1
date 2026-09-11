# Desafío 01 — Organizador de una carrera de atletismo

## Problema

Una carrera de atletismo registra, para cada corredor que termina, su nombre y su
tiempo en segundos. Al finalizar la carrera hay que:

1. Elegir cómo representar cada resultado individual (¿lista, tupla u otra cosa?) y
   justificar la elección.
2. Elegir cómo representar el conjunto de todos los resultados.
3. Ordenar los resultados por tiempo, de menor a mayor (gana quien hace menos tiempo).
4. Decidir y justificar si, para esta tarea, conviene implementar un algoritmo de
   ordenamiento clásico a mano o usar el ordenamiento integrado de Python.
5. Mostrar el podio (los tres primeros lugares) con su posición, nombre y tiempo.
6. A partir de los nombres de todos los corredores que terminaron, obtener cuántos
   nombres **distintos** participaron (algunos corredores podrían aparecer registrados
   más de una vez por un error de doble registro).

## Análisis

- **Entrada**: una lista de resultados sin ordenar, cada uno con nombre y tiempo.
- **Proceso**: elegir estructuras (registro individual, colección de resultados,
  colección de nombres únicos); ordenar por tiempo; extraer el podio; contar nombres
  distintos.
- **Salida**: el podio (tres primeros) y la cantidad de corredores distintos.

## Solución esperada (guía, no código)

1. Cada resultado se representa como una **tupla** `(nombre, tiempo)`: es un registro
   fijo que no debe modificarse una vez cargado.
2. El conjunto de resultados se representa como una **lista** de esas tuplas: hace
   falta un orden y puede haber tiempos repetidos.
3. Ordenar con `sorted(resultados, key=<función que devuelve el tiempo>)`: es la tarea
   de "obtener un resultado ordenado para resolver un problema real", así que se
   justifica usar el ordenamiento integrado en vez de implementar un algoritmo a mano.
4. El podio son los tres primeros elementos de la lista ya ordenada (rebanado `[:3]`).
5. Los nombres únicos se obtienen construyendo un **conjunto** a partir de la lista de
   nombres.

## Entrada

```python
resultados = [
    ("Camila", 62.4),
    ("Tomás", 58.9),
    ("Valeria", 60.1),
    ("Camila", 62.4),   # registrada dos veces por error
    ("Benjamín", 57.3),
    ("Diego", 65.0),
    ("Diego", 65.0),    # registrado dos veces por error
]
```

## Proceso esperado

Elegir y justificar tupla para el registro y lista para la colección ordenable; usar
`sorted` con una función `key` para ordenar por tiempo; usar rebanado para el podio;
construir un conjunto de nombres para contar los corredores distintos.

## Salida

```text
Podio:
1. Benjamín - 57.3 s
2. Tomás - 58.9 s
3. Valeria - 60.1 s
Corredores distintos: 5
```

## Restricciones

- El registro de cada corredor debe ser una tupla, no una lista.
- El ordenamiento debe hacerse con `sorted` y una función `key` (no un algoritmo
  clásico escrito a mano); la solución debe justificar por qué esta es la opción
  adecuada para esta tarea, a diferencia de un ejercicio dedicado a comprender un
  algoritmo.
- Los nombres únicos deben obtenerse con un conjunto, no contando "a mano" con un bucle
  y una lista auxiliar.
- Los identificadores y comentarios deben estar en español.

## Dificultad

Desafío

## Resultados de aprendizaje

- RA-7: analizar un problema y seleccionar el mecanismo de ordenamiento más adecuado,
  justificando la elección.
- RA-8: usar una tupla para representar un registro inmutable.
- RA-9: usar un conjunto para obtener valores únicos.
- RA-5: ordenar con `sorted` y `key`, y usar rebanado para extraer una parte de la
  lista.

## Casos de prueba

| Entrada (`resultados`) | Salida esperada |
|--------------------------|------------------|
| la lista de 7 registros indicada arriba (con 2 duplicados) | Podio: 1. Benjamín 57.3 s, 2. Tomás 58.9 s, 3. Valeria 60.1 s; Corredores distintos: 5 |
| `[("Ana", 70.0), ("Beto", 65.0)]` (solo dos corredores, sin duplicados) | Podio: 1. Beto 65.0 s, 2. Ana 70.0 s (solo dos lugares); Corredores distintos: 2 |
