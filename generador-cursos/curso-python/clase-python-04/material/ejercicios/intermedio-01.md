# 🟡 Intermedio 01 — Depurar una lista de tareas pendientes

## 🧩 Problema

Un diccionario `tareas_pendientes` asocia el nombre de una tarea con su prioridad
(`"alta"`, `"media"` o `"baja"`):

```python
tareas_pendientes = {
    "lavar el auto": "baja",
    "pagar cuentas": "alta",
    "estudiar Python": "media",
    "llamar al dentista": "media",
}
```

Escribe un programa que:

1. Elimine `"pagar cuentas"` con `pop`, guardando y mostrando su prioridad (ya se
   pagaron).
2. Intente eliminar `"hacer ejercicio"` (que no existe) con `pop` y un valor por
   defecto `"no encontrada"`, sin que el programa falle.
3. Elimine con `del` la tarea `"lavar el auto"`.
4. Muestre el diccionario final de tareas pendientes.

## 📥 Entrada

El diccionario `tareas_pendientes` dado arriba, fijo en el código.

## ⚙️ Proceso esperado

Usar `pop` para la primera eliminación (guardando el valor devuelto), `pop` con valor
por defecto para el intento seguro, y `del` para la tercera eliminación.

## 📤 Salida

La prioridad que tenía `"pagar cuentas"`, el resultado de intentar eliminar
`"hacer ejercicio"`, y el diccionario final de tareas pendientes.

## 🚧 Restricciones

- Cada eliminación debe usar el método indicado en el enunciado (no todas con el
  mismo).
- El programa no debe detenerse con `KeyError` en ningún punto.
- Los identificadores y comentarios deben estar en español.

## 📊 Dificultad

Intermedio

## 🎓 Resultados de aprendizaje

- RA-5: eliminar elementos de un diccionario con `del`, `pop` y su variante con valor
  por defecto.
