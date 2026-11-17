# 💡 Ejemplo 03 — Eliminar con del, pop y popitem

**Tema**: `del`, `pop` (con y sin valor por defecto) y `popitem` · **Resultado de
aprendizaje**: RA-5 · **Nivel**: intermedio

## 🧩 Problema

El almacén del ejemplo anterior deja de vender un producto (`"azúcar"`), y necesita
saber cuánto stock le quedaba justo antes de retirarlo. Además, quiere probar qué pasa
si intenta quitar un producto que ya no existe, y quitar el último producto agregado
sin especificar cuál.

## 🔍 Análisis

- **Entrada**: el diccionario de stock con cuatro productos.
- **Proceso**: eliminar `"azúcar"` con `pop` guardando su valor; intentar eliminar un
  producto inexistente con `pop` y un valor por defecto (sin error); eliminar el último
  par agregado con `popitem`.
- **Salida**: el stock eliminado de `"azúcar"`, el resultado de la eliminación segura, y
  el par eliminado con `popitem`.

## 💡 Solución

1. Usar `pop("azúcar")` y guardar el valor devuelto.
2. Usar `pop("gaseosa", 0)` para eliminar de forma segura un producto que no existe.
3. Usar `popitem()` para quitar el último par agregado.

## 💻 Código

```python
stock = {"arroz": 40, "aceite": 20, "azúcar": 15, "fideos": 30}

# pop: elimina y devuelve el valor eliminado
stock_azucar = stock.pop("azúcar")
print("Azúcar tenía en stock:", stock_azucar)
print("Stock tras eliminar azúcar:", stock)

# pop con valor por defecto: no falla aunque la clave no exista
stock_gaseosa = stock.pop("gaseosa", 0)
print("Stock de gaseosa (no existía):", stock_gaseosa)

# popitem: elimina el último par agregado
ultimo_producto = stock.popitem()
print("Último producto eliminado:", ultimo_producto)
print("Stock final:", stock)
```

## 🧭 Explicación paso a paso

1. `stock.pop("azúcar")` elimina la clave `"azúcar"` y **devuelve** su valor (`15`), que
   se guarda en `stock_azucar` para poder mostrarlo.
2. `stock.pop("gaseosa", 0)` intenta eliminar `"gaseosa"`, que no existe; como se dio un
   valor por defecto (`0`), no se produce `KeyError`: simplemente devuelve `0`.
3. `stock.popitem()` elimina el **último** par que quedó en el diccionario
   (`"fideos": 30`, el último agregado que no se había tocado) y lo devuelve como una
   tupla `(clave, valor)`.
4. Al final, `stock` solo conserva `"arroz"` y `"aceite"`.

## ✅ Resultado esperado

```text
Azúcar tenía en stock: 15
Stock tras eliminar azúcar: {'arroz': 40, 'aceite': 20, 'fideos': 30}
Stock de gaseosa (no existía): 0
Último producto eliminado: ('fideos', 30)
Stock final: {'arroz': 40, 'aceite': 20}
```
