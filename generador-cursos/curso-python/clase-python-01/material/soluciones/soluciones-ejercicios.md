# Soluciones de los ejercicios — Clase 01

> **Material docente.** No entregar al estudiantado antes de la puesta en común. Todo el
> código se ejecuta sin errores con Python 3.10 o superior.

Cada solución incluye el código, una explicación breve y el resultado esperado ya
verificado ejecutando el programa.

---

## Básico 01 — Datos de una persona

### Parte A (respuesta esperada)

Se acepta cualquier respuesta que mencione **dos** ideas correctas, por ejemplo:

- El código es **legible**: `print(mensaje)` se entiende casi como una frase en español;
  no hay símbolos de más ni necesidad de declarar el tipo de `mensaje`.
- Python es **interpretado**: el programa se ejecuta línea por línea tal como está, sin
  un paso previo de compilación.

### Parte B — Código

```python
# Datos de la persona (fijos en el código)
nombre = "Camila"
edad = 25
ciudad = "Valparaíso"

# Salida: ficha con los datos
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)
```

### Explicación

- `nombre` y `ciudad` son de tipo `str`; `edad` es `int`.
- Cada `print` combina un texto fijo con el valor de una variable.

### Resultado esperado

```text
Nombre: Camila
Edad: 25
Ciudad: Valparaíso
```

---

## Básico 02 — Conversión de temperatura

### Código

```python
# Entrada
celsius = 25.0

# Proceso: primero * y /, luego + (precedencia)
fahrenheit = celsius * 9 / 5 + 32

# Salida
print(celsius, "°C equivalen a", fahrenheit, "°F")
print("¿Está bajo cero?:", celsius < 0)
```

### Explicación

- En `celsius * 9 / 5 + 32`, Python evalúa `celsius * 9` → `225.0`, luego `/ 5` → `45.0`
  y por último `+ 32` → `77.0`. No hacen falta paréntesis.
- `celsius < 0` es una expresión de comparación: produce directamente `False`, sin
  necesidad de un `if`.

### Resultado esperado

```text
25.0 °C equivalen a 77.0 °F
¿Está bajo cero?: False
```

---

## Intermedio 01 — ¿Mayor de edad?

### Código

```python
# Entrada
edad = 20
acepto_terminos = False

# Proceso y salida
if edad < 18:
    mensaje = "Debe ser mayor de edad"
elif edad >= 18 and acepto_terminos:
    mensaje = "Registro permitido"
else:
    mensaje = "Debe aceptar los términos"

print(mensaje)
```

### Explicación

- Se comprueba primero la edad. Si es menor de 18, no importa si aceptó: el mensaje es
  el de edad.
- El segundo caso combina dos condiciones con `and`: mayor de edad **y** términos
  aceptados.
- El `else` cubre el caso restante: mayor de edad pero sin aceptar.

### Resultado esperado

```text
Debe aceptar los términos
```

Otras pruebas: `edad = 16` → `Debe ser mayor de edad`; `edad = 25`,
`acepto_terminos = True` → `Registro permitido`.

---

## Intermedio 02 — Descuento por monto

### Código

```python
# Entrada
monto = 50000

# Proceso: porcentaje según el tramo
if monto < 20000:
    porcentaje_descuento = 0
elif monto < 50000:
    porcentaje_descuento = 10
else:
    porcentaje_descuento = 20

descuento = monto * porcentaje_descuento / 100
total_a_pagar = monto - descuento

# Salida
print("Descuento:", descuento)
print("Total a pagar:", total_a_pagar)
```

### Explicación

- El orden de los `elif` permite comprobar solo el límite superior de cada tramo.
- `monto * porcentaje_descuento / 100`: con `monto = 50000` y `porcentaje = 20`, da
  `50000 * 20` → `1000000`, luego `/ 100` → `10000.0`.

### Resultado esperado

```text
Descuento: 10000.0
Total a pagar: 40000.0
```

---

## Avanzado 01 — Suma de los primeros números

### Código

```python
# Entrada
n = 5

# Acumuladores
suma = 0
cantidad_pares = 0

# Se conoce el número de vueltas -> for
for numero in range(1, n + 1):
    suma = suma + numero
    if numero % 2 == 0:
        cantidad_pares = cantidad_pares + 1

# Salida
print("Suma:", suma)
print("Cantidad de pares:", cantidad_pares)
```

### Explicación

- `range(1, n + 1)` recorre `1, 2, 3, 4, 5`.
- `suma` acumula: `0 → 1 → 3 → 6 → 10 → 15`.
- El `if numero % 2 == 0` cuenta los pares: el 2 y el 4 → `cantidad_pares = 2`.
- Se usa `for` porque el número de repeticiones (`n`) se conoce de antemano.

### Resultado esperado

```text
Suma: 15
Cantidad de pares: 2
```

---

## Avanzado 02 — Adivina el número

### Código

