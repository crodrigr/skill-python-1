# Ejemplo 06 — Bucle `while`

**Tema**: repetición controlada por una condición; combinación de bucle, condicional y
operadores; riesgo de bucle infinito · **Resultados de aprendizaje**: RA-6, RA-7, RA-8 ·
**Nivel**: avanzado (sexto y último de la secuencia)

## Problema

Un juego de dardos suma los puntos de cada lanzamiento. El jugador sigue lanzando
**mientras** su puntaje total sea menor a 50. Cada lanzamiento suma 7 puntos. El
programa debe mostrar el puntaje después de cada lanzamiento, avisar cuando un
lanzamiento deja el total en 50 o más, y al final informar cuántos lanzamientos hizo.

## Análisis

- **Entrada**: puntos por lanzamiento (`7`, fijo) y meta (`50`, fijo).
- **Proceso**: repetir **hasta** llegar a la meta. No se sabe de antemano cuántos
  lanzamientos harán falta → `while`. En cada vuelta, un `if` comprueba si ya se alcanzó
  la meta.
- **Salida**: el puntaje tras cada lanzamiento, un aviso al alcanzar la meta y el total
  de lanzamientos.

## Solución

Dos variables de control: `puntaje` (acumulador) y `lanzamientos` (contador). La
condición del `while` es `puntaje < 50`. Dentro del bucle **siempre** sumamos puntos y
aumentamos el contador: eso garantiza que la condición terminará siendo falsa y el bucle
terminará.

## Código

```python
puntos_por_lanzamiento = 7
meta = 50

puntaje = 0
lanzamientos = 0

while puntaje < meta:
    puntaje = puntaje + puntos_por_lanzamiento
    lanzamientos = lanzamientos + 1
    print("Lanzamiento", lanzamientos, "- puntaje:", puntaje)

    if puntaje >= meta:
        print("¡Meta alcanzada!")

print("Total de lanzamientos:", lanzamientos)
```

## Explicación paso a paso

1. `puntaje = 0`, `lanzamientos = 0`.
2. Se evalúa la condición `puntaje < meta` (`0 < 50` → `True`) y se entra al bucle.
3. Cada vuelta suma 7 al puntaje y 1 al contador:
   - Vuelta 1 → `puntaje = 7`; vuelta 2 → `14`; … vuelta 7 → `49`.
   - Con `49 < 50` todavía `True`, entra la vuelta 8 → `puntaje = 56`.
4. En la vuelta 8, el `if puntaje >= meta` (`56 >= 50` → `True`) muestra "¡Meta
   alcanzada!".
5. Se vuelve a evaluar la condición del `while`: `56 < 50` → `False`. El bucle termina.
6. `print` final: `lanzamientos` vale `8`.
7. La línea `lanzamientos = lanzamientos + 1` es la que evita el **bucle infinito**: sin
   modificar `puntaje` dentro del bucle, la condición sería siempre verdadera.

## Resultado esperado

```text
Lanzamiento 1 - puntaje: 7
Lanzamiento 2 - puntaje: 14
Lanzamiento 3 - puntaje: 21
Lanzamiento 4 - puntaje: 28
Lanzamiento 5 - puntaje: 35
Lanzamiento 6 - puntaje: 42
Lanzamiento 7 - puntaje: 49
Lanzamiento 8 - puntaje: 56
¡Meta alcanzada!
Total de lanzamientos: 8
```
