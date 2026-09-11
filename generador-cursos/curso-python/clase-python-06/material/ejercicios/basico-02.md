# 🟢 Básico 02 — Recorrer una `deque` con `iter()`/`next()`

## 🧩 Problema

Crea una `collections.deque` con los nombres de 4 estaciones del año, en el orden
`["primavera", "verano", "otoño", "invierno"]`, y muéstralas una por una usando
`iter()`/`next()`, sin usar `for`.

## 📥 Entrada

La lista fija `["primavera", "verano", "otoño", "invierno"]`, convertida en
`collections.deque`.

## ⚙️ Proceso esperado

1. Crear la `deque` a partir de la lista.
2. Obtener su iterador con `iter()`.
3. Llamar a `next()` cuatro veces, mostrando cada estación con un mensaje del tipo
   `"Estación N: <nombre>"`.
4. Intentar una quinta llamada a `next()` dentro de un `try`/`except StopIteration`,
   mostrando un mensaje que indique que ya no quedan más estaciones.

## 📤 Salida

Cuatro líneas con las estaciones numeradas, seguidas de un mensaje indicando que la
`deque` se agotó.

## 🚧 Restricciones

- NO usar un bucle `for` para recorrer la `deque` (el objetivo es practicar `iter()`
  y `next()` manualmente).
- La quinta llamada a `next()` DEBE estar protegida con `try`/`except StopIteration`.

## 📊 Dificultad

Básico

## 🎓 Resultados de aprendizaje

- RA-4
