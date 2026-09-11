# 📚 Explicación conceptual — Clase 02: Funciones

Este documento desarrolla, en orden pedagógico, los siete bloques temáticos de la clase.
Cada bloque sigue la secuencia **Contexto → Concepto → Explicación**. El lenguaje es
deliberadamente sencillo y solo supone lo visto en la Clase 01 (variables, tipos de datos
básicos, operadores, condicionales y bucles).

Convención de código: los nombres de variables y de funciones y los comentarios están en
español; solo las palabras reservadas de Python (`def`, `return`, `if`, `for`, …) están
en inglés porque forman parte del lenguaje. Cada función lleva un texto breve entre
comillas triples (*docstring*) que dice qué hace.

---

## 1️⃣ Concepto de función

**Resultados de aprendizaje**: RA-1.

### 🌍 Contexto

En la Clase 01 escribíamos programas como una única lista de instrucciones, de arriba
abajo. Cuando un cálculo se necesitaba dos veces, se copiaba y se pegaba. Ese estilo
funciona en programas de diez líneas, pero se vuelve difícil de leer y de corregir en
cuanto el programa crece: si el cálculo copiado tenía un error, hay que arreglarlo en
todas las copias.

### 🧠 Concepto

Una **función** es un fragmento de código con **nombre** que resuelve una tarea concreta.
Se escribe una sola vez y se usa (se **llama**) tantas veces como haga falta.

Dos ideas explican para qué sirven:

- **Encapsular**: meter dentro de la función todos los pasos de una tarea, de modo que
  desde fuera solo se ve el nombre y el resultado, no los detalles.
- **Abstraer**: poder pensar en "calcular el promedio" como una sola acción, sin recordar
  cada vez cómo se suma y se divide.

Una función es, entonces, una **herramienta**: la construyes una vez y luego la usas sin
volver a mirar su interior, igual que usas una calculadora sin saber cómo suma por dentro.

### 📖 Explicación

Comparemos el mismo trabajo —saludar a tres personas— sin función y con función:

| Sin función | Con función |
|-------------|-------------|
| `print("Hola, Ana - ¡qué bueno verte!")` | `def saludar(nombre):` |
| `print("Hola, Luis - ¡qué bueno verte!")` | `    print("Hola,", nombre, "- ¡qué bueno verte!")` |
| `print("Hola, Eva - ¡qué bueno verte!")` | `saludar("Ana")` … |

Con función, el texto del saludo se escribe **una sola vez**. Si mañana el saludo cambia,
se cambia en un único lugar.

Términos que usaremos toda la clase:

- **Modularidad**: un programa hecho de piezas pequeñas e independientes (funciones).
- **Reutilización**: usar la misma función en distintos puntos del programa (o en otro
  programa).

Ver el [Ejemplo 01 — Función simple](01-funcion-simple.md).

---

## 2️⃣ Definición y llamada

**Resultados de aprendizaje**: RA-2, RA-5.

### 🌍 Contexto

Para usar una función hay que hacer dos cosas distintas en dos momentos distintos:
**definirla** (decir qué hace) y **llamarla** (pedir que lo haga). Confundir ambas es el
error más común al empezar.

### 🧠 Concepto

Se **define** una función con la palabra reservada `def`:

```python
def mostrar_bienvenida():
    """Muestra un encabezado en pantalla."""
    print("=" * 30)
    print("  Sistema de biblioteca")
    print("=" * 30)
```

Partes de la definición:

- `def` — anuncia que empieza una función.
- `mostrar_bienvenida` — el **nombre** (elegido por quien programa).
- `()` — los paréntesis; aquí irán los parámetros cuando los haya.
- `:` y el **cuerpo** con **sangría** (4 espacios): las instrucciones de la función.

Definir una función **no ejecuta** su cuerpo. Para ejecutarlo hay que **llamarla**,
escribiendo su nombre seguido de paréntesis:

```python
mostrar_bienvenida()
```

### 📖 Explicación

**Flujo de ejecución.** Cuando el programa llega a una llamada:

1. "Salta" al cuerpo de la función.
2. Ejecuta las instrucciones del cuerpo, de arriba abajo.
3. Al terminar el cuerpo (o al encontrar `return`), **vuelve** justo al punto donde
   estaba y continúa con la línea siguiente.

