# 🟡 Intermedio 02 — Reporte de calificaciones

## 🧩 Problema

Un diccionario `calificaciones` asocia el nombre de cada estudiante con su nota:

```python
calificaciones = {"Ana": 6.5, "Luis": 3.8, "Eva": 5.0}
calificaciones_nuevas = {"Eva": 7.0, "Marco": 4.5}
```

Escribe un programa que:

1. Aplique `calificaciones_nuevas` sobre `calificaciones` con `update` (corrige la nota
   de Eva y agrega a Marco).
2. Recorra el diccionario resultante con `items()` y muestre, para cada estudiante, si
   está `"Aprobado"` (nota `>= 4.0`) o `"Reprobado"`, con el formato
   `Ana: 6.5 - Aprobado`.
3. Cuente, con un acumulador durante el mismo recorrido, cuántos estudiantes aprobaron.

## 📥 Entrada

Los diccionarios `calificaciones` y `calificaciones_nuevas` dados arriba, fijos en el
código.

## ⚙️ Proceso esperado

Usar `update` para fusionar los diccionarios; recorrer el resultado con
`for nombre, nota in calificaciones.items()`, decidiendo con un `if` el estado de cada
estudiante y acumulando el conteo de aprobados en la misma vuelta del bucle.

## 📤 Salida

El reporte línea por línea (nombre, nota y estado) y, al final, el total de estudiantes
aprobados.

## 🚧 Restricciones

- La fusión debe hacerse con `update`, no reconstruyendo el diccionario a mano.
- El recorrido para el reporte debe usar `items()`.
- Los identificadores y comentarios deben estar en español.

## 📊 Dificultad

Intermedio

## 🎓 Resultados de aprendizaje

- RA-4: actualizar varias claves de un diccionario a la vez con `update`.
- RA-6: recorrer un diccionario con `items()`, desempaquetando clave y valor.
