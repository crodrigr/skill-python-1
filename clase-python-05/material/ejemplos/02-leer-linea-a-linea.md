# 💡 Ejemplo 02 — Leer línea a línea

**Tema**: `readlines()` y recorrido con `for`, numerando cada línea · **Resultado de
aprendizaje**: RA-3 · **Nivel**: introductorio

## 🧩 Problema

Un archivo tiene una lista de tareas pendientes, una por línea. Se quiere mostrar cada
tarea numerada, como una lista ordenada.

## 🔍 Análisis

- **Entrada**: un archivo `tareas.txt` con varias líneas, cada una con una tarea (se
  crea por código al inicio del programa).
- **Proceso**: leer todas las líneas con `readlines()` y recorrerlas con `for`,
  numerando cada una.
- **Salida**: cada tarea, precedida por su número, en pantalla.

## 💡 Solución

1. Crear `tareas.txt` con tres líneas de ejemplo.
2. Abrirlo para lectura y obtener la lista de líneas con `readlines()`.
3. Recorrer la lista con un bucle `for` que también lleve la posición, para numerar
   cada tarea desde 1.

## 💻 Código

```python
# Crear el archivo de tareas con contenido fijo
with open("tareas.txt", "w") as archivo:
    archivo.write("Comprar pan\nPagar cuentas\nEstudiar Python\n")

# Leer todas las líneas del archivo
with open("tareas.txt", "r") as archivo:
    lineas = archivo.readlines()

for indice in range(len(lineas)):
    print(str(indice + 1) + ". " + lineas[indice].strip())
```

## 🧭 Explicación paso a paso

1. `tareas.txt` se crea con tres líneas, cada una terminada en `\n`.
2. `archivo.readlines()` devuelve una lista con las tres líneas, cada elemento
   incluyendo su salto de línea final (por ejemplo, `"Comprar pan\n"`).
3. `range(len(lineas))` genera los índices `0`, `1` y `2`; en cada vuelta,
   `lineas[indice]` da la línea correspondiente.
4. `lineas[indice].strip()` quita el salto de línea (y cualquier espacio sobrante) antes
   de mostrarla, para que no queden líneas en blanco de más en la salida.
5. `str(indice + 1) + ". "` antepone el número de tarea, empezando en 1 en vez de 0.

## ✅ Resultado esperado

```text
1. Comprar pan
2. Pagar cuentas
3. Estudiar Python
```

**Archivo `tareas.txt` resultante**:

```text
Comprar pan
Pagar cuentas
Estudiar Python
```
