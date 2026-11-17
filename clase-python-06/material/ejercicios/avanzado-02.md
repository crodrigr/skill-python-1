# 🔴 Avanzado 02 — Extender un módulo propio con manejo de errores

## 🧩 Problema

Retoma el módulo `matematicas.py` del Ejemplo 02 (que ya tiene `cuadrado` y `cubo`) y
agrégale una nueva función `raiz_cuadrada(numero)` que use `math.sqrt`. Desde el script
principal, calcula la raíz cuadrada de varios números, manejando el caso de un número
negativo (que no tiene raíz cuadrada real).

## 📥 Entrada

El módulo `matematicas.py` ampliado con `raiz_cuadrada(numero)` (usando
`math.sqrt(numero)`). El script principal prueba con `16` (válido) y `-4` (inválido).

## ⚙️ Proceso esperado

1. Agregar `raiz_cuadrada(numero)` a `matematicas.py`, usando el módulo `math` de la
   biblioteca estándar.
2. Desde el script principal, importar `matematicas` y llamar a `raiz_cuadrada` para
   cada número de prueba, dentro de un `try`/`except`.
3. Capturar el error que se produce al calcular la raíz cuadrada de un número
   negativo, mostrando un mensaje claro en vez de dejar que el programa se detenga.

## 📤 Salida

Para `16`: el resultado de la raíz cuadrada (`4.0`). Para `-4`: un mensaje indicando
que no se puede calcular la raíz cuadrada de un número negativo.

## 🚧 Restricciones

- `raiz_cuadrada` DEBE vivir en `matematicas.py`, junto a `cuadrado` y `cubo`, no en el
  script principal.
- El manejo del número negativo DEBE hacerse con `try`/`except`, capturando el tipo de
  excepción correcto (pista: prueba qué excepción lanza `math.sqrt` con un número
  negativo).

## 📊 Dificultad

Avanzado

## 🎓 Resultados de aprendizaje

- RA-2
- RA-5
