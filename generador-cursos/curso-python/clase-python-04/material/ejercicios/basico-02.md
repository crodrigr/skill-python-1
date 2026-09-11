# 🟢 Básico 02 — Consultas sobre un diccionario de capitales

## 🧩 Problema

Dado el diccionario `capitales = {"Chile": "Santiago", "Perú": "Lima", "Argentina": "Buenos Aires"}`,
escribe un programa que:

1. Muestre cuántos países tiene registrados el diccionario.
2. Compruebe si `"Bolivia"` está entre las claves y muestre el resultado.
3. Muestre la capital de `"Perú"` usando `get`, con `"Desconocida"` como valor por
   defecto.
4. Muestre la capital de `"Bolivia"` usando `get`, con `"Desconocida"` como valor por
   defecto (para comprobar que sí funciona el valor por defecto).

## 📥 Entrada

El diccionario `capitales` dado arriba, fijo en el código.

## ⚙️ Proceso esperado

Usar `len` sobre el diccionario, `in` para comprobar la clave, y `get` con un valor por
defecto para las dos consultas de capital.

## 📤 Salida

Cuatro líneas: la cantidad de países registrados, si `"Bolivia"` está presente, la
capital de Perú, y la capital de Bolivia (el valor por defecto).

## 🚧 Restricciones

- Usar exclusivamente `len`, `in` y `get`; no usar `diccionario[clave]` directo en
  este ejercicio.
- Los identificadores y comentarios deben estar en español.

## 📊 Dificultad

Básico

## 🎓 Resultados de aprendizaje

- RA-3: acceder a un valor por su clave, incluido el manejo de una clave inexistente
  con `get`.
