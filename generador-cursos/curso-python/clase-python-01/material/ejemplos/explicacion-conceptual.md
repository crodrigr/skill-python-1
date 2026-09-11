# Explicación conceptual — Clase 01

Este documento desarrolla, en orden pedagógico, los seis bloques temáticos de la clase.
Cada bloque sigue la secuencia **Contexto → Concepto → Explicación**. El lenguaje es
deliberadamente sencillo y no supone conocimientos previos de programación.

Convención de código: los nombres de variables y los comentarios están en español; solo
las palabras reservadas de Python (`if`, `for`, `while`, `and`, …) están en inglés
porque forman parte del lenguaje.

---

## 1. Python

**Resultado de aprendizaje**: RA-1.

### Contexto

Una computadora solo sabe seguir instrucciones muy precisas. Para decirle qué hacer
necesitamos un **lenguaje de programación**: un conjunto de palabras y reglas que la
persona escribe y la máquina ejecuta. Hay muchos lenguajes; en esta clase usamos
**Python**.

### Concepto

**Python** es un lenguaje de programación de propósito general, conocido por tener una
sintaxis **clara y legible**: el código se parece bastante a una descripción en
lenguaje natural de lo que queremos lograr.

Python es un lenguaje **interpretado**: existe un programa, llamado *intérprete*, que
lee nuestro archivo línea por línea y lo ejecuta al momento. No hace falta un paso
previo de "compilación" para probar un programa.

### Explicación

Comparemos una misma idea —mostrar un saludo en pantalla— escrita como instrucción para
una persona y como programa Python:

| Instrucción para una persona | Programa en Python |
|------------------------------|--------------------|
| "Muestra el texto: Hola" | `print("Hola")` |

**Primer programa** (ejemplo sencillo):

```python
# Este programa muestra un saludo en pantalla
print("Hola, este es mi primer programa en Python")
```

Resultado al ejecutarlo:

```text
Hola, este es mi primer programa en Python
```

Características de Python que lo hacen adecuado para aprender:

- **Legible**: poca "ceremonia" (sin símbolos innecesarios); la indentación (los
  espacios al inicio de línea) forma parte del lenguaje y obliga a escribir código
  ordenado.
- **Interactivo**: se puede probar una línea y ver el resultado de inmediato.
- **De propósito general**: se usa en análisis de datos, sitios web, automatización de
  tareas, inteligencia artificial y más. En esta clase solo usamos lo esencial para
  resolver problemas sencillos.

Cómo se ejecuta un programa:

1. Escribimos las instrucciones en un archivo con extensión `.py`.
2. Pedimos al intérprete que lo ejecute (por ejemplo, `python programa.py`).
3. El intérprete lee el archivo de arriba hacia abajo y realiza cada instrucción.

---

## 2. Variables

**Resultado de aprendizaje**: RA-2.

### Contexto

Los programas trabajan con datos: un nombre, una edad, un precio, un resultado. Para
usar un dato más de una vez —o para calcular con él— necesitamos **guardarlo** y
**ponerle un nombre**.

### Concepto

Una **variable** es un nombre que se refiere a un valor guardado en la memoria. Crear
una variable en Python se hace con una **asignación**, usando el signo `=`:

```python
edad = 20
```

Se lee: "la variable `edad` recibe el valor `20`". A la izquierda del `=` va el nombre;
a la derecha, el valor (o una expresión que produce un valor).

> El `=` de programación **no** es el "igual" de matemáticas. `edad = 20` es una orden
> ("guarda 20 en edad"), no una afirmación. Para comparar si dos valores son iguales se
> usa `==`, que veremos en Operadores.

### Explicación

**Identificadores y reglas de nombrado.** El nombre de una variable (su *identificador*)
debe cumplir:

- Empieza por una letra o `_`; después puede tener letras, dígitos o `_`.
- No puede tener espacios ni signos (`precio-final` no es válido; `precio_final` sí).
- No puede ser una palabra reservada del lenguaje (`if`, `for`, `class`, …).
- Distingue mayúsculas de minúsculas: `nombre` y `Nombre` son variables distintas.

**Buenos nombres.** Un identificador debe describir qué guarda: `precio_total` es mejor
que `pt` o `x`. La convención en Python es `minusculas_con_guion_bajo`.

**Tipos de datos básicos.** Cada valor tiene un **tipo**:

| Tipo | Qué representa | Ejemplos |
|------|----------------|----------|
| `int` | Número entero | `0`, `20`, `-5` |
| `float` | Número con decimales | `3.14`, `-0.5`, `2.0` |
| `str` | Texto (*cadena* de caracteres), entre comillas | `"Ana"`, `'hola'` |
| `bool` | Valor lógico: verdadero o falso | `True`, `False` |

En Python no se declara el tipo por adelantado: se deduce del valor asignado.

**Uso en expresiones.** Una vez creada, la variable puede usarse en cálculos y su nombre
se reemplaza por su valor:

