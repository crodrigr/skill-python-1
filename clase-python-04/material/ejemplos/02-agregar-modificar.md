# 💡 Ejemplo 02 — Agregar y modificar elementos

**Tema**: agregar una clave nueva y modificar el valor de una existente por asignación
· **Resultado de aprendizaje**: RA-4 · **Nivel**: introductorio

## 🧩 Problema

Un pequeño almacén registra el stock de tres productos. Durante el día: llega un
producto nuevo que hay que agregar, y se corrige el stock de un producto porque el
conteo inicial estaba mal.

## 🔍 Análisis

- **Entrada**: el diccionario inicial de stock (`str` → `int`).
- **Proceso**: agregar una clave nueva; modificar el valor de una clave existente,
  mostrando el estado del diccionario después de cada cambio.
- **Salida**: el estado del diccionario tras cada cambio.

## 💡 Solución

1. Crear el diccionario inicial de stock.
2. Agregar el producto nuevo con `diccionario[clave] = valor`.
3. Corregir el stock existente con la misma operación.

## 💻 Código

```python
# Stock inicial por producto
stock = {"arroz": 40, "aceite": 25, "azúcar": 15}
print("Inicio:", stock)

# Llega un producto nuevo: se agrega
stock["fideos"] = 30
print("Tras agregar fideos:", stock)

# El conteo de aceite estaba mal: se corrige
stock["aceite"] = 20
print("Tras corregir aceite:", stock)
```

## 🧭 Explicación paso a paso

1. `stock = {"arroz": 40, "aceite": 25, "azúcar": 15}` crea el diccionario inicial con
   tres productos.
2. `stock["fideos"] = 30` agrega una clave nueva porque `"fideos"` no existía todavía;
   el diccionario pasa a tener cuatro productos.
3. `stock["aceite"] = 20` **no** agrega una clave nueva: `"aceite"` ya existía, así que
   esta asignación reemplaza su valor anterior (`25`) por el nuevo (`20`); el
   diccionario sigue teniendo cuatro productos.

## ✅ Resultado esperado

```text
Inicio: {'arroz': 40, 'aceite': 25, 'azúcar': 15}
Tras agregar fideos: {'arroz': 40, 'aceite': 25, 'azúcar': 15, 'fideos': 30}
Tras corregir aceite: {'arroz': 40, 'aceite': 20, 'azúcar': 15, 'fideos': 30}
```
