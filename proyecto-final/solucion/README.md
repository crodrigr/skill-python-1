# 🔑 Solución de referencia — Proyecto final: Gestor de Biblioteca Personal

Material docente. No compartir con el estudiante; la guía de construcción está en
`../guia/guia-proyecto-final.md`.

## 📦 Archivos

- `libros.py` — módulo con las operaciones sobre la colección (crear, agregar, buscar,
  eliminar, cambiar préstamo, ordenar por título/año).
- `almacenamiento.py` — módulo de persistencia (`cargar_libros`, `guardar_libros`) con
  el formato de archivo `titulo|autor|anio|prestado`.
- `main.py` — punto de entrada: menú en bucle que conecta los dos módulos anteriores.

## ▶️ Cómo ejecutar

```bash
cd curso-python/proyecto-final/solucion
python3 main.py
```

Crea (o reutiliza) `biblioteca.txt` en el mismo directorio. Los datos se guardan
después de cada operación que modifica la colección, y también al elegir "Salir".

## ✅ Verificación (mapeada a los criterios de éxito de la spec)

| Criterio | Cómo se verificó |
|---|---|
| SC-003: las 6 operaciones del menú funcionan | Ejecución manual con `python3 main.py`, cubriendo agregar, listar (por título y por año), buscar, marcar/desmarcar prestado, eliminar y salir. |
| SC-004: los datos persisten entre ejecuciones | Se agregaron libros en una ejecución, se salió con la opción 6, y una segunda ejecución los mostró correctamente (incluido el estado "prestado"). |
| SC-005: entradas inválidas manejadas | Se probaron: año no numérico (repregunta hasta recibir un número válido), título vacío (mensaje y sin agregar), buscar/eliminar/marcar sobre un título inexistente (mensaje claro), y listar con la colección vacía (mensaje claro) — en ningún caso el programa se detuvo con una traza de error. |
| FR-006/FR-007 | Cada libro es un diccionario (`titulo`, `autor`, `anio`, `prestado`) dentro de una lista; `almacenamiento.cargar_libros` maneja `FileNotFoundError` en la primera ejecución. |
| FR-005 (modularidad) | Datos (`libros.py`), persistencia (`almacenamiento.py`) y menú (`main.py`) están separados en tres archivos con responsabilidades distintas. |

## 🧪 Casos de prueba manuales usados

1. Biblioteca vacía → agregar 2 libros → marcar uno como prestado → listar ordenado
   por año → salir. Verificado el contenido de `biblioteca.txt`.
2. Reabrir el programa → los 2 libros y el estado "prestado" persisten → agregar un
   tercer libro con año inválido (`"1900x"`) seguido de uno válido (`"1900"`) → buscar
   y eliminar un título inexistente → salir.
3. Biblioteca vacía desde cero → listar (mensaje "no hay libros") → intentar agregar
   con título vacío (mensaje y no se agrega) → salir.

Todas las salidas coincidieron con el comportamiento esperado descrito en `spec.md`
(Edge Cases y Success Criteria).
