# 💡 Ejemplo 04 — Iterar con `iter()` y `next()`

## 🧩 Problema

Usando la misma cola de pedidos del ejemplo anterior, se quiere recorrerla "a mano",
un elemento a la vez, para entender qué hace Python por dentro cuando usamos `for`.

## 🔍 Análisis

- **Entrada**: la `deque` `["pizza", "sushi", "tacos", "pizza"]` del ejemplo 03.
- **Proceso**: obtener un iterador con `iter()`, avanzar con `next()` hasta agotarlo
  (capturando `StopIteration`), y comparar con recorrer la misma `deque` con `for`.
- **Salida**: cada pedido mostrado uno por uno, el aviso de que ya no quedan más, y el
  mismo recorrido usando `for`.

## 💡 Solución

`iter(cola_pedidos)` crea el iterador; cada `next(iterador)` devuelve el siguiente
pedido. Al agotarse la cola, `next()` lanza `StopIteration`, que se captura con
`try`/`except` para mostrar un mensaje en vez de detener el programa.

## 💻 Código

```python
import collections

cola_pedidos = collections.deque(["pizza", "sushi", "tacos", "pizza"])

iterador = iter(cola_pedidos)
print("Primer pedido:", next(iterador))
print("Segundo pedido:", next(iterador))
print("Tercer pedido:", next(iterador))
print("Cuarto pedido:", next(iterador))

try:
    print("Quinto pedido:", next(iterador))
except StopIteration:
    print("Ya no quedan mas pedidos en la cola (StopIteration)")

print("\nRecorriendo con for (Python maneja StopIteration por nosotros):")
for pedido in cola_pedidos:
    print("-", pedido)
```

## 🧭 Explicación paso a paso

1. `iter(cola_pedidos)` no recorre nada todavía: solo crea el iterador, un objeto que
   recuerda en qué posición va (al principio, antes del primer elemento).
2. Cada `next(iterador)` avanza una posición y devuelve el elemento en esa posición.
3. Después del cuarto pedido, la `deque` está agotada: llamar a `next()` una vez más
   lanza `StopIteration`, que capturamos con `try`/`except` para responder con un
   mensaje en vez de dejar que el programa se detenga con un error sin manejar.
4. El `for` de la segunda parte recorre la **misma** `deque` desde el principio: por
   dentro, Python llama a `iter(cola_pedidos)` una vez y a `next()` en cada vuelta,
   deteniéndose automáticamente al recibir `StopIteration` — es el mismo mecanismo,
   solo que Python maneja la excepción por nosotros.

## ✅ Resultado esperado

```text
Primer pedido: pizza
Segundo pedido: sushi
Tercer pedido: tacos
Cuarto pedido: pizza
Ya no quedan mas pedidos en la cola (StopIteration)

Recorriendo con for (Python maneja StopIteration por nosotros):
- pizza
- sushi
- tacos
- pizza
```
