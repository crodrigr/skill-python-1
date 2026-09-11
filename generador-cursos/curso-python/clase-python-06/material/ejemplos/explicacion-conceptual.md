# 📚 Explicación conceptual — Clase 06: Módulos y manejo de excepciones

## 🌍 Modularidad

### 🌍 Contexto

Hasta ahora, cada programa vivía en un único archivo `.py`. Mientras el programa es
pequeño eso funciona bien, pero a medida que crece —más funciones, más datos, más
lógica— un solo archivo se vuelve largo y difícil de leer, de mantener y de reutilizar
en otro programa. Piensa en una caja de herramientas: si todas las herramientas están
sueltas y mezcladas en un cajón, cuesta encontrar la que necesitas; si están agrupadas
por tipo (destornilladores, llaves, martillos), es mucho más fácil trabajar. Un
**módulo** en Python es esa agrupación: un archivo `.py` que reúne funciones y
variables relacionadas entre sí.

### 🧠 Concepto

Un **módulo** es, simplemente, un archivo `.py` que contiene código Python (funciones,
variables, y hasta clases más adelante en otros cursos) y que puede ser usado desde
otro archivo. **Modularizar** el código significa dividirlo en varios módulos, cada uno
responsable de una parte coherente del programa, en vez de escribirlo todo en un solo
archivo.

### 📖 Explicación

Modularizar el código trae tres beneficios concretos:

- **Organización**: cada archivo tiene un propósito claro (por ejemplo, un módulo para
  operaciones matemáticas, otro para el catálogo de una tienda), en vez de mezclar todo.
- **Mantenibilidad**: si hay que corregir o mejorar una función, se sabe exactamente en
  qué archivo buscarla.
- **Reusabilidad**: un módulo bien escrito se puede importar y reutilizar desde
  cualquier programa nuevo, sin copiar y pegar el código.

Cualquier archivo `.py` puede actuar como módulo de otro. Si tienes un archivo
`operaciones_basicas.py` con una función `sumar(a, b)`, y otro archivo `principal.py`
en la misma carpeta, `principal.py` puede usar esa función importando el módulo. No
hace falta ninguna configuración especial: basta con que ambos archivos estén en el
mismo directorio.

## 🌍 Crear e importar módulos propios

### 🌍 Contexto

Ya sabemos qué es un módulo y por qué conviene usarlo. Ahora falta la parte práctica:
¿cómo se crea un módulo propio y cómo se usa su contenido desde otro archivo? Python
ofrece varias formas de importar, y elegir la correcta hace que el código sea más claro.

### 🧠 Concepto

**Crear un módulo propio** es tan simple como escribir un archivo `.py` con funciones
(y/o variables) dentro. Para **usarlo** desde otro archivo existen varias formas de
`import`:

- `import modulo`: importa el módulo completo; para usar algo de él se escribe
  `modulo.funcion()`.
- `from modulo import nombre`: importa solo un elemento puntual del módulo; se usa
  directamente por su nombre, `nombre()`, sin prefijo.
- `import modulo as alias`: importa el módulo completo pero le da un nombre más corto
  o distinto (el **alias**) para referirse a él, `alias.funcion()`.
- `from modulo import nombre as alias`: importa un elemento puntual y le da un alias,
  `alias()`.

### 📖 Explicación

¿Cuándo conviene cada forma?

- `import modulo` es la opción más clara cuando se usan varias funciones del módulo:
  el prefijo `modulo.` deja claro de dónde viene cada una.
- `from modulo import nombre` es cómodo cuando solo se necesita una función puntual y
  se quiere escribir menos código, aunque puede generar confusión si dos módulos
  distintos definen una función con el mismo nombre.
- El **alias** (`as`) se usa para acortar un nombre de módulo largo, o para evitar que
  el nombre importado choque con otro identificador que ya existe en el programa.

Por ejemplo, si `matematicas.py` define `cuadrado(n)` y `cubo(n)`, se puede escribir
`import matematicas as mate` y luego llamar a `mate.cuadrado(5)`; o bien
`from matematicas import cuadrado as al_cuadrado` y llamar directamente a
`al_cuadrado(5)`. Ambas formas son válidas: la elección es una cuestión de claridad y
de evitar colisiones de nombres, no de que una sea "más correcta" que la otra.