```text
mostrar_bienvenida()   ─┐  (1) salta al cuerpo
                        │
  print(...)  ←─────────┘  (2) ejecuta el cuerpo
  print(...)
  print(...)  ──────────┐
                        │  (3) vuelve aquí
print("Fin")  ←─────────┘
```

Regla práctica: **la definición debe aparecer antes de la llamada** en el programa. Si se
llama a una función que todavía no se ha definido, Python da el error
`NameError: name '...' is not defined`.

Ver el [Ejemplo 01 — Función simple](01-funcion-simple.md).

---

## 3️⃣ Parámetros y argumentos

**Resultados de aprendizaje**: RA-3.

### 🌍 Contexto

`mostrar_bienvenida()` siempre hace exactamente lo mismo. Casi siempre queremos que una
función trabaje con **datos distintos** cada vez: saludar a *otra* persona, calcular el
área de *otro* rectángulo. Esos datos entran por los **parámetros**.

### 🧠 Concepto

Un **parámetro** es un nombre que aparece entre los paréntesis de la **definición**. Un
**argumento** es el valor concreto que se pasa en la **llamada**.

```python
def mostrar_area_rectangulo(base, altura):   # base y altura son PARÁMETROS
    area = base * altura
    print("El área del rectángulo es", area)

mostrar_area_rectangulo(3, 4)                 # 3 y 4 son ARGUMENTOS
```

Dentro de la función, los parámetros se comportan como variables ya creadas: en la
llamada anterior, `base` vale `3` y `altura` vale `4`.

### 📖 Explicación

**Argumentos posicionales.** Por defecto, el primer argumento va al primer parámetro, el
segundo al segundo, etc. El **orden importa**: `mostrar_area_rectangulo(3, 4)` no es lo
mismo que `mostrar_area_rectangulo(4, 3)` si la función los usa de forma distinta.

**Argumentos por nombre.** Se puede indicar a qué parámetro va cada valor, y así el orden
deja de importar:

```python
mostrar_area_rectangulo(altura=4, base=3)
```

**Parámetros con valor por defecto.** Un parámetro puede traer un valor "de fábrica" que
se usa si en la llamada no se pasa ese argumento:

```python
def precio_con_impuesto(precio, iva=0.19):
    return precio + precio * iva

precio_con_impuesto(1000)          # usa iva = 0.19
precio_con_impuesto(1000, 0.10)    # usa iva = 0.10
```

Si el número de argumentos no coincide con el de parámetros (y no hay valores por
defecto que lo cubran), Python avisa con `TypeError: ... missing ... argument`.

Ver los ejemplos [02 — Función con parámetros](02-funcion-parametros.md) y
[04 — Valores por defecto](04-valores-por-defecto.md).

---

## 4️⃣ Valor de retorno

**Resultados de aprendizaje**: RA-4.

### 🌍 Contexto

`mostrar_area_rectangulo` **imprime** el área, pero el programa no puede hacer nada más
con ese número: no se puede sumar a otro, ni guardar, ni comparar. Para que la función
**entregue** un resultado al resto del programa se usa `return`.

### 🧠 Concepto

`return` hace dos cosas a la vez:

1. Termina la función inmediatamente.
2. Devuelve un valor al punto donde se hizo la llamada.

```python
def area_rectangulo(base, altura):
    """Devuelve el área de un rectángulo."""
    return base * altura

area = area_rectangulo(3, 4)   # 'area' recibe el 12 que devolvió la función
print(area + 100)              # ahora sí se puede operar con el resultado
```

### 📖 Explicación

**`return` frente a `print`:**

| | `print(...)` | `return ...` |
|---|---|---|
| Qué hace | muestra texto en pantalla | entrega un valor al programa |
| Después | la función sigue | la función termina |
| ¿Se puede reutilizar el resultado? | no | sí (se puede guardar, sumar, comparar…) |

**Funciones sin `return`.** Si una función no tiene `return` (o tiene `return` sin valor),
al llamarla se obtiene `None`, que significa "ningún valor". Por eso este código imprime
`Área: None`:

```python
def area_triangulo(base, altura):
    resultado = base * altura / 2   # calcula, pero no devuelve nada

print("Área:", area_triangulo(10, 4))   # Área: None
```

La corrección es añadir `return resultado`.

Ver el [Ejemplo 03 — Función con retorno](03-funcion-retorno.md).

---

## 5️⃣ Alcance

**Resultados de aprendizaje**: RA-2, RA-4.

### 🌍 Contexto

Al escribir funciones aparece una duda razonable: si creo una variable dentro de una
función, ¿existe también fuera? La respuesta evita muchos errores confusos.

