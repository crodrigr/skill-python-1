# Ejemplo 04 — Ordenar con sort, sorted y key

**Tema**: `lista.sort()` vs `sorted(lista)`, `reverse`, `key` · **Resultado de
aprendizaje**: RA-5 · **Nivel**: intermedio

## Problema

Un docente tiene los puntajes de un examen en una lista y quiere: obtener una versión
ordenada de menor a mayor sin alterar el orden original (para conservar el orden de
llegada de las entregas), obtener una versión ordenada de mayor a menor, y ordenar una
lista de registros `(nombre, puntaje)` por puntaje.

## Análisis

- **Entrada**: lista de puntajes (`int`) y lista de registros `(nombre, puntaje)`.
- **Proceso**: usar `sorted` (sin modificar el original) con `reverse` para orden
  descendente, y con `key` para ordenar tuplas por un campo.
- **Salida**: la lista original intacta, su versión ascendente, su versión descendente y
  los registros ordenados por puntaje.

## Solución

1. Usar `sorted(lista)` para obtener una copia ordenada ascendente sin tocar la
   original.
2. Usar `sorted(lista, reverse=True)` para la versión descendente.
3. Definir una función que devuelva el puntaje de un registro y pasarla como `key` a
   `sorted`.

## Código

```python
# Puntajes de un examen, en el orden de entrega
puntajes = [78, 95, 60, 88, 72]

# sorted() NO modifica la lista original
puntajes_asc = sorted(puntajes)
puntajes_desc = sorted(puntajes, reverse=True)

print("Orden de entrega (original):", puntajes)
print("De menor a mayor:", puntajes_asc)
print("De mayor a menor:", puntajes_desc)


def obtener_puntaje(registro):
    """Devuelve el puntaje (segundo valor) de un registro (nombre, puntaje)."""
    return registro[1]


registros = [("Ana", 78), ("Luis", 95), ("Eva", 60)]
registros_por_puntaje = sorted(registros, key=obtener_puntaje)
print("Registros por puntaje (ascendente):", registros_por_puntaje)
print("Registros por puntaje (descendente):", sorted(registros, key=obtener_puntaje, reverse=True))
```

## Explicación paso a paso

1. `sorted(puntajes)` construye y devuelve una lista **nueva** ordenada de menor a
   mayor; `puntajes` conserva su orden de entrega original.
2. `sorted(puntajes, reverse=True)` hace lo mismo pero de mayor a menor; sigue sin tocar
   `puntajes`.
3. `obtener_puntaje(registro)` es una función que, dado un registro `(nombre, puntaje)`,
   devuelve solo el puntaje (`registro[1]`).
4. `sorted(registros, key=obtener_puntaje)` llama a `obtener_puntaje` una vez por cada
   registro para decidir el orden, comparando los puntajes en lugar de comparar las
   tuplas completas (lo que fallaría si dos nombres empezaran distinto pero se quisiera
   ordenar por número).
5. Agregar `reverse=True` junto con `key` combina ambos: ordena por puntaje, de mayor a
   menor.

## Resultado esperado

```text
Orden de entrega (original): [78, 95, 60, 88, 72]
De menor a mayor: [60, 72, 78, 88, 95]
De mayor a menor: [95, 88, 78, 72, 60]
Registros por puntaje (ascendente): [('Eva', 60), ('Ana', 78), ('Luis', 95)]
Registros por puntaje (descendente): [('Luis', 95), ('Ana', 78), ('Eva', 60)]
```
