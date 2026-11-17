# 💡 Ejemplo 05 — `try`/`except`/`else`/`finally`

## 🧩 Problema

Se quiere convertir un texto ingresado por el usuario a un número entero, mostrando un
mensaje claro si el texto no es un número válido, un mensaje de éxito si la conversión
funcionó, y un mensaje de cierre que se muestre siempre, haya habido error o no.

## 🔍 Análisis

- **Entrada**: dos casos de prueba: `"5"` (válido) y `"cinco"` (inválido).
- **Proceso**: convertir con `int()` dentro de un `try`; capturar `ValueError` en el
  `except`; mostrar el resultado en `else` si no hubo error; mostrar un mensaje de
  cierre en `finally` en ambos casos.
- **Salida**: mensajes distintos según el caso, y siempre el mensaje de cierre.

## 💡 Solución

Se define una función `convertir_entrada(entrada)` con los cuatro bloques
(`try`/`except`/`else`/`finally`), y se llama dos veces: una con una entrada válida y
otra con una inválida, para mostrar ambos comportamientos.

## 💻 Código

```python
def convertir_entrada(entrada):
    try:
        numero = int(entrada)
    except ValueError:
        print(f"'{entrada}' no es un numero valido")
    else:
        print(f"Convertido correctamente: {numero}")
    finally:
        print("Fin del intento de conversion\n")


print("Caso sin error (entrada = '5'):")
convertir_entrada("5")

print("Caso con error (entrada = 'cinco'):")
convertir_entrada("cinco")
```

## 🧭 Explicación paso a paso

1. `try: numero = int(entrada)` intenta convertir el texto a entero.
2. Si `entrada` no se puede convertir (como `"cinco"`), Python lanza `ValueError`, que
   el `except ValueError:` captura, mostrando un mensaje comprensible en vez de
   detener el programa.
3. Si la conversión **sí** funciona (como `"5"`), no se lanza ninguna excepción, así
   que el bloque `except` se salta y se ejecuta el `else`, mostrando el número
   convertido.
4. El bloque `finally` se ejecuta en **ambos** casos, siempre al final, porque no
   depende de si hubo error: sirve para código que debe correr pase lo que pase (aquí,
   un simple mensaje de cierre).

## ✅ Resultado esperado

```text
Caso sin error (entrada = '5'):
Convertido correctamente: 5
Fin del intento de conversion

Caso con error (entrada = 'cinco'):
'cinco' no es un numero valido
Fin del intento de conversion
```