### 🧠 Concepto

Las variables creadas dentro de una función son **locales**: nacen cuando la función se
llama y desaparecen cuando termina. **No existen fuera** de la función. Los parámetros
también son variables locales.

```python
def calcular():
    resultado = 42      # 'resultado' es local
    return resultado

calcular()
print(resultado)        # NameError: 'resultado' no existe aquí
```

### 📖 Explicación

Para sacar un valor de una función, la vía correcta es `return`, no "dejarlo" en una
variable con la esperanza de leerlo desde fuera.

Dentro de la función sí se pueden **leer** variables creadas fuera, pero en esta clase
evitaremos depender de eso: cada función recibe lo que necesita por sus **parámetros** y
entrega lo que produce con `return`. Así cada función es una pieza independiente y
predecible.

---

## 6️⃣ Reutilización y refactorización

**Resultados de aprendizaje**: RA-5, RA-6.

### 🌍 Contexto

Muchos programas ya escritos "funcionan" pero tienen el mismo bloque de código repetido
varias veces, o mezclan en un mismo sitio tareas distintas. Mejorar esa estructura sin
cambiar lo que el programa hace se llama **refactorizar**.

### 🧠 Concepto

**Refactorizar con funciones** consiste en:

1. Detectar un fragmento de código que se repite (o una tarea con identidad propia).
2. Darle un nombre y moverlo a una función, poniendo como **parámetros** las partes que
   cambian de una copia a otra.
3. Sustituir cada copia por una **llamada** a esa función.
4. Comprobar que el programa produce **el mismo resultado** que antes.

### 📖 Explicación

Antes (el cálculo del promedio está escrito tres veces):

```python
print("Promedio de Ana:", (60 + 70 + 80) / 3)
print("Promedio de Luis:", (50 + 90 + 100) / 3)
print("Promedio de Eva:", (80 + 85 + 90) / 3)
```

Después (el cálculo vive en una función; lo que cambia son las notas → parámetros):

```python
def promedio(nota1, nota2, nota3):
    """Devuelve el promedio de tres notas."""
    return (nota1 + nota2 + nota3) / 3

print("Promedio de Ana:", promedio(60, 70, 80))
print("Promedio de Luis:", promedio(50, 90, 100))
print("Promedio de Eva:", promedio(80, 85, 90))
```

Buenas prácticas al crear una función:

- **Nombre con verbo** que describa la acción: `calcular_total`, `mostrar_boleta`,
  `es_aprobado`.
- **Una sola responsabilidad** por función: si hace "dos cosas", probablemente son dos
  funciones.
- Un **docstring** breve que diga qué hace y qué devuelve.

Ver el [Ejemplo 05 — Refactorización](05-refactorizacion.md).

---

## 7️⃣ Composición de funciones

**Resultados de aprendizaje**: RA-7.

### 🌍 Contexto

Un problema mediano rara vez se resuelve con una función. La estrategia es partirlo en
tareas pequeñas, escribir una función para cada una y luego combinarlas.

### 🧠 Concepto

**Componer** funciones significa que unas funciones usan el resultado de otras, y que un
**bloque principal** (a menudo una función `main`) las coordina.

```python
def subtotal(precio_unitario, cantidad):
    """Devuelve el costo de 'cantidad' unidades."""
    return precio_unitario * cantidad

def con_descuento(monto, porcentaje):
    """Devuelve 'monto' tras aplicarle un descuento porcentual entero."""
    return monto - monto * porcentaje // 100

def total_a_pagar(precio_unitario, cantidad, porcentaje):
    """Combina el subtotal y el descuento para obtener el total."""
    return con_descuento(subtotal(precio_unitario, cantidad), porcentaje)
```

`total_a_pagar` no repite ningún cálculo: **llama** a `subtotal` y pasa su resultado a
`con_descuento`.

### 📖 Explicación

Para descomponer un problema, una guía útil:

1. Escribe en una frase qué entra y qué sale.
2. Lista los pasos intermedios.
3. Cada paso con nombre propio es candidato a función.
4. Escribe una función por paso; pruébala sola.
5. Escribe el bloque principal que las llama en orden.

Este es el método del [Ejemplo 06 — Composición de funciones](06-composicion-funciones.md),
del [Desafío 01](../ejercicios/desafio-01.md) y del
[Taller 01](../../actividades/talleres/taller-01.md).
