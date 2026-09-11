# 🟢 Básico 02 — Bitácora de un viaje

## 🧩 Problema

Escribe un programa que:

1. Cree un archivo `bitacora.txt` en modo `'w'` con la línea `"Día 1: Salida desde la ciudad"`.
2. Agregue, en modo `'a'`, la línea `"Día 2: Llegada al primer destino"`.
3. Agregue, en modo `'a'`, la línea `"Día 3: Regreso"`.
4. Muestre el contenido completo del archivo al final.

## 📥 Entrada

Ninguna: las tres líneas de la bitácora van fijas en el código.

## ⚙️ Proceso esperado

Usar `'w'` solo para la primera escritura (que crea el archivo) y `'a'` para las dos
siguientes (que agregan sin borrar lo anterior); leer y mostrar el resultado con `'r'`.

## 📤 Salida

Las tres líneas de la bitácora, en orden, mostradas en pantalla.

## 🚧 Restricciones

- Usar `with` en cada apertura.
- No usar `'w'` más de una vez (eso borraría lo ya escrito).
- Los identificadores y comentarios deben estar en español.

## 📊 Dificultad

Básico

## 🎓 Resultados de aprendizaje

- RA-4: escribir y agregar contenido a un archivo distinguiendo `'w'` de `'a'`.
