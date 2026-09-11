# 🟡 Intermedio 01 — Separar nombre y precio

## 🧩 Problema

Un archivo `productos.txt` tiene, por línea, el nombre de un producto y su precio,
separados por una coma:

```text
arroz,1200
aceite,3500
azúcar,950
```

Escribe un programa que:

1. Cree `productos.txt` con esas tres líneas.
2. Lo lea, y para cada línea, quite el salto de línea y la divida por la coma para
   obtener el nombre y el precio por separado.
3. Muestre cada producto con el formato `"arroz cuesta 1200"`.

## 📥 Entrada

El archivo `productos.txt` descrito arriba; el programa lo crea al inicio.

## ⚙️ Proceso esperado

Leer las líneas con `readlines()` (o recorriendo el archivo con `for`); para cada
línea, usar `strip()` antes de `split(",")`, y mostrar el resultado con el formato
indicado.

## 📤 Salida

Tres líneas, una por producto, con el formato `"<nombre> cuesta <precio>"`.

## 🚧 Restricciones

- Usar `strip()` antes de `split(",")` en cada línea.
- No dejar el salto de línea ni espacios sobrantes en el nombre ni en el precio
  mostrados.
- Los identificadores y comentarios deben estar en español.

## 📊 Dificultad

Intermedio

## 🎓 Resultados de aprendizaje

- RA-5: quitar saltos de línea y dividir cada línea de un archivo con `split`.
