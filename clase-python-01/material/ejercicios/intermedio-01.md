# 🟡 Intermedio 01 — ¿Mayor de edad?

## 🧩 Problema

Un sitio web exige que la persona sea **mayor de edad** (18 años o más) y que **acepte
los términos** para registrarse. Escribe un programa que, a partir de la edad y de si
aceptó los términos, muestre uno de estos mensajes:

- `Registro permitido` si cumple ambas condiciones.
- `Debe ser mayor de edad` si tiene menos de 18 (haya aceptado o no).
- `Debe aceptar los términos` si es mayor de edad pero no aceptó.

## 📥 Entrada

- `edad` (`int`), fijada en el código.
- `acepto_terminos` (`bool`), fijada en el código.

## ⚙️ Proceso esperado

1. Evaluar la condición de edad con un operador de comparación.
2. Combinar las dos condiciones con un operador lógico para el primer caso.
3. Usar `if` / `elif` / `else` para elegir un único mensaje.

## 📤 Salida

Una línea con el mensaje correspondiente. Ejemplo, para `edad = 20` y
`acepto_terminos = False`:

```text
Debe aceptar los términos
```

## 🚧 Restricciones

- Debe resolverse con una sola estructura `if/elif/else`.
- Usa al menos un operador de comparación y un operador lógico.
- Identificadores y comentarios en español.

## 📊 Dificultad

Intermedio

## 🎓 Resultados de aprendizaje

- RA-4: usar operadores de comparación y lógicos.
- RA-5: usar estructuras condicionales para tomar decisiones.
