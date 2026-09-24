# 📘 Proyecto final 02 — Sistema de Inventario y Ventas de una Tienda de Barrio

**Proyecto final autónomo** · Duración estimada: 12 horas · Dificultad: 🏆 Desafío

## 🎯 Objetivo

Diseñar y construir, **de forma autónoma y desde cero**, una aplicación de consola en
Python que gestione el inventario y las ventas de una tienda de barrio, integrando
todos los temas de las Clases 01 a 06 (variables y tipos, funciones, listas, tuplas,
conjuntos, diccionarios, archivos de texto, módulos propios y manejo de excepciones),
resolviendo todo con esas estructuras de datos.

A diferencia del **Proyecto final 01** (donde se transcribía una guía con el código
ya resuelto), aquí solo se entrega el problema y los requisitos que la solución debe
cumplir. El estudiante decide los nombres de las funciones, cómo organizar los
módulos y qué formato usar para guardar los datos, siempre respetando los requisitos
de abajo.

## 🌍 Contexto y problema

La dueña de una tienda de barrio quiere dejar de anotar en un cuaderno el inventario
y las ventas del día. Pide una aplicación de consola, el **Gestor de Inventario y
Ventas**, que le permita:

- Mantener un catálogo de productos (con su precio, categoría y stock disponible).
- Registrar una venta que puede incluir **varios productos a la vez**, descontando el
  stock correspondiente y calculando el total a cobrar.
- Consultar reportes simples para tomar decisiones: qué se vende más, cuánto se
  facturó y qué productos hay que reponer.
- Que ningún dato se pierda al cerrar el programa: catálogo y ventas deben seguir
  disponibles la próxima vez que lo abra.

## ✅ Prerrequisitos

