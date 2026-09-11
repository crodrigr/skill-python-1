# 💡 Ejemplo 03 — Recorrer y transformar una lista

**Tema**: recorrido con `for`, `in`, construcción de una lista derivada · **Resultado de
aprendizaje**: RA-4 · **Nivel**: introductorio

## 🧩 Problema

Un profesor tiene las calificaciones de un curso en una lista. Quiere: mostrar cada
calificación junto con su posición en la lista, comprobar si alguien sacó exactamente
un `10`, y construir una lista nueva solo con las calificaciones aprobatorias (mayores o
iguales a `6.0`), sin modificar la lista original.

## 🔍 Análisis

- **Entrada**: lista de calificaciones (`float`).
- **Proceso**: recorrer por índice para numerar; comprobar pertenencia con `in`;
  recorrer y filtrar para construir una lista nueva.
- **Salida**: cada calificación numerada, si hay un `10`, y la lista de aprobados.

## 💡 Solución

1. Recorrer con `for indice in range(len(...))` para mostrar posición y valor.
2. Usar `in` para comprobar si `10.0` está en la lista.
3. Recorrer con `for nota in calificaciones` y usar `if` + `append` para construir la
   lista de aprobados.

## 💻 Código

```python
# Calificaciones del curso
calificaciones = [5.5, 6.8, 4.2, 10.0, 7.5, 3.9]

# Recorrido por índice: mostrar posición y valor
for indice in range(len(calificaciones)):
    print("Posición", indice, "->", calificaciones[indice])

# Comprobar pertenencia
if 10.0 in calificaciones:
    print("Alguien sacó un 10")

# Construir una lista nueva con las calificaciones aprobatorias
aprobadas = []
for nota in calificaciones:
    if nota >= 6.0:
        aprobadas.append(nota)

print("Calificaciones originales:", calificaciones)
print("Calificaciones aprobatorias:", aprobadas)
```

## 🧭 Explicación paso a paso

1. `range(len(calificaciones))` genera los índices `0` a `5`; en cada vuelta,
   `calificaciones[indice]` da el valor en esa posición, útil cuando además del valor
   se necesita "en qué lugar está".
2. `10.0 in calificaciones` recorre la lista por dentro y devuelve `True` o `False` sin
   que el programa tenga que escribir el bucle a mano.
3. `aprobadas = []` crea una lista vacía que se irá llenando.
4. El segundo `for` recorre `calificaciones` **por valor** (no por índice, porque aquí
   no hace falta la posición); cada vez que `nota >= 6.0`, ese valor se agrega a
   `aprobadas` con `append`.
5. Al terminar, `calificaciones` sigue teniendo sus seis valores originales;
   `aprobadas` es una lista **distinta** con solo los valores que cumplieron la
   condición.

## ✅ Resultado esperado

```text
Posición 0 -> 5.5
Posición 1 -> 6.8
Posición 2 -> 4.2
Posición 3 -> 10.0
Posición 4 -> 7.5
Posición 5 -> 3.9
Alguien sacó un 10
Calificaciones originales: [5.5, 6.8, 4.2, 10.0, 7.5, 3.9]
Calificaciones aprobatorias: [6.8, 10.0, 7.5]
```
