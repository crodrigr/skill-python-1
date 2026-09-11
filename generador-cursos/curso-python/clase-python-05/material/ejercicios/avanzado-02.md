# 🔴 Avanzado 02 — Resumen de gastos por categoría

## 🧩 Problema

Un archivo `gastos.txt` tiene, por línea, una categoría de gasto y un monto, separados
por una coma (una categoría puede repetirse en varias líneas):

```text
comida,15000
transporte,8000
comida,5000
ocio,12000
transporte,3000
```

Escribe un programa que:

1. Cree `gastos.txt` con esas cinco líneas.
2. Lo lea y, usando un diccionario `categoria -> total_gastado` (como en la Clase 04),
   sume los montos de cada categoría.
3. Escriba el resultado en `resumen_gastos.txt`, con una línea por categoría en el
   formato `categoria:total`.

## 📥 Entrada

El archivo `gastos.txt` descrito arriba; el programa lo crea al inicio.

## ⚙️ Proceso esperado

Leer y procesar cada línea (`strip`+`split(",")`); acumular los montos en un
diccionario usando `get(categoria, 0)` o `setdefault`; recorrer el diccionario con
`items()` para escribir el resumen.

## 📤 Salida

El archivo `resumen_gastos.txt` con el total por categoría, y el mismo resumen
mostrado en pantalla.

## 🚧 Restricciones

- La acumulación por categoría debe hacerse con un diccionario, no con variables
  sueltas por categoría.
- Los montos deben convertirse a número (`int`) antes de sumarlos.
- Los identificadores y comentarios deben estar en español.

## 📊 Dificultad

Avanzado

## 🎓 Resultados de aprendizaje

- RA-5: procesar el contenido de un archivo y transformar los datos.
- RA-7: combinar lectura, procesamiento y escritura en un solo programa.
