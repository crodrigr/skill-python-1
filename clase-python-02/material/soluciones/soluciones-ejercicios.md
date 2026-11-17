# 🔑 Soluciones de los ejercicios — Clase 02: Funciones

> **Material docente.** No entregar al estudiantado antes de la puesta en común. Todo el
> código se ejecuta sin errores con Python 3.10 o superior y su salida coincide con el
> "Resultado esperado" ya verificado.

Cada solución incluye el código, una explicación breve y el resultado esperado.

---

## 🟢 Básico 01 — Definir y llamar una función

### 💻 Código

```python
def mostrar_menu():
    """Muestra el menú del cajero."""
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Salir")

mostrar_menu()
print("-----")
mostrar_menu()
```

### 📖 Explicación

- `mostrar_menu` no tiene parámetros ni `return`: solo produce un efecto (imprimir).
- El texto del menú se escribe una sola vez y las dos llamadas lo reutilizan.

### ✅ Resultado esperado

```text
1. Ver saldo
2. Depositar
3. Salir
-----
1. Ver saldo
2. Depositar
3. Salir
```

---

## 🟢 Básico 02 — Función con parámetro y retorno

### 💻 Código

```python
def doble(numero):
    """Devuelve el doble del número recibido."""
    return numero * 2

print(doble(4))
print(doble(25))
```

### 📖 Explicación

- `numero` es un parámetro; `4` y `25` son los argumentos.
- La función **devuelve** el resultado; es el programa principal quien lo imprime.

### ✅ Resultado esperado

```text
8
50
```

---

## 🟡 Intermedio 01 — Función con decisión

### 💻 Código

```python
def es_aprobado(nota, minimo):
    """Devuelve 'Aprobado' o 'Reprobado' según la nota y el mínimo."""
    if nota >= minimo:
        return "Aprobado"
    return "Reprobado"

print(es_aprobado(65, 60))
print(es_aprobado(40, 60))
```

### 📖 Explicación

- Si `nota >= minimo`, el primer `return` termina la función y devuelve `"Aprobado"`.
- Si no, la ejecución llega al segundo `return` y devuelve `"Reprobado"` (no hace falta
  `else`).

### ✅ Resultado esperado

```text
Aprobado
Reprobado
```

---

## 🟡 Intermedio 02 — Función con varias condiciones

### 💻 Código

```python
def clasificar_imc(peso, altura):
    """Devuelve la categoría de IMC ('bajo', 'normal' o 'alto')."""
    imc = peso / (altura * altura)
    if imc < 18.5:
        return "bajo"
    elif imc < 25:
        return "normal"
    else:
        return "alto"

print(clasificar_imc(50, 1.70))
print(clasificar_imc(80, 1.75))
```

### 📖 Explicación

- El IMC se calcula en una variable local y solo se usa para decidir la categoría.
- `50 / (1.70 * 1.70) ≈ 17.30` → `"bajo"`; `80 / (1.75 * 1.75) ≈ 26.12` → `"alto"`.

### ✅ Resultado esperado

```text
bajo
alto
```

---

## 🔴 Avanzado 01 — Refactorizar con funciones

### 💻 Código (versión refactorizada)

```python
def total_con_iva(neto):
    """Devuelve el total sumando el 19 % de IVA al monto neto."""
    return neto + neto * 19 // 100

def mostrar_boleta(nombre, neto):
    """Muestra la boleta de un cliente con su total."""
    print("Cliente:", nombre)
    print("Total:", total_con_iva(neto))

mostrar_boleta("Ana", 1000 + 2000 + 500)
mostrar_boleta("Luis", 3000 + 1500)
mostrar_boleta("Eva", 800 + 800 + 800 + 800)
```

### 📖 Explicación

- El cálculo del IVA, repetido 3 veces en el código de partida, queda en
  `total_con_iva`.
- La estructura "Cliente / Total" queda en `mostrar_boleta`, que **llama** a
  `total_con_iva`.
- La salida es idéntica a la del código de partida: refactorizar no cambia el
  comportamiento.

### 🔎 Verificación (código de partida vs refactorizado)

Ambas versiones imprimen:

```text
Cliente: Ana
Total: 4165
Cliente: Luis
Total: 5355
Cliente: Eva
Total: 3808
```

(`neto` de Ana = 3500; `3500 * 19 // 100 = 665`; total = 4165. Luis: 4500 → 855 → 5355.
Eva: 3200 → 608 → 3808.)

---

## 🔴 Avanzado 02 — Combinar funciones y un bucle

### 💻 Código

