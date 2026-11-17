# 🔴 Avanzado 02 — De lista de tuplas a diccionario

## 🧩 Problema

Un sistema entrega las calificaciones como una lista de tuplas `(nombre, nota)` — el
mismo formato usado en la Clase 03 —, pero algunos estudiantes quedaron registrados más
de una vez (con su nota corregida en el segundo registro):

```python
registros = [("Ana", 6.5), ("Luis", 3.8), ("Eva", 5.0), ("Ana", 7.0)]
```

Escribe un programa que:

1. Convierta `registros` en un diccionario `calificaciones` (`nombre -> nota`),
   recorriendo la lista de tuplas y desempaquetando cada una.
2. Muestre el diccionario resultante y explique (en un comentario) qué pasó con la nota
   de `"Ana"`.
3. Consulte con `get` la nota de `"Marco"` (que no está registrado), mostrando
   `"sin registro"` si no existe.

## 📥 Entrada

La lista `registros` dada arriba, fija en el código.

## ⚙️ Proceso esperado

Recorrer `registros` con `for nombre, nota in registros:` y asignar
`calificaciones[nombre] = nota` en cada vuelta; usar `get` para la consulta final.

## 📤 Salida

El diccionario `calificaciones` (con la nota final de cada estudiante) y el resultado
de consultar a `"Marco"`.

## 🚧 Restricciones

- No usar `dict(registros)` ni comprensiones de diccionarios: la conversión debe
  hacerse con un bucle explícito.
- Los identificadores y comentarios deben estar en español.

## 📊 Dificultad

Avanzado

## 🎓 Resultados de aprendizaje

- RA-4: agregar y modificar elementos de un diccionario por asignación.
- RA-8: aplicar un diccionario a un problema práctico, combinándolo con una estructura
  ya vista (una lista de tuplas).
