# Ejemplo 02 — Agregar, eliminar y modificar elementos

**Tema**: manipulación de listas (`append`, `insert`, `remove`, `pop`, `del`, asignación
por índice) · **Resultado de aprendizaje**: RA-3 · **Nivel**: introductorio

## Problema

Una lista de tareas pendientes empieza con tres tareas. Durante el día: se agrega una
tarea nueva al final, se inserta una tarea urgente al principio, se completa (y se
elimina) una tarea existente por su nombre, y se corrige el texto de otra tarea que
estaba mal escrita.

## Análisis

- **Entrada**: la lista inicial de tareas (`str`).
- **Proceso**: agregar al final, insertar al principio, eliminar por valor y modificar
  por índice, mostrando el estado de la lista después de cada cambio.
- **Salida**: el estado final de la lista de tareas.

## Solución

1. Crear la lista inicial.
2. Agregar con `append`, insertar con `insert`.
3. Eliminar con `remove` la tarea ya completada.
4. Corregir el texto con asignación por índice.
5. Mostrar el estado tras cada paso.

## Código

```python
# Lista inicial de tareas pendientes
tareas = ["comprar pan", "pagar cuentas", "lavar el auto"]
print("Inicio:", tareas)

# Agregar una tarea nueva al final
tareas.append("estudiar Python")
print("Tras append:", tareas)

# Insertar una tarea urgente al principio (posición 0)
tareas.insert(0, "llamar al médico")
print("Tras insert:", tareas)

# La tarea "pagar cuentas" ya se completó: se elimina por valor
tareas.remove("pagar cuentas")
print("Tras remove:", tareas)

# "lavar el auto" estaba mal escrito; se corrige por índice
indice_a_corregir = tareas.index("lavar el auto")
tareas[indice_a_corregir] = "lavar el auto y la moto"
print("Tras modificar:", tareas)
```

## Explicación paso a paso

1. La lista empieza con tres tareas en el orden dado.
2. `tareas.append("estudiar Python")` agrega el nuevo elemento **al final**; modifica la
   lista original y no devuelve nada útil (`None`).
3. `tareas.insert(0, "llamar al médico")` inserta en la **posición 0**, desplazando el
   resto de los elementos una posición a la derecha.
4. `tareas.remove("pagar cuentas")` busca la **primera** aparición de ese valor exacto y
   la quita; si el valor no existiera, lanzaría `ValueError`.
5. `tareas.index("lavar el auto")` devuelve la posición actual de ese texto (cambia si
   la lista se reordenó); `tareas[indice_a_corregir] = "..."` reemplaza el contenido en
   esa posición sin cambiar el tamaño de la lista.

## Resultado esperado

```text
Inicio: ['comprar pan', 'pagar cuentas', 'lavar el auto']
Tras append: ['comprar pan', 'pagar cuentas', 'lavar el auto', 'estudiar Python']
Tras insert: ['llamar al médico', 'comprar pan', 'pagar cuentas', 'lavar el auto', 'estudiar Python']
Tras remove: ['llamar al médico', 'comprar pan', 'lavar el auto', 'estudiar Python']
Tras modificar: ['llamar al médico', 'comprar pan', 'lavar el auto y la moto', 'estudiar Python']
```
