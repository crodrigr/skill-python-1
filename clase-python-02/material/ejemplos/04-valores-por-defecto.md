# 💡 Ejemplo 04 — Valores por defecto

**Tema**: varios parámetros, uno con valor por defecto; llamadas con argumentos por
nombre · **Resultados de aprendizaje**: RA-3 · **Nivel**: intermedio

## 🧩 Problema

Una tienda calcula el precio final de un producto sumándole el IVA. Casi siempre el IVA
es del 19 %, pero algunos productos tienen IVA reducido o están exentos. Queremos una
función cómoda para el caso habitual y flexible para las excepciones.

## 🔍 Análisis

- **Entrada**: el precio sin impuesto y, opcionalmente, la tasa de IVA.
- **Proceso**: sumar al precio el porcentaje de IVA correspondiente.
- **Salida**: el precio final.

## 💡 Solución

1. Definir `precio_con_impuesto(precio, iva=0.19)`: el segundo parámetro tiene un
   **valor por defecto**.
2. Llamarla sin el segundo argumento para el caso normal.
3. Llamarla con el segundo argumento (posicional o por nombre) para las excepciones.

## 💻 Código

```python
def precio_con_impuesto(precio, iva=0.19):
    """Devuelve el precio final aplicando el IVA (19 % por defecto)."""
    return precio + precio * iva

print(precio_con_impuesto(1000))
print(precio_con_impuesto(1000, 0.10))
print(precio_con_impuesto(precio=1000, iva=0.0))
```

## 🧭 Explicación paso a paso

1. `iva=0.19` en la definición significa: "si en la llamada no se pasa `iva`, vale
   `0.19`".
2. `precio_con_impuesto(1000)`: solo se pasa `precio`. `iva` toma su valor por defecto
   `0.19`. Resultado: `1000 + 1000 * 0.19` = `1190.0`.
3. `precio_con_impuesto(1000, 0.10)`: el segundo argumento posicional reemplaza el valor
   por defecto. Resultado: `1000 + 1000 * 0.10` = `1100.0`.
4. `precio_con_impuesto(precio=1000, iva=0.0)`: **argumentos por nombre**. Se ve con
   claridad qué es cada valor y el orden ya no importa. Resultado: `1000 + 0.0` =
   `1000.0`.

> Los parámetros con valor por defecto van siempre **después** de los que no lo tienen.

## ✅ Resultado esperado

```text
1190.0
1100.0
1000.0
```
