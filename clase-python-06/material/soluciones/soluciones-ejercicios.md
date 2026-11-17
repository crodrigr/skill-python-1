# 🔑 Soluciones — Ejercicios y Taller (Clase 06)

Material docente. No compartir con el estudiante.

## 🟢 Básico 01 — Módulo de conversión de unidades

### 💻 Código

Archivo `conversor.py`:

```python
"""Modulo para convertir distancias entre metros y centimetros."""


def metros_a_centimetros(metros):
    """Convierte una distancia de metros a centimetros."""
    return metros * 100


def centimetros_a_metros(centimetros):
    """Convierte una distancia de centimetros a metros."""
    return centimetros / 100
```

Archivo `principal.py`:

```python
import conversor

en_centimetros = conversor.metros_a_centimetros(2.5)
en_metros = conversor.centimetros_a_metros(350)

print(f"2.5 metros = {en_centimetros} centimetros")
print(f"350 centimetros = {en_metros} metros")
```

### 📖 Explicación

Cada función de conversión aplica la fórmula correspondiente (multiplicar por 100 o
dividir entre 100) y ambas viven en `conversor.py`, separadas del script principal,
que solo las importa y las usa.

### ✅ Resultado esperado

```text
2.5 metros = 250.0 centimetros
350 centimetros = 3.5 metros
```

### 🧪 Verificación

Ejecutado con `python3 principal.py` colocando ambos archivos en el mismo directorio;
salida idéntica a la documentada.

---

## 🟢 Básico 02 — Recorrer una `deque` con `iter()`/`next()`

### 💻 Código

```python
import collections

estaciones = collections.deque(["primavera", "verano", "otoño", "invierno"])
iterador = iter(estaciones)

print(f"Estacion 1: {next(iterador)}")
print(f"Estacion 2: {next(iterador)}")
print(f"Estacion 3: {next(iterador)}")
print(f"Estacion 4: {next(iterador)}")

try:
    print(f"Estacion 5: {next(iterador)}")
except StopIteration:
    print("Ya no quedan mas estaciones")
```

### 📖 Explicación

Se obtiene el iterador una sola vez con `iter()`, y se avanza con cuatro llamadas a
`next()`. La quinta llamada se protege con `try`/`except StopIteration`, porque la
`deque` ya se agotó.

### ✅ Resultado esperado

```text
Estacion 1: primavera
Estacion 2: verano
Estacion 3: otoño
Estacion 4: invierno
Ya no quedan mas estaciones
```

### 🧪 Verificación

Ejecutado con `python3`; salida idéntica a la documentada.

---

## 🟡 Intermedio 01 — Contar votos con `Counter`

### 💻 Código

```python
import collections

votos = ["azul", "rojo", "azul", "verde", "rojo", "azul"]

conteo = collections.Counter(votos)
print("Conteo de votos:", conteo)

color_ganador, cantidad_ganadora = conteo.most_common(1)[0]
print(f"El color mas votado es {color_ganador} con {cantidad_ganadora} votos")
```

### 📖 Explicación

`collections.Counter(votos)` cuenta automáticamente cuántas veces aparece cada color.
`most_common(1)` devuelve una lista con el elemento más frecuente y su conteo, como
una tupla `(color, cantidad)`, que se desempaqueta directamente.

### ✅ Resultado esperado

```text
Conteo de votos: Counter({'azul': 3, 'rojo': 2, 'verde': 1})
El color mas votado es azul con 3 votos
```

### 🧪 Verificación

Ejecutado con `python3`; salida idéntica a la documentada.

---

## 🟡 Intermedio 02 — Convertir con `try`/`except`/`else`

### 💻 Código

```python
def calcular_con_descuento(precio_texto):
    print(f"Precio ingresado: {precio_texto}")
    try:
        precio = float(precio_texto)
    except ValueError:
        print(f"'{precio_texto}' no es un precio valido")
    else:
        precio_con_descuento = precio * 0.9
        print(f"Precio con 10% de descuento: {precio_con_descuento}")


calcular_con_descuento("120.0")
print()
calcular_con_descuento("gratis")
```

### 📖 Explicación

El cálculo del descuento vive en el `else`, por lo que solo se ejecuta cuando la
conversión a `float` tuvo éxito; si falla, se captura `ValueError` y no se intenta
ningún cálculo.

### ✅ Resultado esperado

```text
Precio ingresado: 120.0
Precio con 10% de descuento: 108.0

Precio ingresado: gratis
'gratis' no es un precio valido
```

