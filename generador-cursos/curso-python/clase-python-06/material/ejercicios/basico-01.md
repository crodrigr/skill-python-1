# 🟢 Básico 01 — Módulo de conversión de unidades

## 🧩 Problema

Crea un módulo propio llamado `conversor.py` con dos funciones para convertir
distancias, y un script principal que las use.

## 📥 Entrada

El módulo `conversor.py` debe definir:

- `metros_a_centimetros(metros)`: recibe una distancia en metros y devuelve su
  equivalente en centímetros.
- `centimetros_a_metros(centimetros)`: recibe una distancia en centímetros y devuelve
  su equivalente en metros.

El script principal usa valores fijos: `2.5` metros y `350` centímetros.

## ⚙️ Proceso esperado

1. El script principal importa el módulo `conversor` (con la forma de `import` que
   prefieras: `import conversor` o `from conversor import ...`).
2. Llama a `metros_a_centimetros(2.5)` y muestra el resultado.
3. Llama a `centimetros_a_metros(350)` y muestra el resultado.

## 📤 Salida

Dos líneas en consola con cada resultado, indicando la unidad convertida (por ejemplo,
`"2.5 metros = 250.0 centimetros"`).

## 🚧 Restricciones

- Las dos funciones DEBEN vivir en el archivo `conversor.py`, no en el script
  principal.
- El script principal DEBE importar el módulo (no copiar sus funciones).
- Identificadores y comentarios en español; nombres de archivo en minúsculas.

## 📊 Dificultad

Básico

## 🎓 Resultados de aprendizaje

- RA-1
- RA-2
