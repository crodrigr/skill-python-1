# 💡 Ejemplo 01 — Leer un archivo completo

**Tema**: crear un archivo con `with`, abrirlo y leer todo su contenido con `read()` ·
**Resultado de aprendizaje**: RA-2, RA-3 · **Nivel**: introductorio (primero de la
secuencia)

## 🧩 Problema

Se quiere guardar una breve nota en un archivo de texto y, en un paso separado del
programa, volver a abrir ese archivo y mostrar todo su contenido en pantalla.

## 🔍 Análisis

- **Entrada**: el texto de la nota, fijo en el código.
- **Proceso**: crear el archivo `notas.txt` escribiendo la nota; abrirlo de nuevo para
  lectura y leer todo su contenido con `read()`.
- **Salida**: el contenido completo del archivo, mostrado en pantalla.

## 💡 Solución

1. Abrir `notas.txt` en modo `'w'` con `with` y escribir la nota.
2. Abrir `notas.txt` en modo `'r'` con `with` y leer todo el contenido con `read()`.
3. Mostrar el contenido leído.

## 💻 Código

```python
# Paso 1: crear el archivo con una nota
with open("notas.txt", "w") as archivo:
    archivo.write("Reunión de equipo a las 10:00\nRevisar el informe mensual\n")

# Paso 2: abrir el mismo archivo para lectura y leer todo su contenido
with open("notas.txt", "r") as archivo:
    contenido = archivo.read()

print("Contenido de notas.txt:")
print(contenido)
```

## 🧭 Explicación paso a paso

1. El primer `with open("notas.txt", "w") as archivo:` crea (o sobrescribe) el archivo
   `notas.txt` y escribe dos líneas de texto con `write()`; al salir del bloque `with`,
   el archivo se cierra y los datos quedan guardados en disco.
2. El segundo `with open("notas.txt", "r") as archivo:` abre el mismo archivo, ahora
   para lectura; como ya existe (se acaba de crear en el paso 1), la apertura funciona
   sin problema.
3. `archivo.read()` devuelve **todo** el contenido del archivo como un único texto,
   incluidos los saltos de línea (`\n`) que separan cada nota.
4. `print(contenido)` muestra ese texto tal como quedó guardado.

## ✅ Resultado esperado

```text
Contenido de notas.txt:
Reunión de equipo a las 10:00
Revisar el informe mensual

```

**Archivo `notas.txt` resultante**:

```text
Reunión de equipo a las 10:00
Revisar el informe mensual
```