## 🌍 Módulo `collections`

### 🌍 Contexto

Ya conocemos listas, tuplas, conjuntos y diccionarios. Python trae, además, el módulo
`collections`, con estructuras de datos especializadas que resuelven mejor ciertos
problemas comunes que una lista simple. Antes de ver cómo funciona la iteración "por
dentro", conviene conocer una de estas estructuras: la `deque`.

### 🧠 Concepto

`collections.deque` (se pronuncia "deck", de *double-ended queue*) es una colección
parecida a una lista, pero optimizada para agregar y quitar elementos por **ambos
extremos** de forma eficiente. `collections.Counter` es otra utilidad del mismo
módulo: cuenta cuántas veces aparece cada elemento de una colección.

### 📖 Explicación

Para crear una `deque` se usa `collections.deque([...])`, con una lista inicial de
elementos (o vacía). Se le pueden agregar elementos al final con `append()` o al
principio con `appendleft()`, y quitarlos con `pop()` (del final) o `popleft()` (del
principio) — algo que una lista también permite, pero de forma menos eficiente cuando
se hace repetidamente por el principio.

`collections.Counter` recibe una colección (por ejemplo, una lista) y devuelve un
objeto parecido a un diccionario donde cada clave es un elemento y su valor es cuántas
veces apareció. Por ejemplo, `Counter(["pan", "leche", "pan"])` indica que `"pan"`
aparece 2 veces y `"leche"` 1 vez.

Tanto una `deque` como el resultado de un `Counter` son **iterables**: se pueden
recorrer con `for`, igual que una lista. En la siguiente sección usaremos justamente la
`deque` para entender qué significa "ser iterable" por dentro.

## 🌍 Iterables e iteradores

### 🌍 Contexto

Ya usamos `for elemento in coleccion:` muchas veces, con listas, tuplas, diccionarios y
ahora con una `deque`. Pero ¿qué hace Python exactamente cuando ejecuta ese `for`?
Entender el mecanismo interno ayuda a saber por qué algunas cosas son iterables y
otras no, y a resolver problemas donde se necesita más control sobre el recorrido.

### 🧠 Concepto

Un **iterable** es cualquier objeto que se puede recorrer (una lista, una tupla, un
diccionario, una `deque`...). Un **iterador** es un objeto distinto, con estado propio,
que "recuerda" en qué posición del recorrido está y entrega el siguiente valor cada vez
que se le pide. `iter()` obtiene un iterador a partir de un iterable; `next()` le pide
el siguiente valor.

### 📖 Explicación

Retomemos la `deque` de la sección anterior. Si escribimos:

```python
cola = collections.deque(["a", "b", "c"])
iterador = iter(cola)
```

`iterador` es un objeto nuevo, distinto de `cola`, que sabe por dónde va. Cada llamada
a `next(iterador)` devuelve el siguiente elemento: primero `"a"`, luego `"b"`, luego
`"c"`. Cuando ya no quedan elementos, `next(iterador)` no devuelve un valor "vacío":
lanza la excepción `StopIteration`, que es la señal de que el iterador se agotó.

Cuando usamos `for elemento in cola:`, Python hace internamente exactamente esto: llama
a `iter(cola)` una vez, y luego a `next()` repetidamente, deteniéndose automáticamente
al recibir `StopIteration`. Por eso el `for` nunca "explota" al llegar al final: la
excepción la maneja el propio bucle, no nosotros. Usar `iter()`/`next()` manualmente
sirve para entender ese mecanismo y para los casos en que se necesita leer los
elementos "de a uno" bajo control explícito del programa.

## 🌍 Manejo de errores

### 🌍 Contexto

En la Clase 05 ya usamos `try`/`except` para manejar el caso de un archivo que no
existe (`FileNotFoundError`). Pero los errores en tiempo de ejecución no se limitan a
los archivos: convertir un texto a número que no lo es, buscar una clave que no existe
en un diccionario, o dividir entre cero, son errores comunes que también se pueden
anticipar.

### 🧠 Concepto

`try`/`except` permite **anticipar** que una parte del código puede fallar: el bloque
`try` contiene la operación riesgosa, y uno o más bloques `except` indican qué hacer si
ocurre un error de un tipo determinado, en vez de dejar que el programa se detenga con
una traza de error.

### 📖 Explicación

