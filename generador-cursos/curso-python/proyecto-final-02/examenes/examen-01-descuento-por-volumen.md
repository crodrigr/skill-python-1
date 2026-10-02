# 📘 Examen 01 — Extensión del Proyecto Final 02: Descuento por volumen

**Examen individual** · Duración: 1 hora · Se resuelve sobre el proyecto ya entregado
(`enunciado-proyecto-final-02.md`, Gestor de Inventario y Ventas)

## 🎯 Contexto

Ya entregaste el Gestor de Inventario y Ventas. La dueña de la tienda quiere ahora
premiar a los clientes que compran en cantidad: pide que las ventas grandes tengan un
descuento automático.

## 🧩 Qué tenés que agregar

Al registrar una venta, si la cantidad total de unidades vendidas en esa venta (la
suma de las cantidades de todos sus ítems confirmados) es **mayor o igual a 10
unidades**, se debe aplicar un **descuento del 10%** sobre el total de la venta antes
de guardarla.

Requisitos puntuales:

- Calculá primero el total "bruto" de la venta (la suma de los subtotales de los
  ítems), como ya hacía el programa.
- Si la venta llega a las 10 unidades o más, calculá el total final aplicando el 10%
  de descuento sobre ese total bruto.
- Al confirmar la venta, mostrale al usuario **ambos valores**: el total sin descuento
  y el total final (indicando si se aplicó o no el descuento).
- El número que quede guardado como total de la venta (en el archivo de persistencia)
  debe ser el **total final** (con descuento aplicado, si corresponde).
- Si la venta no llega a las 10 unidades, el total final es igual al total bruto: no
  hay descuento.
- Se mantiene la regla de que una venta sin ningún ítem confirmado no se registra.
- El programa no debe romperse con una venta que llega justo al umbral (10 unidades
  exactas) ni con ninguna cantidad de ítems.

## 🚫 Restricciones

Se mantienen todas las del proyecto original:

- Sin clases propias (POO), sin el módulo `collections`, sin `datetime`.
- Identificadores y comentarios en español.
- Si agregás alguna conversión numérica nueva, usá `try`/`except` con la excepción
  específica (por ejemplo `ValueError`), no un `except` genérico.

## ✍️ Cómo marcar tu código

En tu proyecto ya entregado, justo **antes** de cada bloque de código nuevo o
modificado que resuelva este examen, agregá como comentario, en su propia línea:

```python
# codigo-examen-no1
```

Esto es lo que permite identificar, dentro del proyecto completo, qué código
corresponde a este examen.

## ⏱️ Antes de entregar

Probá al menos dos casos:

1. Una venta que **no** llegue a las 10 unidades (no debe aplicarse descuento).
2. Una venta que las supere (debe aplicarse el 10% de descuento).

Confirmá en ambos casos que el total mostrado y el total guardado en el archivo son
los correctos.

## 📏 Qué se evalúa

| Criterio | Qué se revisa | Peso |
|---|---|---|
| ✅ Lógica del descuento | Se aplica solo cuando la venta llega al umbral de unidades | 40% |
| 💾 Total persistido | El total guardado en el archivo refleja el descuento cuando corresponde | 25% |
| 🚧 Robustez | El programa no se rompe con ningún caso de prueba, incluido el umbral exacto | 20% |
| 🏷️ Marca de código | `# codigo-examen-no1` presente en cada bloque agregado o modificado | 15% |
