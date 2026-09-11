# 🟡 Intermedio 02 — Contar líneas y palabras

## 🧩 Problema

Un archivo `parrafo.txt` contiene varias líneas de texto. Escribe un programa que:

1. Cree `parrafo.txt` con el siguiente contenido (tres líneas):

   ```text
   Python es un lenguaje de programación
   Se usa para análisis de datos y automatización
   Aprenderlo abre muchas puertas
   ```

2. Cuente cuántas líneas tiene el archivo.
3. Cuente cuántas palabras tiene en total (sumando las palabras de todas las líneas).

## 📥 Entrada

El archivo `parrafo.txt` descrito arriba; el programa lo crea al inicio.

## ⚙️ Proceso esperado

Leer las líneas con `readlines()` y usar `len(...)` sobre la lista para contar líneas;
para las palabras, recorrer cada línea, usar `split()` (sin argumento, que separa por
espacios) y sumar `len(...)` de cada lista de palabras a un acumulador.

## 📤 Salida

Dos líneas: la cantidad de líneas del archivo y la cantidad total de palabras.

## 🚧 Restricciones

- No contar palabras "a mano" leyendo carácter por carácter: usar `split()`.
- Los identificadores y comentarios deben estar en español.

## 📊 Dificultad

Intermedio

## 🎓 Resultados de aprendizaje

- RA-5: procesar el contenido de un archivo (dividir en palabras) para calcular un
  resultado.
