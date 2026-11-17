# 💡 Ejemplo 02 — Operadores

**Tema**: operadores aritméticos, de comparación y lógicos · **Resultado de aprendizaje**: RA-4
· **Nivel**: introductorio (segundo de la secuencia)

## 🧩 Problema

En un juego, un jugador gana puntos por nivel superado. Queremos, a partir de los puntos
actuales y los puntos de la última partida:

1. calcular el total de puntos,
2. saber cuántos niveles completos alcanzó (cada nivel cuesta 100 puntos) y cuántos
   puntos le sobran,
3. indicar si superó el récord de la casa (500 puntos) **y** si jugó la partida de hoy.

## 🔍 Análisis

- **Entrada**: `puntos_previos` (`int`), `puntos_partida` (`int`), `jugo_hoy` (`bool`).
- **Proceso**: suma (`+`), división entera (`//`), resto (`%`), comparación (`>`) y
  operador lógico (`and`).
- **Salida**: total de puntos, niveles y puntos sobrantes, y un valor `True`/`False`
  que indica si batió el récord jugando hoy.

## 💡 Solución

1. Sumar los puntos con `+`.
2. Usar `//` para los niveles completos y `%` para los puntos sobrantes.
3. Combinar una comparación (`total > 500`) con `jugo_hoy` mediante `and`.

## 💻 Código

```python
# Entrada
puntos_previos = 380
puntos_partida = 260
jugo_hoy = True

# Proceso
total_puntos = puntos_previos + puntos_partida
niveles_completos = total_puntos // 100
puntos_sobrantes = total_puntos % 100
batio_record_hoy = (total_puntos > 500) and jugo_hoy

# Salida
print("Total de puntos:", total_puntos)
print("Niveles completos:", niveles_completos)
print("Puntos sobrantes:", puntos_sobrantes)
print("¿Batió el récord jugando hoy?:", batio_record_hoy)
```

## 🧭 Explicación paso a paso

1. `total_puntos = 380 + 260` → `640`.
2. `niveles_completos = 640 // 100` → `6` (la división entera descarta los decimales).
3. `puntos_sobrantes = 640 % 100` → `40` (el resto de dividir 640 entre 100).
4. `total_puntos > 500` → `640 > 500` → `True`. Luego `True and jugo_hoy` → `True and
   True` → `True`.
5. Los `print` muestran cada resultado. El último muestra un valor de tipo `bool`.

## ✅ Resultado esperado

```text
Total de puntos: 640
Niveles completos: 6
Puntos sobrantes: 40
¿Batió el récord jugando hoy?: True
```
