# 💡 Ejemplo 05 — update y setdefault

**Tema**: actualizar varias claves a la vez con `update`, inicializar una clave solo si
falta con `setdefault` · **Resultado de aprendizaje**: RA-4, RA-7 · **Nivel**: intermedio

## 🧩 Problema

Una tienda recibe una lista de precios actualizados para varios productos a la vez (y
uno de ellos es nuevo), y además quiere llevar un contador de visitas por sección de la
tienda, inicializando cada sección en cero la primera vez que se menciona.

## 🔍 Análisis

- **Entrada**: diccionario `precios` inicial y un diccionario de `precios_nuevos`
  (algunos productos ya existen, otro es nuevo); una lista de secciones visitadas
  (con repeticiones).
- **Proceso**: `update` para aplicar todos los cambios de precio de una vez;
  `setdefault` para inicializar en cero el contador de una sección la primera vez que
  aparece.
- **Salida**: los precios tras `update`, y el conteo de visitas por sección.

## 💡 Solución

1. Aplicar `precios.update(precios_nuevos)`.
2. Recorrer la lista de secciones visitadas y, para cada una, usar `setdefault` para
   inicializar su contador en `0` la primera vez, y luego sumarle `1`.

## 💻 Código

```python
precios = {"pan": 1300, "leche": 1000, "huevos": 2600}
precios_nuevos = {"leche": 1050, "huevos": 2700, "queso": 3200}

precios.update(precios_nuevos)
print("Precios actualizados:", precios)

secciones_visitadas = ["panadería", "lácteos", "panadería", "carnicería", "lácteos", "lácteos"]

visitas_por_seccion = {}
for seccion in secciones_visitadas:
    visitas_por_seccion.setdefault(seccion, 0)
    visitas_por_seccion[seccion] += 1

print("Visitas por sección:", visitas_por_seccion)
```

## 🧭 Explicación paso a paso

1. `precios.update(precios_nuevos)` recorre `precios_nuevos` y, para cada clave: si ya
   existía en `precios` (`"leche"`, `"huevos"`), reemplaza su valor; si no existía
   (`"queso"`), la agrega. Todo en una sola llamada.
2. `visitas_por_seccion.setdefault(seccion, 0)`: la primera vez que aparece una sección
   (por ejemplo, `"panadería"`), la clave no existe todavía, así que `setdefault` la
   crea con el valor `0` y la deja lista; las siguientes veces que aparece la misma
   sección, `setdefault` no hace nada porque la clave ya existe (no la reinicia a `0`).
3. `visitas_por_seccion[seccion] += 1` suma uno al contador de esa sección en cada
   vuelta del bucle, tanto si acaba de crearse como si ya existía.

## ✅ Resultado esperado

```text
Precios actualizados: {'pan': 1300, 'leche': 1050, 'huevos': 2700, 'queso': 3200}
Visitas por sección: {'panadería': 2, 'lácteos': 3, 'carnicería': 1}
```
