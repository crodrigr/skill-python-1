# 💡 Ejemplo 02 — Alias y `from...import`

## 🧩 Problema

Un módulo `matematicas.py` tiene dos funciones, `cuadrado` y `cubo`. Se quiere usar
`cubo` con el módulo completo pero con un nombre más corto, y usar `cuadrado`
directamente sin escribir el nombre del módulo cada vez.

## 🔍 Análisis

- **Entrada**: un número para cada operación (fijos en el código: `3` y `5`).
- **Proceso**: importar el módulo con alias (`import matematicas as mate`) para usar
  `cubo`, e importar `cuadrado` puntualmente con alias (`from matematicas import
  cuadrado as al_cuadrado`) para usarlo sin prefijo.
- **Salida**: ambos resultados, mostrados en consola.

## 💡 Solución

Se combinan dos formas de `import` en el mismo script: `import modulo as alias` para
acceder al módulo completo con un nombre corto, y `from modulo import nombre as alias`
para traer una única función con un nombre propio.

## 💻 Código

Archivo `matematicas.py` (el módulo):

```python
"""Modulo con operaciones matematicas."""


def cuadrado(numero):
    """Devuelve el cuadrado de numero."""
    return numero ** 2


def cubo(numero):
    """Devuelve el cubo de numero."""
    return numero ** 3
```

Archivo `principal.py` (el script que usa el módulo):

```python
import matematicas as mate
from matematicas import cuadrado as al_cuadrado

print("Usando alias de modulo:", mate.cubo(3))
print("Usando alias de funcion:", al_cuadrado(5))
```

## 🧭 Explicación paso a paso

1. `import matematicas as mate` importa el módulo completo, pero permite referirse a
   él con el nombre corto `mate` en vez de `matematicas`.
2. `mate.cubo(3)` funciona igual que `matematicas.cubo(3)`: el alias es solo un nombre
   alternativo para el mismo módulo.
3. `from matematicas import cuadrado as al_cuadrado` trae únicamente la función
   `cuadrado`, y le asigna el nombre `al_cuadrado` en este archivo.
4. `al_cuadrado(5)` se llama directamente, sin ningún prefijo de módulo, porque se
   importó como un nombre propio del script.
5. Usar alias es útil para acortar nombres largos de módulo o para evitar que un
   nombre importado choque con otro identificador que ya exista en el programa.

## ✅ Resultado esperado

```text
Usando alias de modulo: 27
Usando alias de funcion: 25
```
