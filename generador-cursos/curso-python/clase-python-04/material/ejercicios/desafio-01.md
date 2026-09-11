# 🏆 Desafío 01 — Inscripciones a los talleres de un evento

## 🧩 Problema

Un evento registra las inscripciones a sus talleres como una lista de tuplas
`(nombre_persona, nombre_taller)`. Una misma persona puede inscribirse a más de un
taller, y por error de carga alguien puede quedar registrado dos veces en el mismo
taller. A partir de esos registros, hay que:

1. Elegir y justificar qué estructura usar para contar cuántas **inscripciones** tiene
   cada taller (no personas distintas: cada tupla cuenta como una inscripción, incluida
   una posible repetida por error).
2. Implementar el conteo y determinar el taller más popular (el de más inscripciones).
3. Obtener, aparte, el conjunto de personas **distintas** que se inscribieron a algún
   taller (sin importar a cuántos, ni si alguna quedó repetida).

## 🔍 Análisis

- **Entrada**: una lista de tuplas `(nombre_persona, nombre_taller)`.
- **Proceso**: elegir un diccionario `taller -> cantidad_de_inscripciones` para el
  conteo (los talleres son los identificadores naturales); recorrer los registros
  sumando uno por cada tupla; encontrar el máximo; construir un conjunto de nombres
  para las personas distintas.
- **Salida**: el conteo de inscripciones por taller, el taller más popular, y la
  cantidad de personas distintas inscritas.

## 💡 Solución esperada (guía, no código)

Un diccionario es la estructura adecuada para el conteo porque cada taller es un
identificador con sentido (su nombre) y no hay que buscarlo por posición; una lista
obligaría a recorrerla completa para saber si un taller ya tiene una entrada. El
conjunto de personas distintas usa un conjunto porque solo interesa "quién está", sin
asociarle ningún valor ni conservar el orden ni las repeticiones.

## 📥 Entrada

```python
inscripciones = [
    ("Ana", "Yoga"),
    ("Luis", "Pilates"),
    ("Eva", "Yoga"),
    ("Ana", "Pilates"),
    ("Marco", "Yoga"),
    ("Eva", "Yoga"),   # Eva quedó registrada dos veces en Yoga por error de carga
]
```

## ⚙️ Proceso esperado

Elegir y justificar un diccionario `taller -> cantidad` (con `get` o `setdefault` para
inicializar el conteo); recorrer las inscripciones para llenarlo; recorrer el
diccionario resultante para encontrar el máximo; construir un conjunto con los nombres
de las personas para contar cuántas distintas hay.

## 📤 Salida

```text
Inscripciones por taller: {'Yoga': 4, 'Pilates': 2}
Taller más popular: Yoga con 4 inscripciones
Personas distintas inscritas: 4
```

## 🚧 Restricciones

- El conteo de inscripciones por taller debe ser un diccionario, justificado en un
  comentario.
- El conteo debe incluir la inscripción repetida de Eva (4 inscripciones a Yoga, no 3).
- Las personas distintas deben obtenerse con un conjunto, no contando "a mano".
- Los identificadores y comentarios deben estar en español.

## 📊 Dificultad

Desafío

## 🎓 Resultados de aprendizaje

- RA-7: usar los métodos comunes de los diccionarios (`get`/`setdefault`) para resolver
  una tarea de conteo.
- RA-8: analizar un problema de datos identificados por clave, elegir y justificar el
  uso de un diccionario frente a otras estructuras, e implementarlo.

## 🧪 Casos de prueba

| Entrada (`inscripciones`) | Salida esperada |
|------------------------------|------------------|
| la lista de 6 registros indicada arriba (con 1 repetido) | Inscripciones por taller: `{'Yoga': 4, 'Pilates': 2}`; Taller más popular: Yoga con 4; Personas distintas: 4 |
| `[("Sol", "Cerámica")]` (una sola inscripción) | Inscripciones por taller: `{'Cerámica': 1}`; Taller más popular: Cerámica con 1; Personas distintas: 1 |
