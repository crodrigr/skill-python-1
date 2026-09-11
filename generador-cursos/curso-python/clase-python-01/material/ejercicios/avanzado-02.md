# 🔴 Avanzado 02 — Adivina el número

## 🧩 Problema

El programa tiene un número secreto guardado en una variable (por ejemplo, `7`). Hay una
lista fija de intentos que se van probando **uno a uno** hasta acertar o hasta quedarse
sin intentos. Para cada intento, el programa indica si es `muy bajo`, `muy alto` o
`correcto`. Al final informa si se adivinó y en cuántos intentos.

Para simplificar, los intentos se recorren desde una variable `intento` que empieza en
`1` y aumenta de a `2` en cada vuelta (`1, 3, 5, 7, ...`), y el número secreto es `7`.

## 📥 Entrada

- `numero_secreto` (`int`), fijado en el código (`7`).
- `intento` inicial (`int`) y el paso de aumento, fijados en el código.
- `maximo_valor` (`int`): valor máximo que puede tomar `intento` antes de rendirse
  (por ejemplo, `9`).

## ⚙️ Proceso esperado

1. Usar un bucle `while` que se repita **mientras** `intento <= maximo_valor` y todavía
   no se haya acertado.
2. En cada vuelta, comparar `intento` con `numero_secreto` usando `if` / `elif` / `else`
   y mostrar el mensaje correspondiente.
3. Llevar un contador de intentos y una variable booleana `adivinado`.
4. Aumentar `intento` en cada vuelta (para evitar un bucle infinito).

## 📤 Salida

Varias líneas: un mensaje por intento y un resumen final. Ejemplo:

```text
Intento 1 (valor 1): muy bajo
Intento 2 (valor 3): muy bajo
Intento 3 (valor 5): muy bajo
Intento 4 (valor 7): correcto
Adivinado en 4 intentos
```

## 🚧 Restricciones

- Debe usarse un bucle `while` (no se sabe de antemano en qué vuelta se acierta).
- Debe combinarse el bucle con un `if` / `elif` / `else` y operadores de comparación.
- El valor de `intento` debe cambiar dentro del bucle.
- Identificadores y comentarios en español.

## 📊 Dificultad

Avanzado

## 🎓 Resultados de aprendizaje

- RA-6: usar un bucle `while` para repetir un proceso.
- RA-7: reconocer que `while` es adecuado cuando el final depende de una condición.
- RA-8: combinar bucle, condicional y operadores para resolver el problema.
