# 💡 Ejemplo 04 — Condicional

**Tema**: expresiones booleanas y estructuras `if` / `if-else` / `if-elif-else` ·
**Resultado de aprendizaje**: RA-5 · **Nivel**: intermedio (cuarto de la secuencia)

## 🧩 Problema

Un cine aplica esta regla para el precio de la entrada según la edad:

- Menores de 3 años: entran gratis (precio 0).
- De 3 a 17 años: entrada infantil ($3.000).
- De 18 a 64 años: entrada general ($5.000).
- 65 años o más: entrada tercera edad ($3.500).

El programa recibe la edad y muestra la categoría y el precio.

## 🔍 Análisis

- **Entrada**: `edad` (`int`).
- **Proceso**: elegir **un** camino según en qué rango cae la edad.
- **Salida**: categoría (texto) y precio (`int`).

## 💡 Solución

Empezamos por la decisión más simple (¿es gratis?) y añadimos los demás casos con
`elif`. El orden importa: Python evalúa de arriba hacia abajo y se queda con el **primer**
rango que se cumple, así que basta comprobar el límite superior de cada tramo.

## 💻 Código

```python
# Entrada
edad = 30

# Proceso y salida: un solo camino se ejecuta
if edad < 3:
    categoria = "Liberado"
    precio = 0
elif edad < 18:
    categoria = "Infantil"
    precio = 3000
elif edad < 65:
    categoria = "General"
    precio = 5000
else:
    categoria = "Tercera edad"
    precio = 3500

print("Categoría:", categoria)
print("Precio:", precio)
```

## 🧭 Explicación paso a paso

1. `edad = 30`.
2. `edad < 3` → `30 < 3` → `False`: se salta ese bloque.
3. `edad < 18` → `False`: se salta.
4. `edad < 65` → `30 < 65` → `True`: se ejecuta este bloque (`categoria = "General"`,
   `precio = 5000`) y se **ignoran** el resto de `elif` y el `else`.
5. Los `print` muestran la categoría y el precio elegidos.

## ✅ Resultado esperado

```text
Categoría: General
Precio: 5000
```

> Prueba mental: con `edad = 2` la salida sería `Liberado` / `0`; con `edad = 70`,
> `Tercera edad` / `3500`.