### 🧪 Verificación

Ejecutado con `python3` para ambos casos de prueba; salida idéntica a la documentada.

---

## 🔴 Avanzado 01 — Dos tipos de error con `try`/`except`/`finally`

### 💻 Código

```python
def repartir_puntos(puntos, participantes_texto):
    print(f"\nRepartiendo {puntos} puntos entre '{participantes_texto}' participantes")
    try:
        participantes = int(participantes_texto)
        puntos_por_persona = puntos / participantes
    except ValueError:
        print(f"'{participantes_texto}' no es un numero valido de participantes")
    except ZeroDivisionError:
        print("No se puede repartir entre 0 participantes")
    else:
        print(f"Cada participante recibe {puntos_por_persona} puntos")
    finally:
        print("Fin del reparto")


repartir_puntos(100, "5")
repartir_puntos(100, "cero_participantes")
repartir_puntos(100, "0")
```

### 📖 Explicación

`ValueError` se lanza si el texto no se puede convertir a entero; `ZeroDivisionError`
se lanza si la división por `participantes` es entre cero. Cada una se captura con su
propio `except`. El `finally` se ejecuta en los tres casos.

### ✅ Resultado esperado

```text
Repartiendo 100 puntos entre '5' participantes
Cada participante recibe 20.0 puntos
Fin del reparto

Repartiendo 100 puntos entre 'cero_participantes' participantes
'cero_participantes' no es un numero valido de participantes
Fin del reparto

Repartiendo 100 puntos entre '0' participantes
No se puede repartir entre 0 participantes
Fin del reparto
```

### 🧪 Verificación

Ejecutado con `python3` para los tres casos de prueba; salida idéntica a la
documentada.

---

## 🔴 Avanzado 02 — Extender un módulo propio con manejo de errores

### 💻 Código

Archivo `matematicas.py` (ampliado con `raiz_cuadrada`):

```python
"""Modulo con operaciones matematicas."""
import math


def cuadrado(numero):
    """Devuelve el cuadrado de numero."""
    return numero ** 2


def cubo(numero):
    """Devuelve el cubo de numero."""
    return numero ** 3


def raiz_cuadrada(numero):
    """Devuelve la raiz cuadrada de numero (requiere numero >= 0)."""
    return math.sqrt(numero)
```

Archivo `principal.py`:

```python
import matematicas


def calcular_raiz(numero):
    try:
        resultado = matematicas.raiz_cuadrada(numero)
    except ValueError:
        print(f"No se puede calcular la raiz cuadrada de {numero} (numero negativo)")
    else:
        print(f"La raiz cuadrada de {numero} es {resultado}")


calcular_raiz(16)
calcular_raiz(-4)
```

### 📖 Explicación

`math.sqrt(numero)` lanza `ValueError` ("math domain error") cuando `numero` es
negativo. El script principal captura ese error específico y muestra un mensaje
comprensible; para un número válido, muestra el resultado en el `else`.

### ✅ Resultado esperado

```text
La raiz cuadrada de 16 es 4.0
No se puede calcular la raiz cuadrada de -4 (numero negativo)
```

### 🧪 Verificación

Ejecutado con `python3` colocando `matematicas.py` y `principal.py` en el mismo
directorio; salida idéntica a la documentada.

---

## 🏆 Desafío 01 — Reservas de boletos de cine

### 💻 Código

Archivo `cartelera.py`:

```python
"""Modulo con la cartelera de un cine: precio y cupos por pelicula."""

PRECIOS = {
    "accion": 5000,
    "comedia": 4500,
    "drama": 4000,
}

CUPOS = {
    "accion": 3,
    "comedia": 0,
    "drama": 5,
}


def mostrar_cartelera():
    """Muestra cada pelicula con su precio y cupos disponibles."""
    print("Cartelera disponible:")
    for pelicula in PRECIOS:
        print(f"- {pelicula}: ${PRECIOS[pelicula]} ({CUPOS[pelicula]} cupos)")


def buscar_precio(pelicula):
    """Devuelve el precio de la pelicula o lanza KeyError si no existe."""
    return PRECIOS[pelicula]


def cupos_disponibles(pelicula):
    """Devuelve los cupos disponibles de la pelicula."""
    return CUPOS[pelicula]
```

Archivo `principal.py`:

