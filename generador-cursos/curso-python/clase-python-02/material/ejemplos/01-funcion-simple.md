# Ejemplo 01 — Función simple

**Tema**: definir una función sin parámetros ni retorno; llamarla varias veces
· **Resultados de aprendizaje**: RA-1, RA-2 · **Nivel**: introductorio (primero de la
secuencia)

## Problema

Un programa de biblioteca muestra un encabezado con una línea de `=`, el nombre del
sistema y otra línea de `=`. Ese encabezado aparece al inicio y otra vez después del
menú. Queremos escribirlo una sola vez y reutilizarlo.

## Análisis

- **Entrada**: ninguna. El encabezado siempre es igual.
- **Proceso**: imprimir tres líneas fijas.
- **Salida**: el encabezado en pantalla, cada vez que se necesite.

## Solución

1. Definir una función `mostrar_bienvenida()` (sin parámetros) que imprima las tres
   líneas.
2. Llamarla cada vez que haga falta el encabezado.

## Código

```python
def mostrar_bienvenida():
    """Muestra el encabezado del sistema en pantalla."""
    print("=" * 30)
    print("  Sistema de biblioteca")
    print("=" * 30)

# El programa principal empieza aquí
mostrar_bienvenida()
print("Menú: 1) Buscar libro  2) Salir")
mostrar_bienvenida()
```

## Explicación paso a paso

1. `def mostrar_bienvenida():` **define** la función. Python lee el cuerpo pero **no lo
   ejecuta** todavía.
2. `"""Muestra el encabezado..."""` es el *docstring*: una nota breve de qué hace la
   función.
3. `print("=" * 30)` repite el carácter `=` treinta veces.
4. La primera llamada `mostrar_bienvenida()` hace que el programa salte al cuerpo,
   ejecute los tres `print` y vuelva.
5. Se ejecuta `print("Menú: ...")`.
6. La segunda llamada vuelve a ejecutar el cuerpo completo: el mismo código sirve dos
   veces.

## Resultado esperado

```text
==============================
  Sistema de biblioteca
==============================
Menú: 1) Buscar libro  2) Salir
==============================
  Sistema de biblioteca
==============================
```
