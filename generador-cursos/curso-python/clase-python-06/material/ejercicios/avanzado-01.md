# 🔴 Avanzado 01 — Dos tipos de error con `try`/`except`/`finally`

## 🧩 Problema

Un programa reparte una cantidad de puntos entre un número de participantes. Debe
manejar dos situaciones problemáticas: que la cantidad de participantes no sea un
número válido, y que sea cero (lo que provocaría una división entre cero).

## 📥 Entrada

Tres casos de prueba fijos en el código: `puntos = 100, participantes = "5"` (válido),
`puntos = 100, participantes = "cero_participantes"` (texto no numérico) y
`puntos = 100, participantes = "0"` (numérico pero cero).

## ⚙️ Proceso esperado

1. Convertir `participantes` a entero dentro de un `try`.
2. Calcular `puntos / participantes` (los puntos que le tocan a cada uno) dentro del
   mismo `try`.
3. Capturar `ValueError` si la conversión falla, y `ZeroDivisionError` si el número de
   participantes es cero, con un mensaje distinto para cada caso.
4. Usar un bloque `finally` que muestre siempre un mensaje indicando que el reparto
   terminó (haya tenido éxito o no).

## 📤 Salida

Para el caso válido: los puntos por participante. Para los otros dos: el mensaje de
error correspondiente. En los tres casos, el mensaje de `finally` se muestra al final.

## 🚧 Restricciones

- DEBES manejar `ValueError` y `ZeroDivisionError` con cláusulas `except` separadas
  (no una captura genérica que cubra ambos casos).
- El mensaje de `finally` DEBE aparecer en los tres casos de prueba.

## 📊 Dificultad

Avanzado

## 🎓 Resultados de aprendizaje

- RA-5
- RA-6
