# 💡 Ejemplo 03 — Escribir y sobrescribir

**Tema**: modo `'w'` y su efecto de sobrescritura · **Resultado de aprendizaje**: RA-4
· **Nivel**: introductorio

## 🧩 Problema

Se escribe un reporte en un archivo. Más tarde, se genera un reporte nuevo y se guarda
en el mismo archivo, en modo `'w'`. Se quiere comprobar qué pasa con el contenido
anterior.

## 🔍 Análisis

- **Entrada**: dos versiones de un reporte, fijas en el código.
- **Proceso**: escribir la primera versión en modo `'w'`; leer y mostrar el archivo;
  escribir la segunda versión en modo `'w'` sobre el mismo archivo; leer y mostrar de
  nuevo.
- **Salida**: el contenido del archivo antes y después de la segunda escritura.

## 💡 Solución

1. Escribir el primer reporte en `reporte.txt` con modo `'w'`.
2. Leer y mostrar el contenido para confirmarlo.
3. Escribir un segundo reporte, distinto, también en modo `'w'`.
4. Leer y mostrar el contenido de nuevo para comprobar que el primero desapareció.

## 💻 Código

```python
# Primera escritura
with open("reporte.txt", "w") as archivo:
    archivo.write("Reporte de la mañana\nVentas: 500\n")

with open("reporte.txt", "r") as archivo:
    print("Después de la primera escritura:")
    print(archivo.read())

# Segunda escritura en modo 'w': sobrescribe por completo
with open("reporte.txt", "w") as archivo:
    archivo.write("Reporte de la tarde\nVentas: 800\n")

with open("reporte.txt", "r") as archivo:
    print("Después de la segunda escritura:")
    print(archivo.read())
```

## 🧭 Explicación paso a paso

1. La primera escritura en modo `'w'` crea `reporte.txt` con el reporte de la mañana.
2. La primera lectura confirma que el archivo contiene ese reporte.
3. La segunda escritura vuelve a abrir `reporte.txt` en modo `'w'`: como el archivo ya
   existía, Python lo **vacía por completo** antes de escribir el nuevo contenido — el
   reporte de la mañana no queda mezclado con el de la tarde ni conservado en ningún
   lado.
4. La segunda lectura confirma que el contenido final es únicamente el reporte de la
   tarde.

## ✅ Resultado esperado

```text
Después de la primera escritura:
Reporte de la mañana
Ventas: 500

Después de la segunda escritura:
Reporte de la tarde
Ventas: 800

```

**Archivo `reporte.txt` resultante (al final del programa)**:

```text
Reporte de la tarde
Ventas: 800
```
