# Ejemplo 02 — Función con parámetros

**Tema**: pasar datos a una función mediante parámetros; parámetro vs argumento
· **Resultados de aprendizaje**: RA-2, RA-3 · **Nivel**: básico

## Problema

Necesitamos mostrar el área de varios rectángulos distintos. El cálculo es siempre el
mismo (`base * altura`), pero los números cambian en cada caso.

## Análisis

- **Entrada**: la base y la altura de cada rectángulo.
- **Proceso**: multiplicar base por altura.
- **Salida**: un mensaje con el área, para cada rectángulo.

## Solución

1. Definir `mostrar_area_rectangulo(base, altura)` con dos **parámetros**.
2. Dentro, calcular el área y mostrarla.
3. Llamar a la función con los **argumentos** de cada rectángulo.

## Código

```python
def mostrar_area_rectangulo(base, altura):
    """Muestra el área de un rectángulo a partir de la base y la altura."""
    area = base * altura
    print("El área del rectángulo es", area)

mostrar_area_rectangulo(3, 4)
mostrar_area_rectangulo(10, 2)
```

## Explicación paso a paso

1. En la definición, `base` y `altura` son **parámetros**: nombres para los datos que
   la función recibirá.
2. En `mostrar_area_rectangulo(3, 4)`, los valores `3` y `4` son **argumentos**. Como
   son *posicionales*, `3` se asigna a `base` y `4` a `altura`.
3. Dentro de la función, `area = base * altura` calcula `3 * 4` y guarda `12` en la
   variable local `area`.
4. `print(...)` muestra el mensaje. La función termina y el programa vuelve.
5. La segunda llamada repite todo con `base = 10` y `altura = 2`, por lo que `area` vale
   `20`.

> `base` y `altura` solo existen mientras la función se ejecuta: son variables locales.

## Resultado esperado

```text
El área del rectángulo es 12
El área del rectángulo es 20
```
