# Ejemplo 03 — De algoritmo a programa

**Tema**: análisis de un problema, algoritmo, pseudocódigo y programa · **Resultados de
aprendizaje**: RA-3, RA-9 · **Nivel**: introductorio (tercero de la secuencia)

## Problema

Una panadería vende pan por kilo. El cliente indica cuántos kilos quiere y con cuánto
dinero paga. El programa debe mostrar el precio total y el vuelto (cambio) que recibe.
El precio del kilo es de 2.000 pesos.

## Análisis

| Pregunta | Respuesta |
|----------|-----------|
| Entrada | `kilos` (número con decimales), `paga_con` (número) |
| Proceso | `total = kilos * 2000`; `vuelto = paga_con - total` |
| Salida | el total y el vuelto |

## Solución

### Algoritmo (pasos)

1. Preguntar cuántos kilos quiere el cliente.
2. Preguntar con cuánto dinero paga.
3. Calcular el total: kilos por el precio del kilo.
4. Calcular el vuelto: dinero con que paga menos el total.
5. Mostrar el total y el vuelto.

### Pseudocódigo

```text
PRECIO_KILO ← 2000
Leer kilos
Leer paga_con
total ← kilos * PRECIO_KILO
vuelto ← paga_con - total
Mostrar total
Mostrar vuelto
```

## Código

```python
# Cada paso del pseudocódigo se traduce a una instrucción de Python

precio_kilo = 2000

# Entrada
kilos = float(input("¿Cuántos kilos de pan quiere? "))
paga_con = float(input("¿Con cuánto dinero paga? "))

# Proceso
total = kilos * precio_kilo
vuelto = paga_con - total

# Salida
print("Total a pagar:", total)
print("Vuelto:", vuelto)
```

## Explicación paso a paso

1. `precio_kilo = 2000` guarda el dato constante del problema.
2. `input(...)` muestra la pregunta y espera a que el usuario escriba un valor; devuelve
   siempre **texto**, por eso `float(...)` lo convierte en número con decimales.
3. `total = kilos * precio_kilo`: con `kilos = 1.5` sería `1.5 * 2000` → `3000.0`.
4. `vuelto = paga_con - total`: con `paga_con = 5000` sería `5000 - 3000.0` → `2000.0`.
5. Los `print` muestran los dos resultados.

## Resultado esperado

Prueba con la entrada `1.5` (kilos) y `5000` (paga con):

```text
¿Cuántos kilos de pan quiere? 1.5
¿Con cuánto dinero paga? 5000
Total a pagar: 3000.0
Vuelto: 2000.0
```

> Verificación manual: 1.5 kg × 2.000 = 3.000; 5.000 − 3.000 = 2.000. Coincide.
