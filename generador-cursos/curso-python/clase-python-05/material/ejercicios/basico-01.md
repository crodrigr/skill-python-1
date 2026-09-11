# 🟢 Básico 01 — Guardar y mostrar una lista de compras

## 🧩 Problema

Escribe un programa que:

1. Cree un archivo `compras.txt` y, usando `with` y `write()`, guarde tres productos,
   uno por línea: `"arroz"`, `"aceite"`, `"leche"`.
2. Abra de nuevo `compras.txt` con `with`, en modo lectura.
3. Muestre el contenido completo del archivo con `read()`.

## 📥 Entrada

Ninguna: la lista de productos va fija en el código; el programa crea su propio archivo
de entrada.

## ⚙️ Proceso esperado

Usar `with open("compras.txt", "w") as archivo:` para escribir los tres productos
(cada uno terminado en salto de línea), y un segundo bloque
`with open("compras.txt", "r") as archivo:` para leer y mostrar el contenido completo.

## 📤 Salida

El contenido completo de `compras.txt`, mostrado en pantalla exactamente como quedó
guardado.

## 🚧 Restricciones

- Usar `with` para abrir el archivo, tanto para escribir como para leer; no usar
  `open()`/`close()` manual.
- Cada producto debe quedar en su propia línea dentro del archivo.
- Los identificadores y comentarios deben estar en español.

## 📊 Dificultad

Básico

## 🎓 Resultados de aprendizaje

- RA-2: abrir y cerrar un archivo de forma segura con `with`.
- RA-3: leer el contenido completo de un archivo con `read()`.