```python
def factorial(n):
    """Devuelve n! calculado con un bucle."""
    resultado = 1
    for i in range(2, n + 1):
        resultado = resultado * i
    return resultado

def mostrar_factoriales(desde, hasta):
    """Muestra el factorial de cada entero entre 'desde' y 'hasta'."""
    for numero in range(desde, hasta + 1):
        print(numero, "->", factorial(numero))

mostrar_factoriales(1, 5)
```

### 📖 Explicación

- `factorial(1)`: `range(2, 2)` está vacío, el bucle no se ejecuta y devuelve `1`.
- `mostrar_factoriales` no calcula nada: en cada vuelta **llama** a `factorial`.

### ✅ Resultado esperado

```text
1 -> 1
2 -> 2
3 -> 6
4 -> 24
5 -> 120
```

---

## 🏆 Desafío 01 — Puntaje de una partida

### 💻 Código

```python
def puntos_por_nivel(nivel):
    """Devuelve los puntos ganados por alcanzar un nivel."""
    return nivel * 100

def bono_por_vidas(vidas):
    """Devuelve el bono por las vidas que quedan."""
    return vidas * 50

def penalizacion(errores):
    """Devuelve los puntos que se restan por errores."""
    return errores * 25

def puntaje_final(nivel, vidas, errores):
    """Combina puntos, bono y penalización en el puntaje final."""
    return puntos_por_nivel(nivel) + bono_por_vidas(vidas) - penalizacion(errores)

def categoria(puntaje):
    """Devuelve la categoría del puntaje ('Oro', 'Plata' o 'Bronce')."""
    if puntaje >= 1000:
        return "Oro"
    elif puntaje >= 500:
        return "Plata"
    else:
        return "Bronce"

def mostrar_reporte(nombre, nivel, vidas, errores):
    """Muestra el reporte final de una partida."""
    puntaje = puntaje_final(nivel, vidas, errores)
    print("Jugador:", nombre)
    print("Puntaje:", puntaje)
    print("Categoría:", categoria(puntaje))

mostrar_reporte("Ana", 8, 3, 4)
```

### 📖 Explicación

- Cada fórmula (`* 100`, `* 50`, `* 25`) aparece **una sola vez**, en su función.
- `puntaje_final` combina los resultados de tres funciones; `mostrar_reporte` combina
  `puntaje_final` y `categoria`.

### ✅ Resultado esperado

```text
Jugador: Ana
Puntaje: 850
Categoría: Plata
```

### 🔎 Verificación con los casos de prueba

| `nivel` | `vidas` | `errores` | `puntaje_final` | `categoria` |
|---------|---------|-----------|-----------------|-------------|
| 8 | 3 | 4 | 800 + 150 − 100 = **850** | Plata |
| 12 | 5 | 2 | 1200 + 250 − 50 = **1400** | Oro |
| 2 | 0 | 6 | 200 + 0 − 150 = **50** | Bronce |
| 10 | 0 | 0 | 1000 + 0 − 0 = **1000** | Oro |

---

## 🛠️ Taller 01 — Calculadora de cuenta con propina y división por comensales

### 💻 Código

```python
def calcular_propina(monto, porcentaje):
    """Devuelve el monto de la propina para un porcentaje dado."""
    return monto * porcentaje / 100

def calcular_total(monto, propina):
    """Devuelve el total de la cuenta con propina incluida."""
    return monto + propina

def dividir_entre(total, comensales):
    """Devuelve cuánto paga cada comensal."""
    return total / comensales

def formatear_pesos(valor):
    """Devuelve el valor como texto con el signo $ y dos decimales."""
    return f"${valor:.2f}"

def main():
    monto = 100.00
    porcentaje = 10
    comensales = 4

    propina = calcular_propina(monto, porcentaje)
    total = calcular_total(monto, propina)
    por_persona = dividir_entre(total, comensales)

    print("Propina:", formatear_pesos(propina))
    print("Total:", formatear_pesos(total))
    print("Cada persona paga:", formatear_pesos(por_persona))

main()
```

### 📖 Explicación

- Cuatro funciones de una sola responsabilidad; `main()` solo coordina llamadas.
- `formatear_pesos` es la refactorización del formato `f"${valor:.2f}"`, que aparecía
  tres veces.
- Los datos entran por parámetros y salen por `return`; no hay variables globales
  compartidas entre funciones.

### ✅ Resultado esperado (caso `100.00`, `10`, `4`)

```text
Propina: $10.00
Total: $110.00
Cada persona paga: $27.50
```

### 🔎 Verificación con los casos de prueba

| `monto` | `porcentaje` | `comensales` | Propina | Total | Por persona |
|---------|--------------|--------------|---------|-------|-------------|
| 100.00 | 10 | 4 | $10.00 | $110.00 | $27.50 |
| 80.00 | 15 | 2 | $12.00 | $92.00 | $46.00 |
| 60.00 | 0 | 3 | $0.00 | $60.00 | $20.00 |
