# 🟡 Intermedio 01 — Contar votos con `Counter`

## 🧩 Problema

En una votación informal, cada persona elige un color favorito entre varias opciones.
Los votos ya están registrados en una lista. Usa `collections.Counter` para saber
cuántos votos recibió cada color y cuál fue el más votado.

## 📥 Entrada

La lista fija:

```python
votos = ["azul", "rojo", "azul", "verde", "rojo", "azul"]
```

## ⚙️ Proceso esperado

1. Crear un `collections.Counter` a partir de la lista `votos`.
2. Mostrar el conteo completo (cuántos votos tiene cada color).
3. Determinar y mostrar cuál color tiene más votos y cuántos recibió (el método
   `most_common()` de `Counter` puede ayudarte, aunque no es obligatorio usarlo).

## 📤 Salida

El conteo por color y una línea final indicando el color ganador y su cantidad de
votos (por ejemplo, `"El color mas votado es azul con 3 votos"`).

## 🚧 Restricciones

- DEBES usar `collections.Counter`; no calcules el conteo contando manualmente con
  bucles y variables sueltas por color.
- La lista de votos queda fija en el código, tal como se dio en la Entrada.

## 📊 Dificultad

Intermedio

## 🎓 Resultados de aprendizaje

- RA-3