Haber completado el **Proyecto final 01** (o dominar sus mismos temas: Clases 01 a
06) y tener [Visual Studio Code](https://code.visualstudio.com/) con Python
instalado. Este proyecto asume que el estudiante ya sabe escribir un menú en bucle,
crear módulos propios y guardar/cargar datos en un archivo de texto sin ayuda paso a
paso.

## 📊 Qué lo hace más difícil que el Proyecto final 01

- Dos entidades relacionadas entre sí (producto y venta), no una sola.
- Una venta agrupa **varios ítems** (cada uno con su propio producto y cantidad), no
  un único registro plano.
- Reglas de integridad: no se puede vender más stock del disponible, ni eliminar un
  producto que ya tiene ventas asociadas.
- Reportes que exigen agrupar y contar datos a mano, combinando listas, tuplas,
  conjuntos y diccionarios (por ejemplo, un diccionario para acumular cantidades por
  producto, o `setdefault` para agrupar por categoría), no solo listar u ordenar.
- El formato de guardado en archivo lo diseña el estudiante (no se entrega un formato
  listo), y debe soportar una venta con una cantidad variable de ítems.

---

## 🧩 Requisitos funcionales

### Gestión de productos

- Agregar un producto nuevo: código (único, se rechaza si ya existe), nombre,
  categoría, precio unitario, stock inicial y stock mínimo (para alertas de
  reposición).
- Listar productos, con al menos dos criterios de orden a elección del usuario (por
  ejemplo, por nombre y por stock).
- Buscar un producto por código exacto, y por coincidencia parcial de nombre (que
  devuelva todos los que contengan el texto buscado, sin distinguir mayúsculas).
- Editar el precio, la categoría o el stock mínimo de un producto existente.
- Eliminar un producto **solo si nunca fue vendido**; si ya tiene ventas asociadas,
  el programa debe rechazar la eliminación con un mensaje claro en vez de borrarlo.

### Registrar una venta

- Una venta se arma agregando ítems en un bucle: por cada ítem se pide un código de
  producto y una cantidad, hasta que el usuario decide terminar la venta.
- Antes de confirmar cada ítem, el programa valida que el producto exista y que haya
  stock suficiente; si no lo hay, avisa y no agrega el ítem (la venta puede seguir
  armándose con otros productos).
- Al confirmar la venta completa: se descuenta el stock de cada producto vendido, se
  calcula el subtotal de cada ítem y el total de la venta, se asigna un número de
  venta autoincremental y se guarda la fecha (un texto simple que ingresa el usuario,
  por ejemplo `2026-09-24`; no hace falta validarla como fecha real).
- Una venta sin ningún ítem confirmado no debe registrarse.

### Consultar ventas

- Listar todas las ventas con su número, fecha y total.
- Ver el detalle completo de una venta puntual (todos sus ítems, con producto,
  cantidad, precio unitario de ese momento y subtotal), buscándola por número.
- Listar las ventas en las que participó un producto determinado (buscado por
  código).

### Reportes

- **Producto más vendido**: el producto con mayor cantidad total vendida (unidades).
  Se arma recorriendo todos los ítems de todas las ventas y acumulando la cantidad de
  cada producto en un diccionario (clave: código, valor: cantidad acumulada); el
  resultado sale de buscar la clave con el valor más alto de ese diccionario (por
  ejemplo, con `max(diccionario, key=diccionario.get)`).
- **Ingresos totales**: suma de los totales de todas las ventas registradas.
- **Alerta de stock bajo**: lista de productos cuyo stock actual está por debajo de su
  stock mínimo.
- **Ventas agrupadas por categoría**: cuánto se vendió (en dinero) por cada categoría
  de producto, usando un diccionario armado con `setdefault` (o equivalente) para
  acumular por clave.
- **Últimas ventas**: las últimas 5 ventas registradas, en orden del más reciente al
  más antiguo. Alcanza con la lista de ventas que ya está en memoria: basta con tomar
  los últimos 5 elementos con slicing (por ejemplo `ventas[-5:]`) e invertir ese
  resultado.

### Menú

- Menú principal en bucle con, al menos, estas opciones: gestionar productos (submenú
  con las operaciones de esa sección), registrar venta, consultar ventas (submenú),
  ver reportes (submenú), salir guardando los datos.
- El programa no debe cerrarse ni "romperse" ante ninguna opción inválida o dato mal
  ingresado: siempre vuelve a mostrar el menú correspondiente.

---

## 🗃️ Modelo de datos sugerido

La estructura exacta (diccionario, tupla, lista de diccionarios, etc.) queda a
elección del estudiante, pero como mínimo cada entidad necesita estos datos:

| Entidad | Campos mínimos |
|---|---|
| 📦 Producto | código, nombre, categoría, precio unitario, stock actual, stock mínimo |
| 🧾 Venta | número de venta, fecha, lista de ítems, total |
| 🔖 Ítem de venta | código de producto, nombre del producto, cantidad, precio unitario (al momento de la venta), subtotal |

> 💡 Pista: guardar el nombre y el precio unitario **dentro de cada ítem** (y no solo
> el código) evita que el historial de una venta cambie si más adelante se edita el
> precio o el nombre de ese producto en el catálogo.

## 📦 Arquitectura y estructura de archivos

La aplicación debe ser modular: como mínimo, un módulo para productos, uno para
ventas, uno para persistencia y un punto de entrada con el menú. Por ejemplo (se
pueden usar otros nombres):

```text
proyecto-tienda/
├── productos.py        # modelo y operaciones sobre el catalogo
├── ventas.py            # registrar y consultar ventas
├── reportes.py          # las cinco consultas de la seccion Reportes
├── almacenamiento.py     # guardar y cargar productos.txt y ventas.txt
├── main.py               # menu y punto de entrada
├── productos.txt         # se crea sola, al ejecutar el programa
└── ventas.txt             # se crea sola, al ejecutar el programa
```

## 💾 Persistencia

- Los productos y las ventas se guardan en **dos archivos de texto separados**
  (`productos.txt` y `ventas.txt`), que el programa carga al iniciar y actualiza
  después de cada operación que modifique datos (no solo al salir).
- El formato de cada línea lo define el estudiante. El de productos es directo (un
  producto por línea). El de ventas es el reto: una venta tiene una cantidad
  **variable** de ítems, así que el formato de línea debe poder representarla
  completa (por ejemplo, combinando dos separadores: uno entre los datos generales de
  la venta y otro entre los ítems, o cualquier otro esquema que se elija). El formato
  elegido debe documentarse con un comentario al principio de `almacenamiento.py`.
- Si alguno de los dos archivos todavía no existe (primera ejecución), el programa
  debe iniciar con catálogo y/o historial de ventas vacíos, sin fallar.

---

## 🚧 Manejo de errores exigido

El programa debe anticipar y manejar, sin detenerse con un error sin manejar:

- Datos no numéricos donde se espera un número (precio, stock, cantidad).
- Código de producto vacío o duplicado al agregar.
- Cantidad solicitada mayor al stock disponible.
- Búsquedas, ediciones o eliminaciones sobre un código de producto o un número de
  venta que no existen.
- Intentar eliminar un producto que ya tiene ventas asociadas.
- Alguno de los dos archivos de datos ausente en la primera ejecución.

Se debe usar `try`/`except` con tipos de excepción específicos (por ejemplo
`ValueError`, `KeyError`, `FileNotFoundError`) en vez de capturar todo con un
`except` genérico, y aprovechar `else`/`finally` donde tenga sentido, como se vio en
la Clase 06.

## 🚫 Restricciones técnicas

- Sin bases de datos, sin librerías externas que requieran instalación (`pip`), sin
  interfaz gráfica.
- Sin programación orientada a objetos (clases propias): todo se resuelve con
  funciones, diccionarios, listas, tuplas y conjuntos, como en las Clases 01 a 06.
- Sin el módulo `collections` (ni `Counter`, ni `deque`, ni similares): todo el
  conteo, la agrupación y el historial de ventas se resuelven con listas, tuplas,
  conjuntos y diccionarios simples (`setdefault` sigue siendo válido: es un método de
  los diccionarios, no del módulo `collections`).
- Sin el módulo `datetime` ni similares: la fecha de una venta es un texto simple
  ingresado por el usuario, no un objeto de fecha.
- Identificadores y comentarios en español (salvo palabras reservadas y nombres de la
  biblioteca estándar).

---

## 🧪 Casos de prueba

Se recomienda verificar el programa con un escenario como este:

1. Agregar al menos 4 productos, en al menos 2 categorías distintas, con stocks
   variados (alguno con stock por debajo de lo definido como mínimo).
2. Registrar 3 ventas con distintos ítems cada una; en alguna, intentar pedir más
   cantidad de la que hay en stock y comprobar que el programa lo rechaza sin
   romperse.
3. Consultar el detalle de una de esas ventas por su número.
4. Pedir los cinco reportes y comprobar a mano que los números coinciden con lo
   registrado.
5. Intentar eliminar un producto ya vendido: debe rechazarse. Eliminar uno que nunca
   se vendió: debe funcionar.
6. Salir del programa y volver a abrirlo: catálogo, stocks actualizados e historial
   de ventas deben seguir exactamente igual que al cerrar.
7. Volver a probar dejando algún dato vacío o con letras donde se espera un número:
   el programa debe avisar y seguir funcionando.

---

## 🏆 Extensión opcional (para ir más allá)

Estas tareas no son obligatorias, pero suman si se completan antes de las 12 horas:

- Exportar el reporte de ingresos por categoría a un archivo de texto nuevo
  (`reporte.txt`), legible para alguien que nunca vio el programa.
- Ordenar el ranking de productos más vendidos implementando a mano uno de los
  algoritmos de ordenamiento de la Clase 03 (burbuja, selección o inserción), en vez
  de usar `sorted`.
- Permitir cancelar (anular) una venta ya registrada, devolviendo el stock vendido a
  cada producto involucrado.

---

## 📦 Entregable

Una carpeta de proyecto (por ejemplo `proyecto-tienda/`) con los módulos `.py` del
estudiante, que al ejecutar `python3 main.py` desde la terminal integrada de VS Code,
cumpla todos los requisitos funcionales de arriba. No se entrega guía ni
transcripción: se entrega código propio.

## 📏 Criterios de evaluación

| Criterio | Qué se revisa | Peso |
|---|---|---|
| ✅ Funcionalidad | Las cuatro secciones de requisitos funcionan como se describe | 35% |
| 🧩 Modelo e integridad | Producto/venta bien representados; reglas de stock y de eliminación se respetan | 20% |
| 💾 Persistencia | Ambos archivos se guardan/cargan correctamente, incluida la primera ejecución | 15% |
| 🚧 Manejo de errores | Los seis casos de la sección de errores no rompen el programa | 15% |
| 📦 Modularidad y estilo | Módulos con responsabilidad única, nombres claros, identificadores en español | 10% |
| 🏆 Extensión opcional | Alguna tarea de la sección de extensión resuelta correctamente | +5% extra |

---

## 🏁 Verificación final

El proyecto está completo cuando se puede marcar todo esto:

- [ ] El programa se ejecuta con `python3 main.py` sin errores y sin necesidad de
      instalar nada.
- [ ] Se puede agregar, listar, buscar, editar y eliminar productos, respetando la
      regla de no eliminar uno ya vendido.
- [ ] Se puede registrar una venta con varios ítems, validando stock, y consultarla
      después por su número.
- [ ] Los cinco reportes (producto más vendido, ingresos totales, stock bajo, ventas
      por categoría, últimas 5 ventas) muestran datos correctos.
- [ ] Si se cierra el programa y se vuelve a abrir, catálogo y ventas siguen
      exactamente igual que al salir.
- [ ] Ninguno de los casos de prueba de la sección anterior rompe el programa.

Si algo no funciona, conviene probar primero las funciones de `productos.py` y
`ventas.py` de forma aislada (por ejemplo, desde una sesión interactiva de Python)
antes de sospechar del menú.
