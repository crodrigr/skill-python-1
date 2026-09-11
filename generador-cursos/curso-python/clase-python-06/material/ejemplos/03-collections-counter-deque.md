# 💡 Ejemplo 03 — `collections`: `Counter` y `deque`

## 🧩 Problema

Una cafetería anota los pedidos del día en una lista, en el orden en que llegaron. Se
quiere guardarlos en una estructura eficiente para agregar pedidos (una `deque`) y
saber cuántas veces se pidió cada producto.

## 🔍 Análisis

- **Entrada**: una lista fija de pedidos: `["pizza", "sushi", "tacos", "pizza"]`.
- **Proceso**: guardar los pedidos en una `collections.deque`, y usar
  `collections.Counter` sobre ella para contar cuántas veces aparece cada producto.
- **Salida**: la cola de pedidos, el conteo por producto, y cuántas veces se pidió
  "pizza" en particular.

## 💡 Solución

Se crea una `collections.deque` a partir de la lista de pedidos, y se le pasa
directamente a `collections.Counter`, que también acepta cualquier iterable (una
`deque` lo es).

## 💻 Código

```python
import collections

cola_pedidos = collections.deque(["pizza", "sushi", "tacos", "pizza"])
print("Cola de pedidos:", cola_pedidos)

conteo_pedidos = collections.Counter(cola_pedidos)
print("Conteo de pedidos:", conteo_pedidos)
print("Cuantas pizzas se pidieron:", conteo_pedidos["pizza"])
```

## 🧭 Explicación paso a paso

1. `collections.deque([...])` crea una `deque` a partir de una lista inicial; se ve y
   se comporta de forma parecida a una lista al recorrerla o mostrarla.
2. `collections.Counter(cola_pedidos)` recorre la `deque` completa y cuenta cuántas
   veces aparece cada elemento, devolviendo un objeto parecido a un diccionario.
3. `conteo_pedidos["pizza"]` accede al conteo de un producto puntual, igual que se
   accedería a una clave de un diccionario.
4. Tanto la `deque` como el `Counter` son iterables: en el próximo ejemplo usamos esta
   misma `deque` para ver cómo funciona la iteración con `iter()`/`next()`.

## ✅ Resultado esperado

```text
Cola de pedidos: deque(['pizza', 'sushi', 'tacos', 'pizza'])
Conteo de pedidos: Counter({'pizza': 2, 'sushi': 1, 'tacos': 1})
Cuantas pizzas se pidieron: 2
```
