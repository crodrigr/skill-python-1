# 📘 Examen 03 — Extensión del Proyecto Final 02: Alerta de reposición urgente

**Examen individual** · Duración: 1 hora · Se resuelve sobre el proyecto ya entregado
(`enunciado-proyecto-final-02.md`, Gestor de Inventario y Ventas)

## 🎯 Contexto

Ya entregaste el Gestor de Inventario y Ventas. El reporte actual de "alerta de stock
bajo" solo lista qué productos están por debajo de su mínimo, pero no dice cuánto
comprar ni cuáles son más urgentes. La dueña de la tienda pide esa información para
decidir qué reponer primero.

## 🧩 Qué tenés que agregar

Un nuevo reporte, accesible desde el submenú de reportes, llamado **"Alerta de
reposición urgente"**.

Requisitos puntuales:

- Tomar todos los productos cuyo stock actual esté por debajo de su stock mínimo
  (igual que el reporte de stock bajo que ya tenías).
- Para cada uno, calcular cuántas unidades hay que comprar para llegar al **doble**
  de su stock mínimo. Por ejemplo: si el stock mínimo es 10 y el stock actual es 3,
  hay que comprar 17 unidades para llegar a 20.
- Mostrar la lista ordenada de **mayor a menor urgencia**, entendiendo "urgencia"
  como la diferencia entre el stock mínimo y el stock actual (a mayor diferencia, más
  urgente).
- Para cada producto de la lista, mostrar: código, nombre, stock actual, stock mínimo
  y unidades a comprar.
- Si **ningún producto** está por debajo de su mínimo, el reporte debe avisarlo con
  un mensaje claro (por ejemplo "No hay productos con alerta de reposición"), sin
  fallar.
- Para ordenar de mayor a menor urgencia sin usar `collections`, podés usar `sorted`
  con el parámetro `key` (por ejemplo ordenando por `stock_minimo - stock_actual`,
  descendente), o armar el orden a mano con las estructuras ya conocidas.

## 🚫 Restricciones

Se mantienen todas las del proyecto original:

- Sin el módulo `collections`, sin `datetime`.
- Identificadores y comentarios en español.
- Si agregás alguna conversión numérica nueva, usá `try`/`except` con la excepción
  específica, no un `except` genérico.

## ✍️ Cómo marcar tu código

En tu proyecto ya entregado, justo **antes** de cada bloque de código nuevo o
modificado que resuelva este examen, agregá como comentario, en su propia línea:

```python
# codigo-examen-no3
```

Esto es lo que permite identificar, dentro del proyecto completo, qué código
corresponde a este examen.

## ⏱️ Antes de entregar

Probá al menos tres casos:

1. Ningún producto por debajo de su mínimo (debe avisar, no fallar).
2. Un solo producto por debajo de su mínimo (debe mostrar la cantidad a comprar
   correcta).
3. Varios productos por debajo de su mínimo, con distintas diferencias (debe quedar
   ordenada de mayor a menor urgencia).

## 📏 Qué se evalúa

| Criterio | Qué se revisa | Peso |
|---|---|---|
| ✅ Cálculo de reposición | Las unidades a comprar están bien calculadas (llegar al doble del mínimo) | 35% |
| 🔢 Orden por urgencia | La lista queda ordenada de mayor a menor diferencia | 25% |
| 🚧 Caso sin alertas | Avisa correctamente cuando no hay productos bajo el mínimo, sin romperse | 25% |
| 🏷️ Marca de código | `# codigo-examen-no3` presente en cada bloque agregado o modificado | 15% |
