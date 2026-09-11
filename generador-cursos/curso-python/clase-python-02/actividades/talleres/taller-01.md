# Taller 01 — Calculadora de cuenta con propina y división por comensales

**Actividad guiada** · Duración estimada: 45–55 min · **Resultados de aprendizaje**:
RA-2, RA-3, RA-4, RA-6, RA-7

## Objetivo

Construir un programa **descomponiéndolo en funciones**: unas piden o calculan datos (con
parámetros y `return`), otra presenta el resultado y un bloque principal las combina.
Durante el taller, además, se detecta un cálculo repetido y se **refactoriza** a una
función reutilizable (RA-6, RA-7).

## Contexto

Un grupo cena en un restaurante. A partir del **monto de la cuenta**, un **porcentaje de
propina** y el **número de comensales**, el programa debe calcular:

- la propina,
- el total (cuenta + propina),
- cuánto paga cada comensal.

Los tres valores se muestran con el signo `$` y **dos decimales**.

## Pasos

### 1. Analizar el problema

| Pregunta | Respuesta |
|----------|-----------|
| Entrada | `monto` (`float`), `porcentaje` (`int`), `comensales` (`int`) |
| Proceso | calcular propina; calcular total; dividir el total entre los comensales; dar formato a cada valor |
| Salida | tres líneas: propina, total y pago por persona, con formato `$0.00` |

### 2. Descomponer en funciones

Escribe una función por tarea. Se sugiere:

| Función | Qué recibe | Qué devuelve |
|---------|------------|--------------|
| `calcular_propina(monto, porcentaje)` | monto y % | el valor de la propina |
| `calcular_total(monto, propina)` | monto y propina | el total |
| `dividir_entre(total, comensales)` | total y nº de personas | lo que paga cada una |
| `formatear_pesos(valor)` | un número | el texto `"$valor"` con 2 decimales |

### 3. Componer en un bloque principal

Escribe `main()` que:

1. fije `monto`, `porcentaje` y `comensales`;
2. llame en orden a `calcular_propina`, `calcular_total` y `dividir_entre`, guardando
   cada resultado en una variable;
3. imprima las tres líneas usando `formatear_pesos`.

Al final del archivo, una sola llamada: `main()`.

### 4. Refactorizar el cálculo repetido

Al escribir los tres `print` verás que el formato `f"${valor:.2f}"` se repite tres
veces. Muévelo a `formatear_pesos(valor)` y llama a esa función en los tres sitios. El
programa debe seguir dando la misma salida.

### 5. Probar

Ejecuta el programa con cada fila de la tabla de **Casos de prueba** (cambiando los
valores de `main`) y comprueba que la salida coincide.

## Entregable

Un archivo `cuenta.py` con **al menos cuatro funciones** y un bloque principal `main()`
que las combina. Ningún cálculo ni formato debe estar repetido. Los datos van fijos en
`main`.

## Casos de prueba

| `monto` | `porcentaje` | `comensales` | Salida esperada |
|---------|--------------|--------------|-----------------|
| `100.00` | `10` | `4` | `Propina: $10.00` · `Total: $110.00` · `Cada persona paga: $27.50` |
| `80.00` | `15` | `2` | `Propina: $12.00` · `Total: $92.00` · `Cada persona paga: $46.00` |
| `60.00` | `0` | `3` | `Propina: $0.00` · `Total: $60.00` · `Cada persona paga: $20.00` |

## Criterios de evaluación

- **Descomposición**: cada función tiene una sola responsabilidad y un nombre con verbo.
- **Parámetros y retorno**: los datos entran por parámetros y los resultados salen con
  `return`; no se usan variables globales para comunicar funciones.
- **Sin repetición**: el formato de moneda está en una única función.
- **Composición**: `main()` solo coordina llamadas; el resultado es correcto en los tres
  casos.
- **Legibilidad**: identificadores y comentarios en español, un docstring por función.

> Nota para el docente: la versión resuelta y comentada está en
> `../../material/soluciones/soluciones-ejercicios.md` (sección "Taller 01"). No
> compartir con el estudiantado antes de la puesta en común.
