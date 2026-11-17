# 🔴 Avanzado 01 — Agrupar palabras por su letra inicial

## 🧩 Problema

Dada la lista `palabras = ["python", "perro", "casa", "carro", "banana", "barco", "python"]`,
escribe un programa que construya un diccionario donde cada **clave** sea una letra
inicial y cada **valor** sea la lista de palabras (en el orden en que aparecen) que
empiezan con esa letra, y lo muestre.

## 📥 Entrada

La lista `palabras` dada arriba, fija en el código.

## ⚙️ Proceso esperado

Recorrer `palabras` con un `for`. Para cada palabra, obtener su primera letra
(`palabra[0]`) y usar `setdefault(letra, [])` para asegurar que exista una lista vacía
la primera vez que aparece esa letra, y luego usar `append` sobre esa lista para agregar
la palabra.

## 📤 Salida

Un diccionario `letra -> lista de palabras`, por ejemplo (el orden de las claves sigue
el de la primera aparición de cada letra):
`{'p': ['python', 'perro', 'python'], 'c': ['casa', 'carro'], 'b': ['banana', 'barco']}`.

## 🚧 Restricciones

- Usar `setdefault` para crear la lista vacía solo la primera vez que aparece cada
  letra; no usar `if letra not in diccionario: ...`.
- No usar comprensiones de diccionarios ni de listas.
- Los identificadores y comentarios deben estar en español.

## 📊 Dificultad

Avanzado

## 🎓 Resultados de aprendizaje

- RA-7: usar `setdefault` para resolver una tarea de agrupación.
- RA-8: aplicar un diccionario a un problema práctico que requiere asociar datos por
  clave.
