# 🛠️ Taller 01 — Calculadora de propina

**Actividad guiada** · Duración estimada: 40–50 min · **Resultados de aprendizaje**:
RA-3, RA-4, RA-5, RA-6, RA-8, RA-9

## 🎯 Objetivo

Construir, siguiendo la secuencia **análisis → algoritmo → programa → prueba**, un programa
que combine variables, operadores, una decisión y una repetición para resolver un
problema cotidiano: repartir la cuenta de un restaurante con propina entre varias
personas (RA-3, RA-8, RA-9).

## 🌍 Contexto

Un grupo de amigos comparte la cuenta de un restaurante. Quieren agregar una propina que
depende de qué tan bueno fue el servicio y luego dividir el total en partes iguales.

Regla de la propina, según una calificación del servicio de 1 a 5:

- Calificación 4 o 5 → 20% de propina.
- Calificación 2 o 3 → 10% de propina.
- Calificación 1 → sin propina.

## 🪜 Pasos

### 1️⃣ Analizar el problema

Completa el análisis:

| Pregunta | Respuesta |
|----------|-----------|
| Entrada | `monto_cuenta` (int), `calificacion_servicio` (int, 1–5), `numero_personas` (int) |
| Proceso | elegir el porcentaje de propina (decisión); calcular propina y total; dividir el total entre las personas y mostrar la parte de cada una (repetición) |
| Salida | porcentaje aplicado, propina, total y la parte que paga cada persona |

### 2️⃣ Diseñar el algoritmo (pseudocódigo)

```text
Leer monto_cuenta, calificacion_servicio, numero_personas

Si calificacion_servicio >= 4:
    porcentaje ← 20
Sino, si calificacion_servicio >= 2:
    porcentaje ← 10
Sino:
    porcentaje ← 0

propina ← monto_cuenta * porcentaje / 100
total ← monto_cuenta + propina
parte ← total / numero_personas

Mostrar porcentaje, propina, total
Para persona desde 1 hasta numero_personas:
    Mostrar "Persona <persona> paga <parte>"
```

### 3️⃣ Escribir el programa

Traduce el pseudocódigo a Python. Debes usar:

- variables con nombres descriptivos en español;
- operadores aritméticos (`*`, `/`, `+`) y de comparación (`>=`);
- una estructura `if` / `elif` / `else` para el porcentaje;
- un bucle `for` para recorrer a las personas.

### 4️⃣ Probar

Ejecuta el programa con cada fila de la tabla de **Casos de prueba** y comprueba que la
salida coincide.

## 📦 Entregable

Un archivo `propina.py` que, con los datos fijados en el código, produzca exactamente la
salida esperada para los casos de prueba. El programa debe combinar, como mínimo:
variables, un operador aritmético, un operador de comparación, una decisión
(`if/elif/else`) y una repetición (`for`).

## 🧪 Casos de prueba

| `monto_cuenta` | `calificacion_servicio` | `numero_personas` | Salida esperada |
|----------------|--------------------------|-------------------|-----------------|
| `30000` | `5` | `3` | `Porcentaje de propina: 20` · `Propina: 6000.0` · `Total: 36000.0` · `Persona 1 paga: 12000.0` · `Persona 2 paga: 12000.0` · `Persona 3 paga: 12000.0` |
| `20000` | `3` | `2` | `Porcentaje de propina: 10` · `Propina: 2000.0` · `Total: 22000.0` · `Persona 1 paga: 11000.0` · `Persona 2 paga: 11000.0` |
| `15000` | `1` | `1` | `Porcentaje de propina: 0` · `Propina: 0.0` · `Total: 15000.0` · `Persona 1 paga: 15000.0` |

## 📏 Criterios de evaluación

- **Corrección del resultado**: la salida coincide con la esperada en los tres casos.
- **Justificación de estructuras**: el estudiante explica por qué usó `if/elif/else`
  para la propina y `for` para las personas (número de vueltas conocido).
- **Terminación**: el bucle `for` recorre exactamente `numero_personas` vueltas y
  termina; no hay riesgo de repetición infinita.
- **Legibilidad**: nombres descriptivos, comentarios en español, formato claro.

> Nota para el docente: una versión resuelta y comentada está disponible en
> `../../material/soluciones/soluciones-ejercicios.md` (sección "Taller 01"). No
> compartir con el estudiantado antes de la puesta en común.
