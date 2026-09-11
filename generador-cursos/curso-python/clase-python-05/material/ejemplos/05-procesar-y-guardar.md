# 💡 Ejemplo 05 — Procesar el contenido y guardarlo en otro archivo

**Tema**: `strip()` + `split()` para procesar datos leídos, y escribir el resultado en
un archivo distinto · **Resultado de aprendizaje**: RA-5 · **Nivel**: intermedio

## 🧩 Problema

Un archivo `temperaturas.txt` tiene, por línea, el nombre de una ciudad y su
temperatura en grados Celsius, separados por una coma. Se necesita convertir cada
temperatura a grados Fahrenheit y guardar el resultado en un nuevo archivo
`temperaturas_fahrenheit.txt`.

## 🔍 Análisis

- **Entrada**: `temperaturas.txt`, con líneas `ciudad,temperatura_celsius` (se crea por
  código al inicio del programa).
- **Proceso**: leer cada línea, quitar el salto de línea, dividirla por la coma,
  convertir la temperatura a Fahrenheit (`F = C * 9 / 5 + 32`), y armar una línea de
  salida por ciudad.
- **Salida**: el archivo `temperaturas_fahrenheit.txt` con las temperaturas
  convertidas, y un resumen en pantalla.

## 💡 Solución

1. Crear `temperaturas.txt` con tres ciudades y sus temperaturas en Celsius.
2. Leer el archivo, limpiar y dividir cada línea, y convertir la temperatura.
3. Escribir cada resultado en `temperaturas_fahrenheit.txt` y mostrarlo en pantalla.

## 💻 Código

```python
# Crear el archivo de entrada con datos fijos
with open("temperaturas.txt", "w") as archivo:
    archivo.write("Santiago,20\nLima,25\nBogotá,15\n")

# Leer, procesar y guardar el resultado
with open("temperaturas.txt", "r") as archivo_entrada:
    lineas = archivo_entrada.readlines()

with open("temperaturas_fahrenheit.txt", "w") as archivo_salida:
    for linea in lineas:
        ciudad, celsius_texto = linea.strip().split(",")
        celsius = float(celsius_texto)
        fahrenheit = celsius * 9 / 5 + 32

        linea_resultado = ciudad + "," + str(fahrenheit) + "\n"
        archivo_salida.write(linea_resultado)
        print(ciudad + ": " + str(celsius) + "°C = " + str(fahrenheit) + "°F")
```

## 🧭 Explicación paso a paso

1. Se crea `temperaturas.txt` con tres líneas `ciudad,temperatura_celsius`.
2. `readlines()` obtiene las tres líneas, cada una con su salto de línea final.
3. Para cada línea: `strip()` quita el salto de línea, y `split(",")` separa el nombre
   de la ciudad del texto de la temperatura, en una lista de dos elementos que se
   desempaqueta en `ciudad` y `celsius_texto`.
4. `float(celsius_texto)` convierte el texto (por ejemplo, `"20"`) en un número
   decimal, necesario para poder calcular con él.
5. `celsius * 9 / 5 + 32` aplica la fórmula de conversión.
6. Cada resultado se escribe como una nueva línea `ciudad,fahrenheit` en
   `temperaturas_fahrenheit.txt`, y también se muestra en pantalla en un formato más
   legible.

## ✅ Resultado esperado

```text
Santiago: 20.0°C = 68.0°F
Lima: 25.0°C = 77.0°F
Bogotá: 15.0°C = 59.0°F
```

**Archivo `temperaturas_fahrenheit.txt` resultante**:

```text
Santiago,68.0
Lima,77.0
Bogotá,59.0
```
