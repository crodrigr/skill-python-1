# 🔴 Avanzado 01 — Calificaciones que podrían no existir

## 🧩 Problema

Escribe una función `leer_calificaciones(ruta)` que intente abrir y leer un archivo de
calificaciones (líneas `nombre,nota`), y:

- Si el archivo existe, muestre cada línea con el formato `"Ana: 6.5"`.
- Si el archivo **no** existe, muestre el mensaje
  `"No se encontró el archivo de calificaciones."` sin que el programa se detenga.

Prueba la función dos veces:

1. Primero, sin crear ningún archivo, llamando a `leer_calificaciones("calificaciones.txt")`
   (debe mostrar el mensaje de aviso).
2. Luego, crea `calificaciones.txt` con las líneas `"Ana,6.5"`, `"Luis,3.8"` y
   `"Eva,7.0"`, y vuelve a llamar a la función con la misma ruta (debe mostrar las tres
   calificaciones).

## 📥 Entrada

Ninguna al principio (el archivo no existe); luego, el propio programa crea
`calificaciones.txt` con las tres líneas indicadas.

## ⚙️ Proceso esperado

Definir `leer_calificaciones(ruta)` con `try`/`except FileNotFoundError` alrededor de
la apertura y lectura del archivo; llamarla antes y después de crear el archivo.

## 📤 Salida

Primero, el mensaje de aviso (archivo inexistente). Después de crear el archivo, las
tres calificaciones, una por línea, con el formato `"<nombre>: <nota>"`.

## 🚧 Restricciones

- El manejo del error debe hacerse con `try`/`except FileNotFoundError`, no
  comprobando "a mano" si el archivo existe antes de abrirlo.
- El programa no debe detenerse en ningún punto de la prueba.
- Los identificadores y comentarios deben estar en español.

## 📊 Dificultad

Avanzado

## 🎓 Resultados de aprendizaje

- RA-6: anticipar y gestionar `FileNotFoundError` con `try`/`except`.
