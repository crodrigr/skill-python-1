# Ejemplo 08 — Conjuntos y sus operaciones

**Tema**: construir un conjunto de valores únicos y aplicar unión, intersección y
diferencia · **Resultado de aprendizaje**: RA-9 · **Nivel**: intermedio

## Problema

Una biblioteca registra, por cada préstamo del mes, el nombre de la persona que lo
pidió; una misma persona puede aparecer varias veces si pidió más de un libro. Se
necesita saber cuántas personas **distintas** pidieron un préstamo, y comparar dos
listas (los lectores de enero y los de febrero) para saber quiénes leyeron en ambos
meses, quiénes leyeron en cualquiera de los dos, y quiénes leyeron solo en enero.

## Análisis

- **Entrada**: lista de préstamos de enero y lista de préstamos de febrero (nombres,
  con posibles repetidos).
- **Proceso**: construir un conjunto de lectores únicos por mes; aplicar unión,
  intersección y diferencia entre ambos conjuntos.
- **Salida**: la cantidad de lectores únicos de enero, y los tres resultados de
  comparar los dos meses.

## Solución

1. Construir un conjunto a partir de cada lista de préstamos con `set(...)`.
2. Usar `len(...)` sobre el conjunto para contar lectores distintos.
3. Aplicar `|`, `&` y `-` entre los dos conjuntos, mostrando cada resultado con
   `sorted(...)` para que el orden de la salida sea siempre el mismo (los conjuntos en
   sí no tienen orden).

## Código

```python
prestamos_enero = ["Ana", "Luis", "Ana", "Eva", "Luis", "Ana"]
prestamos_febrero = ["Luis", "Marco", "Eva", "Marco"]

lectores_enero = set(prestamos_enero)
lectores_febrero = set(prestamos_febrero)

print("Préstamos registrados en enero:", len(prestamos_enero))
print("Lectores distintos en enero:", len(lectores_enero))

print("Leyeron en ambos meses:", sorted(lectores_enero & lectores_febrero))
print("Leyeron en cualquiera de los dos meses:", sorted(lectores_enero | lectores_febrero))
print("Leyeron solo en enero:", sorted(lectores_enero - lectores_febrero))
```

## Explicación paso a paso

1. `prestamos_enero` tiene 6 préstamos, pero "Ana" y "Luis" se repiten.
2. `set(prestamos_enero)` construye un conjunto que conserva cada nombre **una sola
   vez**, sin importar cuántas veces aparecía en la lista.
3. `len(lectores_enero)` cuenta cuántos nombres distintos hay: 3 (Ana, Luis, Eva), en
   vez de los 6 préstamos totales.
4. `lectores_enero & lectores_febrero` (intersección) da los nombres que están en
   **ambos** conjuntos: quienes leyeron los dos meses.
5. `lectores_enero | lectores_febrero` (unión) da todos los nombres que aparecen en
   **cualquiera** de los dos conjuntos, sin repetir.
6. `lectores_enero - lectores_febrero` (diferencia) da los nombres que están en enero
   pero **no** en febrero.
7. Los conjuntos no tienen orden interno; por eso cada resultado se envuelve con
   `sorted(...)` antes de imprimirlo, para obtener siempre una lista ordenada y
   predecible en la pantalla.

## Resultado esperado

```text
Préstamos registrados en enero: 6
Lectores distintos en enero: 3
Leyeron en ambos meses: ['Eva', 'Luis']
Leyeron en cualquiera de los dos meses: ['Ana', 'Eva', 'Luis', 'Marco']
Leyeron solo en enero: ['Ana']
```
