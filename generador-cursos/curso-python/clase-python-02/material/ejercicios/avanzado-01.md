# Avanzado 01 — Refactorizar con funciones

## Problema

El siguiente programa imprime la boleta de tres clientes. Funciona, pero el cálculo del
total con IVA (`neto + neto * 19 // 100`) está repetido tres veces y la estructura
"Cliente / Total" también.

**Refactoriza** el programa usando funciones, **sin cambiar su salida**.

## Código de partida

```python
print("Cliente: Ana")
neto_ana = 1000 + 2000 + 500
total_ana = neto_ana + neto_ana * 19 // 100
print("Total:", total_ana)

print("Cliente: Luis")
neto_luis = 3000 + 1500
total_luis = neto_luis + neto_luis * 19 // 100
print("Total:", total_luis)

print("Cliente: Eva")
neto_eva = 800 + 800 + 800 + 800
total_eva = neto_eva + neto_eva * 19 // 100
print("Total:", total_eva)
```

## Entrada

- Los montos netos de cada cliente, ya presentes en el código de partida.

## Proceso esperado

1. Detectar el fragmento repetido: el cálculo del total con IVA.
2. Crear `total_con_iva(neto)` que **devuelva** `neto + neto * 19 // 100`.
3. Detectar la estructura repetida "imprimir Cliente / imprimir Total".
4. Crear `mostrar_boleta(nombre, neto)` que imprima ambas líneas usando
   `total_con_iva`.
5. Reemplazar el código de partida por tres llamadas a `mostrar_boleta`.
6. Ejecutar y comprobar que la salida es **idéntica** a la del código de partida.

## Salida

```text
Cliente: Ana
Total: 4165
Cliente: Luis
Total: 5355
Cliente: Eva
Total: 3808
```

## Restricciones

- La salida debe ser exactamente la misma que la del código de partida.
- No debe quedar ningún cálculo de IVA repetido: debe estar en una sola función.
- `total_con_iva` usa `return`; `mostrar_boleta` usa `print`.
- Identificadores y comentarios en español.

## Dificultad

Avanzado

## Resultados de aprendizaje

- RA-5: escribir funciones reutilizables y modulares.
- RA-6: refactorizar código repetido extrayéndolo a funciones.
- RA-7: combinar una función con otra (`mostrar_boleta` usa `total_con_iva`).
