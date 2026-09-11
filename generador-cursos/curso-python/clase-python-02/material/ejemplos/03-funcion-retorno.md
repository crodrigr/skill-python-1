# Ejemplo 03 — Función con retorno

**Tema**: devolver un valor con `return`; diferencia entre `return` y `print`
· **Resultados de aprendizaje**: RA-4 · **Nivel**: básico

## Problema

Queremos calcular el área de dos rectángulos y, además, la **suma** de ambas áreas. La
función del Ejemplo 02 solo imprime el área: no deja usar ese número para nada más.

## Análisis

- **Entrada**: la base y la altura de cada rectángulo.
- **Proceso**: calcular cada área y sumarlas.
- **Salida**: las dos áreas y su suma.

## Solución

1. Definir `area_rectangulo(base, altura)` que **devuelva** el área con `return` (no que
   la imprima).
2. Guardar cada resultado en una variable.
3. Operar con esas variables (sumarlas) y mostrar todo.

## Código

```python
def area_rectangulo(base, altura):
    """Devuelve el área de un rectángulo."""
    return base * altura

area_uno = area_rectangulo(3, 4)
area_dos = area_rectangulo(10, 2)

print("Área 1:", area_uno)
print("Área 2:", area_dos)
print("Suma de áreas:", area_uno + area_dos)
```

## Explicación paso a paso

1. `return base * altura` calcula el producto y lo **entrega** a quien llamó la función;
   la función termina en ese punto.
2. `area_uno = area_rectangulo(3, 4)`: la llamada se "reemplaza" por el valor devuelto
   (`12`), que se guarda en `area_uno`.
3. `area_dos` recibe `20` del mismo modo.
4. `area_uno + area_dos` vale `32`, porque ahora sí tenemos los números disponibles.

### `return` frente a `print`

| | Ejemplo 02 (`print`) | Ejemplo 03 (`return`) |
|---|---|---|
| La función… | muestra el área en pantalla | entrega el área al programa |
| ¿Se puede sumar el resultado? | no | sí (`area_uno + area_dos`) |

Si en este ejemplo la función usara `print` en vez de `return`, `area_uno` valdría
`None` y `area_uno + area_dos` daría error.

## Resultado esperado

```text
Área 1: 12
Área 2: 20
Suma de áreas: 32
```
