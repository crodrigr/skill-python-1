# 💡 Ejemplo 06 — Ordenamiento por burbuja, paso a paso

**Tema**: algoritmo de ordenamiento por burbuja implementado con bucles anidados ·
**Resultado de aprendizaje**: RA-6, RA-7 · **Nivel**: intermedio-avanzado

## 🧩 Problema

Se quiere ordenar de menor a mayor la lista `[5, 1, 4, 2, 8]` usando el algoritmo de
ordenamiento por burbuja, implementado a mano (sin `sort`/`sorted`), mostrando el estado
completo de la lista después de cada pasada para poder seguir el proceso.

## 🔍 Análisis

- **Entrada**: lista de números sin ordenar.
- **Proceso**: recorrer la lista varias veces (pasadas); en cada pasada, comparar cada
  par de elementos vecinos y, si el de la izquierda es mayor que el de la derecha,
  intercambiarlos.
- **Salida**: el estado de la lista después de cada pasada y la lista final ordenada.

## 💡 Solución

1. Usar un bucle exterior que controla cuántas pasadas se hacen (como máximo, una menos
   que la cantidad de elementos).
2. Usar un bucle interior que recorre los pares de elementos vecinos aún no fijados,
   comparando e intercambiando cuando corresponde.
3. Mostrar la lista al final de cada pasada exterior.

## 💻 Código

```python
numeros = [5, 1, 4, 2, 8]
cantidad = len(numeros)

# Bucle exterior: una pasada completa por vuelta
for pasada in range(cantidad - 1):
    # Bucle interior: compara cada par de vecinos no fijados todavía
    for posicion in range(cantidad - 1 - pasada):
        if numeros[posicion] > numeros[posicion + 1]:
            # Intercambio de posiciones (swap)
            numeros[posicion], numeros[posicion + 1] = numeros[posicion + 1], numeros[posicion]

    print("Después de la pasada", pasada + 1, ":", numeros)

print("Lista ordenada:", numeros)
```

## 🧭 Explicación paso a paso

1. `cantidad - 1` pasadas son suficientes como máximo: si hay 5 elementos, con 4 pasadas
   la lista queda garantizada como ordenada.
2. En cada pasada, el bucle interior recorre desde el principio hasta el último par de
   elementos que **todavía no están fijados** (`cantidad - 1 - pasada`): con cada
   pasada, el elemento más grande restante "sube" a su posición final, así que no hace
   falta volver a compararlo.
3. `numeros[posicion], numeros[posicion + 1] = numeros[posicion + 1], numeros[posicion]`
   intercambia los dos valores en una sola línea (asignación múltiple de Python).
4. Al imprimir después de cada pasada se puede seguir cómo el mayor elemento restante
   llega a su lugar en cada vuelta:
   - Pasada 1: el `8` (el mayor de toda la lista) llega a la última posición.
   - Pasada 2: el `5` (el mayor de lo que queda) llega a la penúltima posición.
   - Y así sucesivamente, hasta que no queda nada por mover.

## ✅ Resultado esperado

```text
Después de la pasada 1 : [1, 4, 2, 5, 8]
Después de la pasada 2 : [1, 2, 4, 5, 8]
Después de la pasada 3 : [1, 2, 4, 5, 8]
Después de la pasada 4 : [1, 2, 4, 5, 8]
Lista ordenada: [1, 2, 4, 5, 8]
```
