# 💡 Ejemplo 06 — Manejar un archivo inexistente

**Tema**: `try`/`except FileNotFoundError` al intentar abrir un archivo que no existe ·
**Resultado de aprendizaje**: RA-6 · **Nivel**: intermedio-avanzado

## 🧩 Problema

Un programa necesita leer un archivo de configuración. Se quiere que, si el archivo
existe, muestre su contenido; y que, si no existe, muestre un mensaje claro en vez de
detenerse con un error sin manejar. Se prueban los dos casos con el mismo programa.

## 🔍 Análisis

- **Entrada**: un archivo `configuracion.txt` que sí se crea, y un nombre de archivo
  `ajustes.txt` que **no** se crea, para probar el caso de error.
- **Proceso**: una función que intenta abrir y leer un archivo dentro de un
  `try`/`except FileNotFoundError`, mostrando el contenido si existe o un mensaje si no.
- **Salida**: el contenido de `configuracion.txt`, y el mensaje de aviso para
  `ajustes.txt`.

## 💡 Solución

1. Definir una función `mostrar_contenido(ruta)` que intente abrir y leer el archivo
   dentro de un `try`, y capture `FileNotFoundError` en el `except`.
2. Crear `configuracion.txt` y llamar a la función con esa ruta (caso existente).
3. Llamar a la función con `ajustes.txt`, que nunca se creó (caso inexistente).

## 💻 Código

```python
def mostrar_contenido(ruta):
    """Muestra el contenido de un archivo, o un mensaje si no existe."""
    try:
        with open(ruta, "r") as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print("No se encontró el archivo '" + ruta + "'. Revisa el nombre o créalo primero.")


# Caso 1: el archivo sí existe
with open("configuracion.txt", "w") as archivo:
    archivo.write("modo=oscuro\nidioma=es\n")

print("Intentando leer configuracion.txt:")
mostrar_contenido("configuracion.txt")

# Caso 2: el archivo no existe (nunca se creó)
print("Intentando leer ajustes.txt:")
mostrar_contenido("ajustes.txt")
```

## 🧭 Explicación paso a paso

1. `mostrar_contenido` intenta, dentro de `try`, abrir y leer el archivo recibido.
2. Si la apertura falla porque el archivo no existe, Python lanza `FileNotFoundError`;
   el bloque `except FileNotFoundError:` lo captura y muestra un mensaje comprensible
   en vez de dejar que el programa se detenga.
3. Al llamar con `"configuracion.txt"` (que sí existe, porque se creó justo antes), el
   `try` se ejecuta completo: se abre, se lee y se imprime su contenido; el `except`
   nunca se ejecuta en este caso.
4. Al llamar con `"ajustes.txt"` (que nunca se creó), `open(...)` lanza
   `FileNotFoundError` dentro del `try`; Python salta de inmediato al `except`, que
   muestra el mensaje de aviso, y el programa continúa con normalidad después.

## ✅ Resultado esperado

```text
Intentando leer configuracion.txt:
modo=oscuro
idioma=es

Intentando leer ajustes.txt:
No se encontró el archivo 'ajustes.txt'. Revisa el nombre o créalo primero.
```

**Archivo `configuracion.txt` resultante**:

```text
modo=oscuro
idioma=es
```

No se crea ningún archivo `ajustes.txt`: el `except` evita que el programa lo necesite
para continuar.
