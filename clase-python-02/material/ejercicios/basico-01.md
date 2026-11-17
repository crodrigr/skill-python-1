# 🟢 Básico 01 — Definir y llamar una función

## 🧩 Problema

Escribe una función `mostrar_menu()` que imprima el menú de un cajero automático con tres
opciones. Luego llama a la función **dos veces**: una al inicio del programa y otra
después de imprimir una línea separadora.

## 📥 Entrada

- Ninguna. El menú es siempre igual y la función no recibe parámetros.

## ⚙️ Proceso esperado

1. Definir `mostrar_menu()` con `def`, sin parámetros.
2. En el cuerpo, imprimir las tres opciones (una por línea).
3. En el programa principal, llamar a `mostrar_menu()`, imprimir `"-----"` y volver a
   llamar a `mostrar_menu()`.

## 📤 Salida

Seis líneas de menú (tres por cada llamada) con la línea separadora en medio, por
ejemplo:

```text
1. Ver saldo
2. Depositar
3. Salir
-----
1. Ver saldo
2. Depositar
3. Salir
```

## 🚧 Restricciones

- La función no lleva parámetros ni `return`.
- El texto del menú se escribe **una sola vez** (dentro de la función).
- Identificadores y comentarios en español; nombre de la función con verbo.

## 📊 Dificultad

Básico

## 🎓 Resultados de aprendizaje

- RA-1: explicar qué es una función y cómo encapsula una acción.
- RA-2: definir una función con `def` e invocarla.
