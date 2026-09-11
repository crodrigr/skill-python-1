# Desafío 01 — Puntaje de una partida

## Problema

Un videojuego calcula el **puntaje final** de una partida así:

- `100` puntos por cada nivel alcanzado;
- `50` puntos de bono por cada vida que sobra;
- se **restan** `25` puntos por cada error cometido.

Con el puntaje final se asigna una **categoría**:

- `"Oro"` si el puntaje es `1000` o más;
- `"Plata"` si es `500` o más (pero menos de `1000`);
- `"Bronce"` en cualquier otro caso.

Escribe un programa que, dado el nombre de la persona, su nivel, sus vidas restantes y
sus errores, muestre un reporte con el nombre, el puntaje final y la categoría.

Resuélvelo en cuatro pasos: **analizar**, **descomponer en funciones**, **escribir el
programa** y **probarlo** con los casos de prueba.

## Entrada

- `nombre` (`str`).
- `nivel` (`int`, ≥ 0).
- `vidas` (`int`, ≥ 0).
- `errores` (`int`, ≥ 0).

Los valores van fijos en el código.

## Proceso esperado

1. **Analizar**: entrada, pasos intermedios y salida.
2. **Descomponer**: define una función por tarea. Se sugiere:
   - `puntos_por_nivel(nivel)` → `nivel * 100`
   - `bono_por_vidas(vidas)` → `vidas * 50`
   - `penalizacion(errores)` → `errores * 25`
   - `puntaje_final(nivel, vidas, errores)` → combina las tres anteriores
   - `categoria(puntaje)` → devuelve `"Oro"` / `"Plata"` / `"Bronce"`
   - `mostrar_reporte(nombre, nivel, vidas, errores)` → imprime el reporte
3. **Escribir** el programa: cada función con su `return`; `puntaje_final` y
   `mostrar_reporte` **llaman** a las demás, sin repetir cálculos.
4. **Probar** con la tabla de casos.

## Salida

Para `mostrar_reporte("Ana", 8, 3, 4)`:

```text
Jugador: Ana
Puntaje: 850
Categoría: Plata
```

## Restricciones

- Al menos **cuatro** funciones, y `puntaje_final` debe combinar los resultados de otras.
- Ninguna fórmula (`* 100`, `* 50`, `* 25`) debe aparecer más de una vez.
- Cada función tiene una sola responsabilidad y un nombre con verbo o predicado claro.
- Identificadores y comentarios en español.

## Casos de prueba

| `nivel` | `vidas` | `errores` | Puntaje | Categoría |
|---------|---------|-----------|---------|-----------|
| `8` | `3` | `4` | `850` | `Plata` |
| `12` | `5` | `2` | `1400` | `Oro` |
| `2` | `0` | `6` | `50` | `Bronce` |
| `10` | `0` | `0` | `1000` | `Oro` |

## Resultados de aprendizaje

- RA-6: refactorizar / evitar repetición usando funciones.
- RA-7: descomponer un problema en varias funciones y combinarlas.
- RA-4: devolver valores con `return` y usarlos entre funciones.