```python
precio_unitario = 1200      # int
cantidad = 3                # int
precio_total = precio_unitario * cantidad
print(precio_total)         # muestra 3600
```

Si a una variable se le asigna un nuevo valor, el anterior se pierde:

```python
saldo = 1000
saldo = saldo - 250          # ahora saldo vale 750
print(saldo)
```

---

## 3. Algoritmos

**Resultados de aprendizaje**: RA-3, RA-9.

### Contexto

Antes de escribir código conviene **pensar la solución**. Si empezamos a teclear sin un
plan, es fácil perderse. Ese plan, expresado como una secuencia de pasos, es un
algoritmo.

### Concepto

Un **algoritmo** es una secuencia **finita** y **ordenada** de pasos **precisos** que,
a partir de unos datos de entrada, produce un resultado y **termina**.

Características de un buen algoritmo:

- **Preciso**: cada paso no deja lugar a dudas.
- **Ordenado**: los pasos tienen una secuencia clara.
- **Finito**: termina después de un número acotado de pasos.
- **Con entrada y salida**: parte de datos conocidos y produce un resultado.

### Explicación

**Análisis entrada – proceso – salida.** Para analizar un problema respondemos tres
preguntas:

| Pregunta | Nombre |
|----------|--------|
| ¿Qué datos me dan o me pide el usuario? | **Entrada** |
| ¿Qué hay que hacer con esos datos? | **Proceso** |
| ¿Qué resultado debo mostrar? | **Salida** |

**Ejemplo de análisis.** Problema: "calcular el promedio de dos notas".

- Entrada: `nota1`, `nota2` (números).
- Proceso: sumar las dos notas y dividir entre 2.
- Salida: el promedio.

**Del algoritmo al pseudocódigo.** El *pseudocódigo* escribe el algoritmo en un formato
parecido a un programa, pero en lenguaje natural:

```text
1. Leer nota1
2. Leer nota2
3. promedio ← (nota1 + nota2) / 2
4. Mostrar promedio
```

**Del pseudocódigo al programa.** Cada paso se traduce a una instrucción de Python:

```python
# Entrada
nota1 = float(input("Primera nota: "))
nota2 = float(input("Segunda nota: "))

# Proceso
promedio = (nota1 + nota2) / 2

# Salida
print("El promedio es:", promedio)
```

`input(...)` lee texto escrito por el usuario; `float(...)` convierte ese texto en un
número con decimales. Siempre conviene **probar** el programa con datos de los que
conocemos el resultado esperado (por ejemplo, `4` y `6` deben dar `5.0`).

---

## 4. Operadores

**Resultado de aprendizaje**: RA-4.

### Contexto

En el proceso de un algoritmo casi siempre hay **cálculos** y **comparaciones**: sumar
precios, ver si una edad alcanza un mínimo, comprobar dos condiciones a la vez. Para eso
usamos operadores.

### Concepto

Un **operador** es un símbolo que combina uno o más valores (*operandos*) y produce un
resultado. Los agrupamos en cuatro familias:

| Familia | Operadores | Ejemplo | Resultado |
|---------|-----------|---------|-----------|
| Aritméticos | `+` `-` `*` `/` `//` `%` `**` | `7 // 2` | `3` (división entera) |
| Comparación | `==` `!=` `<` `>` `<=` `>=` | `3 >= 3` | `True` |
| Lógicos | `and` `or` `not` | `True and False` | `False` |
| Asignación | `=` `+=` `-=` `*=` `/=` | `x += 1` | suma 1 a `x` |

### Explicación

**Aritméticos.** Además de las cuatro operaciones habituales:

- `/` siempre da un `float`: `6 / 2` → `3.0`.
- `//` da la parte entera de la división: `7 // 2` → `3`.
- `%` (módulo) da el **resto**: `7 % 2` → `1`. Sirve, por ejemplo, para saber si un
  número es par: `numero % 2 == 0`.
- `**` es la potencia: `2 ** 3` → `8`.

**Comparación.** Producen siempre un valor `bool` (`True` o `False`). Se usan para tomar
decisiones:

```python
edad = 17
print(edad >= 18)     # False
```

**Lógicos.** Combinan valores `bool`:

- `and`: verdadero solo si **ambos** lados son verdaderos.
- `or`: verdadero si **al menos uno** es verdadero.
- `not`: invierte el valor.

```python
tiene_entrada = True
es_mayor = False
print(tiene_entrada and es_mayor)   # False
print(tiene_entrada or es_mayor)    # True
print(not es_mayor)                 # True
```

**Asignación compuesta.** `saldo += 100` es una forma corta de `saldo = saldo + 100`.

**Precedencia (solo lo necesario).** Cuando en una misma expresión hay varios
operadores, Python los evalúa en un orden fijo. Para esta clase basta recordar:

