# 💡 Ejemplo 04 — Agregar contenido sin perder lo anterior

**Tema**: modo `'a'` para agregar al final de un archivo · **Resultado de aprendizaje**:
RA-4 · **Nivel**: introductorio

## 🧩 Problema

Un archivo de historial guarda un registro por línea. Se necesita agregar un nuevo
registro cada vez que ocurre un evento, sin borrar los registros anteriores.

## 🔍 Análisis

- **Entrada**: un registro inicial y dos registros nuevos, fijos en el código.
- **Proceso**: crear el historial con el primer registro en modo `'w'`; agregar los dos
  registros siguientes en modo `'a'`.
- **Salida**: el contenido final del historial, con los tres registros en orden.

## 💡 Solución

1. Crear `historial.txt` con el primer registro, usando modo `'w'` (porque es la
   primera vez que se escribe).
2. Agregar el segundo y el tercer registro, cada uno con modo `'a'`.
3. Leer y mostrar el contenido final.

## 💻 Código

```python
# Primer registro: se crea el archivo
with open("historial.txt", "w") as archivo:
    archivo.write("08:00 - Apertura de la tienda\n")

# Segundo registro: se agrega sin borrar el anterior
with open("historial.txt", "a") as archivo:
    archivo.write("10:30 - Primera venta del día\n")

# Tercer registro: se agrega sin borrar los anteriores
with open("historial.txt", "a") as archivo:
    archivo.write("18:00 - Cierre de caja\n")

with open("historial.txt", "r") as archivo:
    print(archivo.read())
```

## 🧭 Explicación paso a paso

1. La primera escritura usa `'w'` porque `historial.txt` todavía no existe; lo crea con
   un solo registro.
2. Cada escritura siguiente usa `'a'`: como el archivo ya existe, `'a'` **no** lo
   sobrescribe, sino que agrega el nuevo texto después del contenido que ya había.
3. Al leer el archivo al final, los tres registros aparecen en el orden en que se
   escribieron, uno tras otro.

## ✅ Resultado esperado

```text
08:00 - Apertura de la tienda
10:30 - Primera venta del día
18:00 - Cierre de caja

```

**Archivo `historial.txt` resultante**:

```text
08:00 - Apertura de la tienda
10:30 - Primera venta del día
18:00 - Cierre de caja
```