```python
# Entrada
numero_secreto = 7
intento = 1
maximo_valor = 9

# Control
intentos_realizados = 0
adivinado = False

# No se sabe en qué vuelta se acierta -> while
while intento <= maximo_valor and not adivinado:
    intentos_realizados = intentos_realizados + 1

    if intento < numero_secreto:
        resultado = "muy bajo"
    elif intento > numero_secreto:
        resultado = "muy alto"
    else:
        resultado = "correcto"
        adivinado = True

    print("Intento", intentos_realizados, "(valor", str(intento) + "):", resultado)
    intento = intento + 2   # cambia el estado: evita el bucle infinito

# Salida final
if adivinado:
    print("Adivinado en", intentos_realizados, "intentos")
else:
    print("No se adivinó el número")
```

### Explicación

- La condición del `while` combina dos ideas con `and`: quedan valores por probar
  (`intento <= maximo_valor`) **y** todavía no se acertó (`not adivinado`).
- El `if` / `elif` / `else` decide el mensaje de cada intento y, al acertar, pone
  `adivinado = True` para que el bucle termine.
- `intento = intento + 2` garantiza que el bucle avanza y termina.
- Se usa `while` porque el final depende de una condición evaluada en cada vuelta.

### Resultado esperado

```text
Intento 1 (valor 1): muy bajo
Intento 2 (valor 3): muy bajo
Intento 3 (valor 5): muy bajo
Intento 4 (valor 7): correcto
Adivinado en 4 intentos
```

---

## Desafío 01 — Cajero de billetes

### Código

```python
# Entrada
monto = 47000

# Se recorre una colección de valores de billete, de mayor a menor
total_billetes = 0

for valor_billete in (20000, 10000, 5000, 2000, 1000):
    cantidad = monto // valor_billete      # cuántos billetes de este valor caben
    monto = monto % valor_billete          # dinero que queda por entregar

    if cantidad > 0:
        print("Billetes de", str(valor_billete) + ":", cantidad)

    total_billetes = total_billetes + cantidad

print("Total de billetes:", total_billetes)
```

### Explicación (análisis → algoritmo → programa)

- **Análisis**: entrada = `monto`; proceso = repartir en billetes de mayor a menor;
  salida = cantidad por billete y total.
- **Algoritmo**: para cada valor de billete, tomar `monto // valor` billetes y quedarse
  con `monto % valor` como resto para el siguiente.
- **Programa**: el bucle recorre los cinco valores en orden decreciente; empezar por el
  mayor asegura la **menor cantidad** de billetes.
- `str(valor_billete) + ":"` une el número con los dos puntos para que la salida quede
  `Billetes de 20000: 2` sin espacio antes de los dos puntos.

### Resultado esperado (los cuatro casos de prueba)

```text
# monto = 47000
Billetes de 20000: 2
Billetes de 5000: 1
Billetes de 2000: 1
Total de billetes: 4

# monto = 1000
Billetes de 1000: 1
Total de billetes: 1

# monto = 0
Total de billetes: 0

# monto = 38000
Billetes de 20000: 1
Billetes de 10000: 1
Billetes de 5000: 1
Billetes de 2000: 1
Billetes de 1000: 1
Total de billetes: 5
```

---

## Taller 01 — Calculadora de propina

### Código (`propina.py`)

```python
# Entrada
monto_cuenta = 30000
calificacion_servicio = 5
numero_personas = 3

# Decisión: porcentaje de propina según la calificación
if calificacion_servicio >= 4:
    porcentaje_propina = 20
elif calificacion_servicio >= 2:
    porcentaje_propina = 10
else:
    porcentaje_propina = 0

# Cálculos
propina = monto_cuenta * porcentaje_propina / 100
total = monto_cuenta + propina
parte = total / numero_personas

# Salida
print("Porcentaje de propina:", porcentaje_propina)
print("Propina:", propina)
print("Total:", total)

# Repetición: la parte de cada persona
for persona in range(1, numero_personas + 1):
    print("Persona", persona, "paga:", parte)
```

### Explicación

- **`if` / `elif` / `else`**: hay tres tramos de calificación → una decisión con tres
  caminos.
- **`for`**: se conoce el número de vueltas (`numero_personas`) → bucle `for` con
  `range`.
- El bucle recorre exactamente `numero_personas` vueltas y termina; no hay riesgo de
  repetición infinita.

### Resultado esperado (los tres casos de prueba)

```text
# 30000, calificación 5, 3 personas
Porcentaje de propina: 20
Propina: 6000.0
Total: 36000.0
Persona 1 paga: 12000.0
Persona 2 paga: 12000.0
Persona 3 paga: 12000.0

# 20000, calificación 3, 2 personas
Porcentaje de propina: 10
Propina: 2000.0
Total: 22000.0
Persona 1 paga: 11000.0
Persona 2 paga: 11000.0

# 15000, calificación 1, 1 persona
Porcentaje de propina: 0
Propina: 0.0
Total: 15000.0
Persona 1 paga: 15000.0
```