```python
import cartelera


def reservar(pelicula, cantidad_texto):
    print(f"\nIntentando reservar: {cantidad_texto} de '{pelicula}'")
    try:
        cantidad = int(cantidad_texto)
        precio_unitario = cartelera.buscar_precio(pelicula)
    except ValueError:
        print(f"'{cantidad_texto}' no es una cantidad valida")
    except KeyError:
        print(f"La pelicula '{pelicula}' no esta en la cartelera")
    else:
        if cantidad > cartelera.cupos_disponibles(pelicula):
            print(f"No hay cupos suficientes para '{pelicula}'")
        else:
            total = cantidad * precio_unitario
            print(f"Reserva realizada: {cantidad} entradas de {pelicula} = ${total}")
    finally:
        print("Fin del intento de reserva")


cartelera.mostrar_cartelera()

reservar("accion", "2")
reservar("accion", "diez")
reservar("terror", "1")
reservar("comedia", "1")
```

### 📖 Explicación

El módulo `cartelera.py` guarda precio y cupos por película. `reservar()` maneja
`ValueError` (cantidad no numérica) y `KeyError` (película inexistente) por separado;
dentro del `else` (sin errores de conversión ni de búsqueda), una condición adicional
verifica si hay cupos suficientes antes de confirmar la reserva. El `finally` cierra
siempre el intento.

### ✅ Resultado esperado

```text
Cartelera disponible:
- accion: $5000 (3 cupos)
- comedia: $4500 (0 cupos)
- drama: $4000 (5 cupos)

Intentando reservar: 2 de 'accion'
Reserva realizada: 2 entradas de accion = $10000
Fin del intento de reserva

Intentando reservar: diez de 'accion'
'diez' no es una cantidad valida
Fin del intento de reserva

Intentando reservar: 1 de 'terror'
La pelicula 'terror' no esta en la cartelera
Fin del intento de reserva

Intentando reservar: 1 de 'comedia'
No hay cupos suficientes para 'comedia'
Fin del intento de reserva
```

### 🧪 Verificación

Ejecutado con `python3` colocando `cartelera.py` y `principal.py` en el mismo
directorio, cubriendo los cuatro casos de prueba del enunciado; salida idéntica a la
documentada.

---

## 🛠️ Taller 01 — Menú para comprar

### 💻 Código

Archivo `catalogo.py`:

```python
"""Modulo con el catalogo de productos de la tienda."""

PRODUCTOS = {
    "manzana": 800,
    "pan": 1500,
    "leche": 1200,
}


def mostrar_catalogo():
    """Muestra el catalogo completo, un producto por linea."""
    print("Catalogo disponible:")
    for producto in PRODUCTOS:
        print(f"- {producto}: ${PRODUCTOS[producto]}")


def buscar_precio(producto):
    """Devuelve el precio de producto o lanza KeyError si no existe."""
    return PRODUCTOS[producto]
```

Archivo `principal.py`:

```python
import catalogo


def comprar(producto, cantidad_texto):
    print(f"\nIntentando comprar: {cantidad_texto} de '{producto}'")
    try:
        cantidad = int(cantidad_texto)
        precio_unitario = catalogo.buscar_precio(producto)
    except ValueError:
        print(f"'{cantidad_texto}' no es una cantidad valida")
    except KeyError:
        print(f"El producto '{producto}' no esta en el catalogo")
    else:
        total = cantidad * precio_unitario
        print(f"Compra realizada: {cantidad} x {producto} = ${total}")
    finally:
        print("Fin del intento de compra")


catalogo.mostrar_catalogo()

comprar("pan", "2")
comprar("pan", "dos")
comprar("queso", "1")
```

### 📖 Explicación

Esta es la solución de referencia del taller: coincide en estructura con el Ejemplo 06
(mismo patrón módulo + iteración + `try`/`except`/`else`/`finally`), aplicado a los
tres casos de prueba del taller (compra válida, cantidad inválida, producto
inexistente).

### ✅ Resultado esperado

```text
Catalogo disponible:
- manzana: $800
- pan: $1500
- leche: $1200

Intentando comprar: 2 de 'pan'
Compra realizada: 2 x pan = $3000
Fin del intento de compra

Intentando comprar: dos de 'pan'
'dos' no es una cantidad valida
Fin del intento de compra

Intentando comprar: 1 de 'queso'
El producto 'queso' no esta en el catalogo
Fin del intento de compra
```

### 🧪 Verificación

Ejecutado con `python3` colocando `catalogo.py` y `principal.py` en el mismo
directorio, cubriendo los tres casos de prueba del taller; salida idéntica a la
documentada.
