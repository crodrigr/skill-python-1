# 🔴 Avanzado 01 — Corregir un ordenamiento por selección

## 🧩 Problema

El siguiente programa intenta ordenar una lista de menor a mayor usando el algoritmo de
ordenamiento por **selección**, pero tiene un error y no siempre produce el resultado
correcto. Analiza el código, identifica el error y corrígelo para que ordene
correctamente cualquier lista de números.

Pista: en cada pasada hay que **recordar** la posición del elemento más pequeño
encontrado hasta el momento, para poder comparar los siguientes contra ese valor y, al
final de la búsqueda, intercambiarlo con el primero de la parte no ordenada.

## 📥 Entrada

La lista `[7, 2, 9, 1, 5]`, fija en el código de partida.

## ⚙️ Proceso esperado

Corregir la implementación del ordenamiento por selección conservando la estructura de
bucles anidados (bucle exterior por pasada, bucle interior para buscar el mínimo), sin
usar `sort` ni `sorted`.

## 📤 Salida

La lista ordenada de menor a mayor: `[1, 2, 5, 7, 9]`.

## 🚧 Restricciones

- No usar `sort()` ni `sorted()`: el ordenamiento debe quedar implementado a mano.
- Conservar el nombre y la estructura general de las variables del código de partida en
  lo posible.
- Los identificadores y comentarios deben estar en español.

## 📊 Dificultad

Avanzado

## 🎓 Resultados de aprendizaje

- RA-6: describir el funcionamiento del algoritmo de selección e implementarlo
  correctamente.
- RA-7: reconocer un error de implementación en un algoritmo de ordenamiento.

## 💻 Código de partida

```python
numeros = [7, 2, 9, 1, 5]
cantidad = len(numeros)

for pasada in range(cantidad - 1):
    posicion_minimo = pasada
    for posicion in range(pasada + 1, cantidad):
        if numeros[posicion] < numeros[posicion_minimo]:
            pass  # ERROR: aquí falta recordar la nueva posición mínima encontrada
    # Intercambia el primero de la parte no ordenada con el mínimo encontrado
    numeros[pasada], numeros[posicion_minimo] = numeros[posicion_minimo], numeros[pasada]

print(numeros)
```

Con este error, el programa imprime `[7, 2, 9, 1, 5]` — la lista **sin cambios** —
porque `posicion_minimo` nunca se actualiza dentro del bucle interior: siempre vale
`pasada`, así que el intercambio final es "cambiar un elemento por sí mismo".
