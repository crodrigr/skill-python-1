# Ejemplo 05 — Refactorización

**Tema**: detectar código repetido y extraerlo a una función parametrizada
· **Resultados de aprendizaje**: RA-5, RA-6 · **Nivel**: intermedio

## Problema

Tenemos un programa que calcula el promedio de tres notas para tres estudiantes. El
cálculo `(n1 + n2 + n3) / 3` está escrito tres veces. Si mañana el promedio se pondera de
otra forma, hay que corregir tres líneas y es fácil olvidar una.

## Análisis

- **Entrada**: las tres notas de cada estudiante.
- **Proceso**: calcular el promedio. **Es el mismo cálculo repetido tres veces**; lo que
  cambia son las notas.
- **Salida**: el promedio de cada estudiante (el resultado no debe cambiar tras
  refactorizar).

## Solución

1. Identificar el fragmento repetido: `(a + b + c) / 3`.
2. Crear una función `promedio(nota1, nota2, nota3)` con las notas como parámetros.
3. Reemplazar cada repetición por una llamada.
4. Ejecutar y comprobar que la salida es idéntica a la de la versión inicial.

## Código

### Antes (con repetición)

```python
print("Promedio de Ana:", (60 + 70 + 80) / 3)
print("Promedio de Luis:", (50 + 90 + 100) / 3)
print("Promedio de Eva:", (80 + 85 + 90) / 3)
```

### Después (con función)

```python
def promedio(nota1, nota2, nota3):
    """Devuelve el promedio de tres notas."""
    return (nota1 + nota2 + nota3) / 3

print("Promedio de Ana:", promedio(60, 70, 80))
print("Promedio de Luis:", promedio(50, 90, 100))
print("Promedio de Eva:", promedio(80, 85, 90))
```

## Explicación paso a paso

1. El cálculo aparece 3 veces → es candidato a función.
2. Lo que cambia entre copias son los tres números → serán los **parámetros**.
3. `promedio(60, 70, 80)` devuelve `(60 + 70 + 80) / 3` = `70.0`, exactamente lo que
   antes calculaba la primera línea.
4. Ventaja: si el cálculo cambia, se edita **solo el cuerpo de `promedio`**.
5. Ambas versiones imprimen lo mismo: refactorizar mejora la estructura, no el resultado.

## Resultado esperado

Igual para las dos versiones:

```text
Promedio de Ana: 70.0
Promedio de Luis: 80.0
Promedio de Eva: 85.0
```
