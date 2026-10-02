# 📘 Examen 02 — Extensión del Proyecto Final 02: Ranking de productos más vendidos

**Examen individual** · Duración: 1 hora · Se resuelve sobre el proyecto ya entregado
(`enunciado-proyecto-final-02.md`, Gestor de Inventario y Ventas)

## 🎯 Contexto

Ya entregaste el Gestor de Inventario y Ventas. El reporte actual solo muestra **el**
producto más vendido. La dueña de la tienda quiere ver un panorama más completo: un
ranking con los productos que más se venden.

## 🧩 Qué tenés que agregar

Un nuevo reporte, accesible desde el submenú de reportes, llamado **"Top 3 productos
más vendidos"**.

Requisitos puntuales:

- Mostrar los **3 productos** con mayor cantidad total vendida (en unidades),
  ordenados de mayor a menor.
- Para cada producto del ranking, mostrar: la posición (1, 2 o 3), el código, el
  nombre, la cantidad total vendida y el **porcentaje** que esa cantidad representa
  sobre el total general de unidades vendidas (la suma de las cantidades de todos los
  ítems de todas las ventas), con dos decimales.
- Si hay **menos de 3 productos** con ventas registradas, mostrar solo los que haya,
  sin inventar productos ni romper el programa.
- Si **todavía no hay ventas registradas**, el reporte debe avisarlo con un mensaje
  claro (por ejemplo "Todavía no hay ventas registradas") sin fallar.
- Podés reutilizar el diccionario de cantidades acumuladas por producto que ya usabas
  para el reporte "producto más vendido" (clave: código, valor: cantidad acumulada).
- Para ordenar de mayor a menor sin usar `collections`, podés usar `sorted` con el
  parámetro `key` sobre los pares del diccionario (por ejemplo
  `sorted(diccionario.items(), key=lambda item: item[1], reverse=True)`), o armar el
  orden a mano con las estructuras ya conocidas.

## 🚫 Restricciones

Se mantienen todas las del proyecto original:

- Sin clases propias (POO), sin el módulo `collections`, sin `datetime`.
- Identificadores y comentarios en español.
- Si agregás alguna conversión numérica nueva, usá `try`/`except` con la excepción
  específica, no un `except` genérico.

## ✍️ Cómo marcar tu código

En tu proyecto ya entregado, justo **antes** de cada bloque de código nuevo o
modificado que resuelva este examen, agregá como comentario, en su propia línea:

```python
# codigo-examen-no2
```

Esto es lo que permite identificar, dentro del proyecto completo, qué código
corresponde a este examen.

## ⏱️ Antes de entregar

Probá al menos tres casos:

1. Sin ninguna venta registrada (debe avisar, no fallar).
2. Con ventas pero menos de 3 productos distintos vendidos (debe mostrar solo los que
   haya).
3. Con 3 o más productos distintos vendidos (debe mostrar el top 3 completo, con los
   porcentajes sumando un valor coherente).

## 📏 Qué se evalúa

| Criterio | Qué se revisa | Peso |
|---|---|---|
| ✅ Ranking correcto | El orden de mayor a menor y las cantidades son correctas | 35% |
| 🔢 Porcentajes | El porcentaje de cada producto está bien calculado (dos decimales) | 25% |
| 🚧 Casos límite | Maneja sin romperse los casos de 0, 1-2 y 3+ productos vendidos | 25% |
| 🏷️ Marca de código | `# codigo-examen-no2` presente en cada bloque agregado o modificado | 15% |
