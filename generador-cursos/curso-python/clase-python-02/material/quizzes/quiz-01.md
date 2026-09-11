# Quiz 02 — Funciones en Python

**Instrucciones**: 10 preguntas. En las de selección múltiple e identificación de
resultado, marca **una** opción. En las de análisis y de corrección, escribe tu
respuesta con una breve justificación. El problema final se entrega como código.

> Este documento no incluye las respuestas. La clave está en
> `../soluciones/soluciones-quiz.md` (material docente).

---

## 1. [Selección múltiple]

¿Cuál es el propósito principal de escribir una función?

- A) Hacer que el programa se ejecute más rápido siempre.
- B) Encapsular una tarea con un nombre para reutilizarla y organizar el código.
- C) Evitar tener que usar variables.
- D) Traducir el programa a otro idioma.

_RA: RA-1_

---

## 2. [Selección múltiple]

Dado el siguiente código, ¿qué línea **llama** a la función?

```python
def registrar():
    print("Registro completado")

registrar()
```

- A) `def registrar():`
- B) `print("Registro completado")`
- C) `registrar()`
- D) Ninguna: el código no llama a la función.

_RA: RA-2_

---

## 3. [Selección múltiple]

En `def cobrar(monto, propina): ...` y la llamada `cobrar(1000, 150)`, ¿qué son `monto`
y `propina`?

- A) Argumentos de la llamada.
- B) Parámetros de la definición.
- C) Valores de retorno.
- D) Variables globales.

_RA: RA-3_

---

## 4. [Selección múltiple]

¿Cuál es la diferencia entre `return` y `print` dentro de una función?

- A) No hay diferencia: hacen lo mismo.
- B) `return` entrega un valor al programa que llamó; `print` solo muestra texto en
  pantalla.
- C) `print` termina la función; `return` no.
- D) `return` solo funciona con números; `print` solo con texto.

_RA: RA-4_

---

## 5. [Selección múltiple]

Dada esta función:

```python
def entrada(nombre, saludo="Hola"):
    return saludo + ", " + nombre
```

¿Cuál de estas llamadas provoca un **error**?

- A) `entrada("Ana")`
- B) `entrada("Ana", "Buenas")`
- C) `entrada(nombre="Ana")`
- D) `entrada()`

_RA: RA-3_

---

## 6. [Análisis de código]

Indica **qué imprime** este programa y explica **en qué orden** se ejecutan las
funciones.

```python
def doble(n):
    return n * 2

def mas_uno(n):
    return n + 1

print(mas_uno(doble(5)))
```

_RA: RA-4, RA-7_

---

## 7. [Análisis de código]

Indica **qué imprime** este programa y explica por qué la función no llega a evaluar
todos los `if`.

```python
def signo(numero):
    if numero > 0:
        return "positivo"
    if numero < 0:
        return "negativo"
    return "cero"

print(signo(-4))
```

_RA: RA-4_

---

## 8. [Identificación de resultado]

¿Qué imprime este programa?

```python
def entrada(nombre, saludo="Hola"):
    return saludo + ", " + nombre

print(entrada("Ana"))
print(entrada("Luis", "Buenas"))
```

- A) `Hola, Ana` y luego `Buenas, Luis`
- B) `Hola, Ana` y luego `Hola, Luis`
- C) `Hola, Ana` y luego un error
- D) `, Ana` y luego `Buenas, Luis`

_RA: RA-3_

---

## 9. [Corrección de errores]

Este programa debería imprimir `Área: 20.0`, pero imprime `Área: None`. Identifica el
error y reescribe el código corregido.

```python
def area_triangulo(base, altura):
    resultado = base * altura / 2

print("Área:", area_triangulo(10, 4))
```

_RA: RA-2, RA-4_

---

## 10. [Problema breve de programación]

El siguiente programa repite el mismo cálculo tres veces:

```python
print("Ana:", (7 + 8 + 9) / 3)
print("Luis:", (5 + 6 + 10) / 3)
print("Eva:", (9 + 9 + 6) / 3)
```

Escribe una función `promedio(a, b, c)` que devuelva el promedio de tres números y
**reescribe** las tres líneas usando esa función. La salida no debe cambiar.

_RA: RA-5, RA-6_
