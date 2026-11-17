# 🟡 Intermedio 02 — Convertir con `try`/`except`/`else`

## 🧩 Problema

Escribe un programa que intente convertir un precio ingresado como texto a un número
decimal (`float`), mostrando un mensaje de error claro si el texto no es un número
válido, y el precio con un 10% de descuento aplicado si la conversión funcionó.

## 📥 Entrada

Dos casos de prueba fijos en el código: `"120.0"` (válido) y `"gratis"` (inválido).

## ⚙️ Proceso esperado

1. Para cada caso, intentar convertir el texto a `float` dentro de un `try`.
2. Si falla (`ValueError`), mostrar un mensaje indicando que el precio no es válido.
3. Si funciona, usar un bloque `else` para calcular el precio con 10% de descuento
   (`precio * 0.9`) y mostrarlo.

## 📤 Salida

Para `"120.0"`: el precio con descuento (`108.0`). Para `"gratis"`: un mensaje de
error, sin ningún cálculo de descuento.

## 🚧 Restricciones

- El cálculo del descuento DEBE estar en el bloque `else`, no dentro del `try`.
- Capturar específicamente `ValueError`; no usar `except:` sin tipo.

## 📊 Dificultad

Intermedio

## 🎓 Resultados de aprendizaje

- RA-5
- RA-6
