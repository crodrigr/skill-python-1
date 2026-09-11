# 💡 Ejemplo 01 — Crear un módulo propio

## 🧩 Problema

Se necesitan dos operaciones matemáticas simples —sumar y restar dos números— en un
programa. En vez de escribirlas directamente en el script principal, se quiere
guardarlas en un archivo aparte (un módulo propio) para poder reutilizarlas en
cualquier otro programa sin copiar el código.

## 🔍 Análisis

- **Entrada**: dos números para cada operación (en este ejemplo, fijos en el código:
  `4` y `3`).
- **Proceso**: definir las funciones `sumar` y `restar` en un archivo `.py` separado
  (el módulo), e importar ese módulo desde el script principal.
- **Salida**: el resultado de cada operación, mostrado en consola.

## 💡 Solución

Se crea un archivo `operaciones_basicas.py` con las dos funciones. El script principal
(`principal.py`), ubicado en la misma carpeta, importa el módulo completo con
`import operaciones_basicas` y llama a sus funciones con el prefijo del módulo.

## 💻 Código

Archivo `operaciones_basicas.py` (el módulo):

```python
"""Modulo con operaciones matematicas basicas."""


def sumar(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def restar(a, b):
    """Devuelve la resta de a menos b."""
    return a - b
```

Archivo `principal.py` (el script que usa el módulo):

```python
import operaciones_basicas

resultado_suma = operaciones_basicas.sumar(4, 3)
resultado_resta = operaciones_basicas.restar(4, 3)

print("4 + 3 =", resultado_suma)
print("4 - 3 =", resultado_resta)
```

## 🧭 Explicación paso a paso

1. `operaciones_basicas.py` es un archivo `.py` normal: no necesita nada especial para
   convertirse en un módulo, solo debe estar en la misma carpeta que quien lo importa.
2. `import operaciones_basicas` carga el archivo completo. Python usa el nombre del
   archivo (sin la extensión `.py`) como nombre del módulo.
3. Para usar una función del módulo se escribe `nombre_del_modulo.funcion(...)`: el
   prefijo `operaciones_basicas.` dice explícitamente de dónde viene cada función.
4. `sumar(4, 3)` y `restar(4, 3)` se ejecutan igual que si estuvieran definidas en el
   mismo archivo; la única diferencia es el prefijo del módulo.

## ✅ Resultado esperado

```text
4 + 3 = 7
4 - 3 = 1
```