1. Primero `**`.
2. Luego `*`, `/`, `//`, `%`.
3. Luego `+`, `-`.
4. Luego las comparaciones (`<`, `>`, `==`, …).
5. Luego `not`, después `and`, después `or`.

Los **paréntesis** cambian el orden y hacen el código más claro:

```python
print(2 + 3 * 4)        # 14  (primero 3*4, luego +2)
print((2 + 3) * 4)      # 20  (primero el paréntesis)
```

---

## 5. Estructuras condicionales

**Resultados de aprendizaje**: RA-5, RA-8.

### Contexto

Muchos problemas requieren **decidir**: si el cliente es mayor de edad, mostrar una
opción; si no, mostrar otra. El programa debe ejecutar **distintas instrucciones según
una condición**.

### Concepto

Una **estructura condicional** ejecuta un bloque de código **solo si** una condición
(una expresión que vale `True` o `False`) se cumple.

```python
edad = 20
if edad >= 18:
    print("Puede ingresar")
```

La línea termina en `:` y el bloque que depende del `if` va **indentado** (con sangría,
normalmente 4 espacios). La indentación es la que indica a Python qué instrucciones
están "dentro" del `if`.

### Explicación

**`if` / `else`.** `else` define qué hacer cuando la condición **no** se cumple:

```python
edad = 16
if edad >= 18:
    print("Puede ingresar")
else:
    print("No puede ingresar")
```

**`if` / `elif` / `else`.** Cuando hay más de dos caminos, `elif` (abreviatura de
"else if") añade condiciones intermedias. Python evalúa de arriba hacia abajo y ejecuta
**el primer bloque cuya condición sea verdadera**:

```python
nota = 5.2
if nota >= 6.0:
    print("Aprobado")
elif nota >= 4.0:
    print("Recuperación")
else:
    print("Reprobado")
```

**Condición booleana.** La condición puede usar operadores de comparación y lógicos:

```python
edad = 20
tiene_entrada = True
if edad >= 18 and tiene_entrada:
    print("Acceso permitido")
```

**Condicionales anidados (extensión opcional).** Un `if` puede contener otro `if`. Solo
conviene usarlos cuando el problema realmente lo pide y el grupo ya domina los casos
anteriores; muchas veces se pueden reemplazar por condiciones con `and`.

**Combinar con operadores (RA-8).** La condición de un `if` es una expresión: allí se
combinan variables y operadores para expresar la regla de decisión del problema.

---

## 6. Bucles

**Resultados de aprendizaje**: RA-6, RA-7, RA-8.

### Contexto

A veces hay que **repetir** una acción: mostrar los números del 1 al 10, pedir una
contraseña hasta que sea correcta, sumar una lista de precios. Escribir la instrucción
muchas veces es inviable; para eso existen los bucles.

### Concepto

Un **bucle** repite un bloque de instrucciones. Python tiene dos:

- **`for`**: repite un número de veces **conocido de antemano** (recorrer un rango o una
  colección de elementos).
- **`while`**: repite **mientras** una condición sea verdadera; el número de
  repeticiones **no se conoce de antemano**.

### Explicación

**Bucle `for` con `range`.** `range(inicio, fin)` genera los números desde `inicio`
hasta `fin - 1`:

```python
for numero in range(1, 6):
    print(numero)
# muestra 1, 2, 3, 4, 5 (cada uno en una línea)
```

En cada vuelta, la variable `numero` toma el siguiente valor del rango.

**Acumuladores.** Un patrón muy común: una variable que se actualiza en cada vuelta.

```python
suma = 0
for valor in range(1, 6):
    suma = suma + valor      # o: suma += valor
print(suma)                  # 15
```

**Bucle `while`.** Se repite mientras la condición se cumpla. Es imprescindible que
**algo cambie dentro del bucle** para que la condición llegue a ser falsa; si no, el
bucle **nunca termina** (bucle infinito):

```python
contador = 1
while contador <= 5:
    print(contador)
    contador = contador + 1   # sin esta línea, el bucle sería infinito
```

**Elegir entre `for` y `while` (RA-7).**

| Situación | Estructura adecuada |
|-----------|---------------------|
| "Repetir 10 veces", "para cada elemento de…" | `for` |
| "Repetir hasta que el usuario acierte", "mientras queden datos" | `while` |
| Sé exactamente cuántas iteraciones | `for` |
| El final depende de una condición que se evalúa en cada vuelta | `while` |

**Combinar bucle + condicional + operadores (RA-8).** Dentro de un bucle podemos poner
un `if` para decidir en cada vuelta:

```python
for numero in range(1, 11):
    if numero % 2 == 0:
        print(numero, "es par")
    else:
        print(numero, "es impar")
```

**Riesgo de bucle infinito.** Si un `while` no modifica la variable que controla su
condición, hay que corregirlo añadiendo esa actualización (lo veremos en el Ejemplo 06 y
en el Quiz).
