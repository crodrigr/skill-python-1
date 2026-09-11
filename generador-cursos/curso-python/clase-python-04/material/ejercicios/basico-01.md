# 🟢 Básico 01 — Agenda de contactos

## 🧩 Problema

Escribe un programa que:

1. Cree un diccionario `agenda` con tres contactos: `"Ana": "555-1234"`,
   `"Luis": "555-5678"`, `"Eva": "555-9012"`.
2. Agregue un contacto nuevo: `"Marco": "555-3456"`.
3. Modifique el número de `"Ana"` a `"555-0000"` (cambió de número).
4. Muestre el diccionario completo al final, y también cuántos contactos tiene.

## 📥 Entrada

Ninguna: los contactos van fijos en el código.

## ⚙️ Proceso esperado

Crear el diccionario con `{}`; agregar el contacto nuevo y modificar el de Ana usando
asignación por clave (`agenda[clave] = valor`); usar `len` para contar los contactos.

## 📤 Salida

El diccionario final de contactos y la cantidad de contactos que contiene.

## 🚧 Restricciones

- Crear el diccionario inicial con `{}`, no con `dict()`.
- Agregar y modificar deben hacerse con asignación por clave, no recreando el
  diccionario completo.
- Los identificadores y comentarios deben estar en español.
- No usar `input`: los datos van fijos en el código.

## 📊 Dificultad

Básico

## 🎓 Resultados de aprendizaje

- RA-2: crear un diccionario con pares clave-valor.
- RA-4: agregar y modificar elementos de un diccionario por asignación.
