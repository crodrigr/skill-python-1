# 🏆 Desafío 01 — Reservas de boletos de cine

## 🧩 Problema

Un cine quiere un mini sistema de reservas de boletos. Cada película tiene un precio y
una cantidad de cupos disponibles. El sistema debe mostrar la cartelera, permitir
reservar boletos para una película, y manejar los errores comunes: una cantidad de
boletos mal escrita, una película que no está en cartelera, y una reserva que pide más
boletos de los cupos disponibles.

## 📥 Entrada

- Un módulo propio `cartelera.py` con el precio y los cupos disponibles de al menos 3
  películas (tú eliges los nombres y valores).
- Cuatro intentos de reserva de prueba: uno válido, uno con cantidad no numérica, uno
  con una película que no existe en la cartelera, y uno que pide más boletos de los
  cupos disponibles.

## ⚙️ Proceso esperado

1. Crear `cartelera.py` con los datos de las películas (precio y cupos) y funciones
   para mostrar la cartelera, buscar el precio de una película y consultar sus cupos
   disponibles.
2. Desde el script principal, importar el módulo y mostrar la cartelera completa
   iterando sobre ella.
3. Definir una función de reserva que reciba una película y una cantidad (como texto),
   maneje con `try`/`except` la conversión de la cantidad y la búsqueda de la
   película, y — solo si ambas tuvieron éxito (bloque `else`) — verifique si hay
   cupos suficientes antes de confirmar la reserva.
4. Usar un bloque `finally` que muestre siempre un mensaje indicando que el intento de
   reserva terminó.

## 📤 Salida

Para cada uno de los cuatro casos de prueba, un mensaje que indique claramente el
resultado (reserva confirmada con el total a pagar, cantidad inválida, película
inexistente, o cupos insuficientes), y en todos los casos, el mensaje final de
`finally`.

## 🚧 Restricciones

- El catálogo de películas (precio y cupos) DEBE vivir en el módulo propio, no en el
  script principal.
- DEBES manejar por separado la cantidad inválida (`ValueError`) y la película
  inexistente (`KeyError`); la verificación de cupos insuficientes puede resolverse
  con una condición dentro del `else`, sin necesidad de una excepción nueva.
- El `finally` DEBE ejecutarse en los cuatro casos de prueba.

## 📊 Dificultad

Desafío

## 🎓 Resultados de aprendizaje

- RA-2
- RA-3
- RA-4
- RA-5
- RA-6
- RA-7

## 🧪 Casos de prueba

| Película | Cantidad | Resultado esperado |
|---|---|---|
| Una película en cartelera, con cupos suficientes | Un número válido menor o igual a los cupos | Reserva confirmada con el total correcto |
| Una película en cartelera | Un texto no numérico | Mensaje de cantidad inválida |
| Una película que NO está en la cartelera | Cualquier cantidad | Mensaje de película inexistente |
| Una película en cartelera, con pocos o cero cupos | Un número mayor a los cupos disponibles | Mensaje de cupos insuficientes |
