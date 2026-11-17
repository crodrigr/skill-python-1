# 🏆 Desafío 01 — Registro de asistencia a un curso

## 🧩 Problema

Un docente registra la asistencia de su curso en un archivo de texto: cada línea tiene
el nombre de un estudiante y si asistió (`"si"` o `"no"`), separados por una coma. El
archivo podría no existir todavía (si es la primera vez que se genera el reporte). A
partir de esos datos hay que:

1. Elegir y justificar una estrategia para manejar el caso de que el archivo de
   asistencia no exista, de modo que el programa avise con claridad y no se detenga.
2. Leer el archivo (si existe), procesar cada línea y calcular cuántos estudiantes
   estuvieron presentes, cuántos ausentes, y el porcentaje de asistencia.
3. Escribir un archivo de reporte con esos tres datos.

## 🔍 Análisis

- **Entrada**: un archivo `asistencia.txt` con líneas `nombre,presente`
  (`presente` es `"si"` o `"no"`); puede existir o no.
- **Proceso**: manejar con `try`/`except FileNotFoundError` la posible ausencia del
  archivo; si existe, contar presentes y ausentes, y calcular el porcentaje
  (`presentes / total * 100`).
- **Salida**: un archivo `reporte_asistencia.txt` con presentes, ausentes y el
  porcentaje, y el mismo resumen en pantalla; o, si el archivo de entrada no existe, un
  mensaje que lo indique sin generar un reporte con datos inventados.

## 💡 Solución esperada (guía, no código)

Envolver la apertura y lectura de `asistencia.txt` en `try`/`except FileNotFoundError`
es la estrategia adecuada porque el problema concreto que puede fallar es "el archivo
no está", que corresponde exactamente a esa excepción; no hace falta comprobar antes
"a mano" si el archivo existe. Si el archivo no existe, el programa debe avisarlo y
terminar esa función sin escribir un reporte con datos que no existen (en vez de, por
ejemplo, escribir un reporte con ceros que podría confundirse con un curso real sin
asistencia).

## 📥 Entrada

```python
registros = [("Ana", "si"), ("Luis", "no"), ("Eva", "si"), ("Marco", "si"), ("Sofía", "no")]
```

(el programa crea `asistencia.txt` a partir de esta lista para el primer caso de
prueba; para el segundo caso de prueba, usa una ruta que nunca se crea).

## ⚙️ Proceso esperado

Definir una función que reciba la ruta del archivo, maneje `FileNotFoundError` al
abrirlo, y si existe, recorra sus líneas (`strip`+`split(",")`) contando presentes y
ausentes con acumuladores, calcule el porcentaje, y escriba el reporte.

## 📤 Salida

```text
Presentes: 3
Ausentes: 2
Porcentaje de asistencia: 60.0%
```

## 🚧 Restricciones

- El manejo del archivo inexistente debe hacerse con `try`/`except`, no comprobando su
  existencia por otro medio.
- Si el archivo no existe, el programa NO debe crear un `reporte_asistencia.txt` con
  datos inventados.
- Los identificadores y comentarios deben estar en español.

## 📊 Dificultad

Desafío

## 🎓 Resultados de aprendizaje

- RA-6: anticipar y gestionar `FileNotFoundError`, justificando la estrategia elegida.
- RA-7: resolver un problema práctico completo de lectura, procesamiento y escritura.

## 🧪 Casos de prueba

| Situación | Salida esperada |
|-----------|-------------------|
| `asistencia.txt` existe, con los 5 registros indicados arriba | `reporte_asistencia.txt` con `Presentes: 3`, `Ausentes: 2`, `Porcentaje de asistencia: 60.0%` |
| El archivo de asistencia no existe (por ejemplo, se usa una ruta que nunca se creó) | El programa muestra un mensaje claro de que no encontró el archivo, y no genera `reporte_asistencia.txt` |