La forma general es:

```python
try:
    # operacion que puede fallar
    ...
except ValueError:
    # que hacer si el error fue de tipo ValueError
    ...
except KeyError:
    # que hacer si el error fue de tipo KeyError
    ...
```

Es importante capturar **tipos específicos** de excepción (`ValueError`, `KeyError`,
`ZeroDivisionError`, etc.), no una captura genérica sin tipo (`except:` a secas). Un
`except:` sin tipo atrapa *cualquier* error, incluso errores que no anticipamos ni
sabemos cómo manejar, lo que puede ocultar bugs reales del programa en vez de
resolverlos. Por ejemplo, `int("abc")` lanza `ValueError` porque "abc" no se puede
convertir a número; `diccionario["clave_inexistente"]` lanza `KeyError`; `10 / 0` lanza
`ZeroDivisionError`. Cada una se captura con su `except` correspondiente.

## 🌍 Los bloques `else` y `finally`

### 🌍 Contexto

Un `try`/`except` decide qué pasa si hay un error. Pero a veces también hace falta
código que solo debe correr si **no** hubo ningún error, y código que debe correr
**siempre**, haya habido error o no (por ejemplo, un mensaje de cierre o una limpieza).
Para eso existen `else` y `finally`.

### 🧠 Concepto

- El bloque `else` se ejecuta **solo si** el `try` terminó sin lanzar ninguna
  excepción.
- El bloque `finally` se ejecuta **siempre**, tanto si hubo una excepción manejada,
  como si no hubo ninguna.

### 📖 Explicación

```python
try:
    numero = int(entrada)
except ValueError:
    print("Eso no es un numero valido")
else:
    print("Convertido correctamente:", numero)
finally:
    print("Fin del intento de conversion")
```

Si `entrada` es `"5"`, la conversión tiene éxito: se ejecuta el `try`, luego el
`else` (porque no hubo error), y por último el `finally`. Si `entrada` es `"cinco"`,
la conversión falla: se ejecuta el `except` (en vez del `else`), y el `finally` se
ejecuta igual, porque `finally` no depende de si hubo error o no.

Una forma sencilla de recordarlo: `else` es "si todo salió bien", y `finally` es
"pase lo que pase". No hace falta usar los cuatro bloques siempre: `else` y `finally`
son opcionales y se agregan solo cuando el programa realmente necesita distinguir
esos dos momentos.

## 🌍 Aplicación práctica

### 🌍 Contexto

Ya vimos, por separado, cómo crear e importar un módulo propio, cómo usar
`collections` y el protocolo `iter()`/`next()`, y cómo manejar errores con
`try`/`except`/`else`/`finally`. Un programa real casi nunca usa uno solo de estos
temas de forma aislada: los combina. Un buen ejemplo cotidiano es un menú para comprar
en una tienda: hay un catálogo de productos (que conviene organizar en su propio
módulo), hay que mostrarlo (iterando sobre él), y hay que anticipar errores del
usuario (una cantidad mal escrita, un producto que no existe).

### 🧠 Concepto

**Integrar** los tres bloques significa usar cada uno donde corresponde dentro de un
mismo programa: el módulo organiza los datos y las funciones relacionadas con ellos;
la iteración recorre esos datos para mostrarlos; y el manejo de errores protege las
partes del programa donde el usuario puede equivocarse.

### 📖 Explicación

En el ejemplo integrador de esta clase, un módulo propio `catalogo.py` guarda el
catálogo de una tienda (un diccionario `producto -> precio`) junto con funciones para
mostrarlo y buscar un producto. El script principal importa ese módulo, muestra el
catálogo iterando sobre él, y pide al usuario un producto y una cantidad para
"comprar". Ahí es donde entra el manejo de errores: si la cantidad no es un número
válido, se captura `ValueError`; si el producto no está en el catálogo, se maneja esa
situación (por ejemplo, con `KeyError` o una validación equivalente) — en ambos casos,
con un mensaje claro en vez de que el programa se detenga. Cuando la compra es válida,
un bloque `else` calcula y muestra el total; un bloque `finally` muestra siempre un
mensaje de cierre, se haya completado la compra o no.

Esta combinación —módulo propio + iteración + manejo de errores— es exactamente el
patrón que vas a practicar en el taller guiado de esta clase.
