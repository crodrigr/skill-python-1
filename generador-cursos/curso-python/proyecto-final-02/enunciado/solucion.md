# 📘 Solución explicada — Proyecto final 02: Sistema de Inventario y Ventas

## 🎯 Objetivo de esta guía

Este documento es **para el repaso en clase**, después de que cada estudiante
intentó resolver el [enunciado](enunciado-proyecto-final-02.md) por su cuenta. No
reemplaza el desafío de pensar la solución propia: se usa **después**, para comparar
decisiones de diseño y para que quien no haya llegado a terminarlo pueda
transcribir una solución de referencia completa y funcional.

Los nombres de funciones, el formato de archivo y la organización exacta de este
documento son **una** solución válida entre varias posibles — el enunciado deja
esas decisiones a criterio del estudiante a propósito. Si tu solución resolvió lo
mismo con otros nombres u otro formato de archivo, también es correcta.

## 📝 Cómo usar esta guía

Cada paso da el código completo de una parte del programa, con una explicación de
qué hace y por qué se decidió así. Si vas a transcribirla, hazlo en el orden en que
aparece, en el archivo indicado en el título de cada paso.

---

## 🧱 Resultado final

```text
proyecto-tienda/
├── productos.py        # Pasos 2, 3 y 4 - catalogo de productos
├── ventas.py            # Pasos 5 y 6 - registrar y consultar ventas
├── reportes.py          # Paso 7 - las cinco consultas de reportes
├── almacenamiento.py    # Pasos 8 y 9 - guardar y cargar productos.txt y ventas.txt
├── main.py              # Pasos 10 a 15 - menu y punto de entrada
├── productos.txt        # se crea solo, al ejecutar el programa (Paso 16)
└── ventas.txt           # se crea solo, al ejecutar el programa (Paso 16)
```

## 🗃️ Modelo de datos que usa esta solución

| Entidad | Representación | Campos |
|---|---|---|
| 📦 Producto | diccionario | `codigo`, `nombre`, `categoria`, `precio`, `stock`, `stock_minimo` |
| 🧾 Venta | diccionario | `numero`, `fecha`, `items` (lista de ítems), `total` |
| 🔖 Ítem de venta | diccionario | `codigo`, `nombre`, `cantidad`, `precio_unitario`, `subtotal` |

El catálogo completo es una **lista de diccionarios de producto**, y el historial
de ventas es una **lista de diccionarios de venta**, cada una con su propia lista de
ítems adentro. Como dice la pista del enunciado, cada ítem guarda su propio
`nombre` y `precio_unitario` (no solo el `codigo`), para que el historial de una
venta vieja no cambie si más adelante se edita ese producto en el catálogo.

---

## 🪜 Pasos

### Paso 1 — Preparar el proyecto en VS Code

Crea una carpeta `proyecto-tienda` y ábrela en Visual Studio Code. Dentro, crea
cuatro archivos vacíos: `productos.py`, `ventas.py`, `reportes.py`,
`almacenamiento.py` y `main.py`. Los archivos `productos.txt` y `ventas.txt` no se
crean a mano: los genera el propio programa la primera vez que se ejecuta (Paso
16).

📖 **Explicación**: igual que en el Proyecto final 01, cada módulo tiene **una**
responsabilidad (Clase 06): `productos.py` sabe de productos, `ventas.py` sabe de
ventas, `reportes.py` sabe de las cinco consultas, `almacenamiento.py` sabe de
guardar/cargar, y `main.py` conecta todo con el menú. Esta vez hay dos entidades
relacionadas (producto y venta), así que son cinco módulos en vez de tres.

### Paso 2 — Modelar un producto y agregarlo al catálogo (`productos.py`)

```python
"""Modulo con el modelo y las operaciones sobre el catalogo de productos."""


def crear_producto(codigo, nombre, categoria, precio, stock, stock_minimo):
    """Crea un diccionario que representa un producto."""
    return {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "stock_minimo": stock_minimo,
    }


def agregar_producto(productos, producto):
    """Agrega un producto al catalogo si su codigo no existe todavia.

    Devuelve True si se agrego, False si el codigo ya estaba en uso.
    """
    if buscar_por_codigo(productos, producto["codigo"]) is not None:
        return False
    productos.append(producto)
    return True


def buscar_por_codigo(productos, codigo):
    """Busca un producto por codigo exacto. Devuelve el diccionario o None."""
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None
```

📖 **Explicación**: `crear_producto` arma el diccionario con los seis campos
mínimos que pide el enunciado. `buscar_por_codigo` es la función más reutilizada de
todo el proyecto (la usan `agregar_producto`, `editar_producto`,
`eliminar_producto` y varias opciones del menú): recorre la lista y devuelve el
diccionario del producto o `None` si no existe. `agregar_producto` la usa primero
para rechazar un código duplicado **antes** de agregar, devolviendo `True`/`False`
para que quien llama decida qué mensaje mostrar.

### Paso 3 — Buscar por nombre, editar y eliminar (`productos.py`)

Agrega estas funciones debajo de las del Paso 2:

```python
def buscar_por_nombre(productos, texto):
    """Devuelve los productos cuyo nombre contiene el texto buscado,
    sin distinguir mayusculas de minusculas."""
    texto = texto.lower()
    return [producto for producto in productos if texto in producto["nombre"].lower()]


def editar_producto(productos, codigo, precio=None, categoria=None, stock_minimo=None):
    """Edita precio, categoria y/o stock minimo de un producto existente.

    Devuelve True si encontro el producto, False si no.
    """
    producto = buscar_por_codigo(productos, codigo)
    if producto is None:
        return False
    if precio is not None:
        producto["precio"] = precio
    if categoria is not None:
        producto["categoria"] = categoria
    if stock_minimo is not None:
        producto["stock_minimo"] = stock_minimo
    return True


def eliminar_producto(productos, codigo):
    """Elimina un producto del catalogo por codigo.

    Devuelve True si lo elimino, False si no lo encontro. Esta funcion NO
    verifica si el producto tiene ventas asociadas: esa regla de integridad
    la aplica quien la llama (main.py), consultando antes a
    ventas.producto_tiene_ventas.
    """
    producto = buscar_por_codigo(productos, codigo)
    if producto is None:
        return False
    productos.remove(producto)
    return True


def descontar_stock(producto, cantidad):
    """Descuenta cantidad del stock de un producto."""
    producto["stock"] -= cantidad
```

📖 **Explicación**: `buscar_por_nombre` usa `texto in nombre.lower()` para una
coincidencia **parcial** sin distinguir mayúsculas, y devuelve una lista (puede
haber más de un resultado). `editar_producto` recibe los tres campos editables
como argumentos **opcionales** (`=None`): si no se pasa un valor para alguno, ese
campo queda igual — así una sola función sirve para editar uno, dos o los tres
campos a la vez. `eliminar_producto` deliberadamente **no** conoce el historial de
ventas: mezclar esa regla acá obligaría a este módulo a importar `ventas`, y
`ventas` ya necesita cosas de `productos` (ver Paso 5), lo que generaría un import
circular. Por eso la regla de "no eliminar si ya fue vendido" se resuelve en
`main.py`, que sí tiene acceso a ambos módulos (Paso 11). `descontar_stock` queda
separada porque se reutiliza al registrar una venta (Paso 12).

### Paso 4 — Ordenar el catálogo (`productos.py`)

Agrega al final de `productos.py`:

```python
def ordenar_por_nombre(productos):
    """Devuelve una lista nueva de productos ordenada por nombre."""
    return sorted(productos, key=lambda producto: producto["nombre"].lower())


def ordenar_por_stock(productos):
    """Devuelve una lista nueva de productos ordenada por stock, de menor a mayor."""
    return sorted(productos, key=lambda producto: producto["stock"])
```

📖 **Explicación**: igual que en el Proyecto final 01, `sorted(..., key=...)`
devuelve una lista **nueva** sin tocar el catálogo original, cumpliendo el
requisito de "al menos dos criterios de orden a elección del usuario".

### Paso 5 — Modelar una venta y confirmarla (`ventas.py`)

```python
"""Modulo con el modelo de venta y las operaciones de registro y consulta."""


def crear_item(codigo, nombre, cantidad, precio_unitario):
    """Crea el diccionario de un item de venta, calculando su subtotal."""
    return {
        "codigo": codigo,
        "nombre": nombre,
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "subtotal": cantidad * precio_unitario,
    }


def siguiente_numero_venta(ventas):
    """Calcula el proximo numero de venta (autoincremental)."""
    if not ventas:
        return 1
    return max(venta["numero"] for venta in ventas) + 1


def confirmar_venta(ventas, fecha, items):
    """Arma y agrega una nueva venta a partir de una lista de items ya validados.

    El total de la venta es la suma de los subtotales de sus items.
    Devuelve el diccionario de la venta creada.
    """
    numero = siguiente_numero_venta(ventas)
    total = sum(item["subtotal"] for item in items)
    venta = {
        "numero": numero,
        "fecha": fecha,
        "items": items,
        "total": total,
    }
    ventas.append(venta)
    return venta
```

📖 **Explicación**: `crear_item` calcula el `subtotal` en el momento (`cantidad *
precio_unitario`), así nadie tiene que recordar hacerlo después. `
siguiente_numero_venta` calcula el número autoincremental **a partir del propio
historial** (el mayor número existente más uno, o `1` si todavía no hay ventas), en
vez de guardar un contador aparte: esto evita que el contador y la lista de ventas
se desincronicen. `confirmar_venta` recibe la lista de ítems **ya armada y
validada** (eso lo hace `main.py` en el Paso 12, pidiendo producto y cantidad en un
bucle): esta función solo arma el diccionario de la venta, calcula el total sumando
los subtotales de cada ítem, y la agrega al historial.

> 💡 En esta solución, el stock se descuenta **ítem por ítem**, en el momento en
> que `main.py` agrega cada ítem a la venta (ver Paso 12), no todo junto acá en
> `confirmar_venta`. Esto evita vender dos veces el mismo stock si una venta
> incluye el mismo producto en más de un ítem, y simplifica la validación: el stock
> que se consulta siempre es el stock "real" en ese instante. Descontar todo junto
> al confirmar es igual de válido, pero exige llevar una cuenta aparte del stock ya
> comprometido en la venta que se está armando.

### Paso 6 — Consultar ventas y validar integridad (`ventas.py`)

Agrega al final de `ventas.py`:

```python
def buscar_venta_por_numero(ventas, numero):
    """Busca una venta por su numero. Devuelve el diccionario o None."""
    for venta in ventas:
        if venta["numero"] == numero:
            return venta
    return None


def ventas_de_producto(ventas, codigo):
    """Devuelve la lista de ventas en las que participo el producto dado."""
    resultado = []
    for venta in ventas:
        for item in venta["items"]:
            if item["codigo"] == codigo:
                resultado.append(venta)
                break
    return resultado


def producto_tiene_ventas(ventas, codigo):
    """Indica si un producto aparece en alguna venta registrada."""
    return len(ventas_de_producto(ventas, codigo)) > 0
```

📖 **Explicación**: `ventas_de_producto` recorre cada venta y, dentro, cada ítem;
en cuanto encuentra uno con el código buscado agrega **la venta completa** (no el
ítem) al resultado y corta con `break` para no agregarla dos veces si el mismo
producto apareciera más de una vez en la misma venta. `producto_tiene_ventas` es la
función clave para la regla de integridad del enunciado ("no se puede eliminar un
producto que ya tiene ventas asociadas"): reutiliza `ventas_de_producto` en vez de
repetir el recorrido, y la llama `main.py` **antes** de borrar un producto (Paso
11).

### Paso 7 — Los cinco reportes (`reportes.py`)

```python
"""Modulo con las cinco consultas de reportes sobre productos y ventas."""
import productos as productos_modulo


def producto_mas_vendido(ventas):
    """Devuelve (codigo, nombre, cantidad) del producto con mayor cantidad total
    vendida, o None si todavia no hay ventas."""
    cantidades = {}
    nombres = {}
    for venta in ventas:
        for item in venta["items"]:
            codigo = item["codigo"]
            cantidades[codigo] = cantidades.get(codigo, 0) + item["cantidad"]
            nombres[codigo] = item["nombre"]
    if not cantidades:
        return None
    codigo_top = max(cantidades, key=cantidades.get)
    return (codigo_top, nombres[codigo_top], cantidades[codigo_top])


def ingresos_totales(ventas):
    """Suma el total de todas las ventas registradas."""
    return sum(venta["total"] for venta in ventas)


def stock_bajo(productos):
    """Devuelve los productos cuyo stock actual esta por debajo de su stock minimo."""
    return [producto for producto in productos if producto["stock"] < producto["stock_minimo"]]


def ventas_por_categoria(ventas, productos):
    """Devuelve un diccionario {categoria: total vendido en dinero}."""
    totales = {}
    for venta in ventas:
        for item in venta["items"]:
            producto = productos_modulo.buscar_por_codigo(productos, item["codigo"])
            categoria = producto["categoria"] if producto is not None else "Sin categoria"
            totales.setdefault(categoria, 0)
            totales[categoria] += item["subtotal"]
    return totales


def ultimas_ventas(ventas, cantidad=5):
    """Devuelve las ultimas `cantidad` ventas, de la mas reciente a la mas antigua."""
    recientes = ventas[-cantidad:]
    recientes.reverse()
    return recientes
```

📖 **Explicación**: cada reporte sigue la pista que da el propio enunciado.
`producto_mas_vendido` arma un diccionario `{codigo: cantidad_acumulada}`
recorriendo todos los ítems de todas las ventas (y uno paralelo con los nombres,
para no tener que buscarlo después), y usa `max(diccionario, key=diccionario.get)`
para encontrar la clave con el valor más alto. `ventas_por_categoria` necesita el
catálogo además de las ventas, porque cada ítem solo guarda el `codigo` del
producto (no su categoría): busca el producto con `productos_modulo.buscar_por_codigo`
para saber su categoría actual, y usa `setdefault(categoria, 0)` para que la
primera vez que aparece una categoría arranque en `0` antes de sumarle el
subtotal. `ultimas_ventas` toma `ventas[-5:]` (los últimos 5 elementos, del más
viejo al más nuevo dentro de ese grupo) y les aplica `.reverse()` para que queden
del más reciente al más antiguo; como el slice ya crea una lista **nueva**,
`.reverse()` no afecta al historial original.

> 🚫 Fíjate que este módulo **no** usa `collections.Counter` ni nada parecido para
> contar: todo se arma con diccionarios simples y `setdefault`/`.get`, como exige
> el enunciado.

### Paso 8 — Guardar y cargar productos (`almacenamiento.py`)

```python
"""Modulo para guardar y cargar productos y ventas en archivos de texto.

Formato elegido:
- productos.txt: un producto por linea, campos separados por "|":
    codigo|nombre|categoria|precio|stock|stock_minimo
- ventas.txt: una venta por linea, con dos separadores anidados: "|" entre
  los datos generales de la venta y ";" entre los items; dentro de cada item,
  los campos van separados por ",":
    numero|fecha|item1;item2;...|total
    donde cada item es: codigo,nombre,cantidad,precio_unitario,subtotal
  Para reconstruir una venta se separa primero por "|", luego el bloque de
  items por ";", y por ultimo cada item por ",".
"""

SEP_PRODUCTO = "|"
SEP_VENTA = "|"
SEP_ITEMS = ";"
SEP_CAMPOS_ITEM = ","


def cargar_productos(ruta):
    """Carga el catalogo desde un archivo de texto.

    Si el archivo no existe todavia, devuelve una lista vacia en vez de fallar.
    """
    productos = []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                codigo, nombre, categoria, precio, stock, stock_minimo = linea.split(SEP_PRODUCTO)
                productos.append({
                    "codigo": codigo,
                    "nombre": nombre,
                    "categoria": categoria,
                    "precio": float(precio),
                    "stock": int(stock),
                    "stock_minimo": int(stock_minimo),
                })
    except FileNotFoundError:
        print("No se encontro un catalogo previo; se inicia vacio.")
    return productos


def guardar_productos(ruta, productos):
    """Guarda el catalogo completo, sobrescribiendo el contenido anterior."""
    with open(ruta, "w", encoding="utf-8") as archivo:
        for producto in productos:
            archivo.write(
                f"{producto['codigo']}{SEP_PRODUCTO}{producto['nombre']}"
                f"{SEP_PRODUCTO}{producto['categoria']}{SEP_PRODUCTO}{producto['precio']}"
                f"{SEP_PRODUCTO}{producto['stock']}{SEP_PRODUCTO}{producto['stock_minimo']}\n"
            )
```

📖 **Explicación**: el comentario al principio del archivo documenta el formato
completo, como pide el enunciado. `productos.txt` es el caso simple: cada línea es
un producto con sus seis campos separados por `|`; `cargar_productos` deshace esa
unión con `.split(SEP_PRODUCTO)` y convierte `precio` a `float`, `stock` y
`stock_minimo` a `int` (en el archivo todo se guarda como texto). El `try`/`except
FileNotFoundError` es el que resuelve "primera ejecución, el archivo no existe
todavía": en vez de que el programa falle, `cargar_productos` simplemente devuelve
una lista vacía.

### Paso 9 — Guardar y cargar ventas, con ítems variables (`almacenamiento.py`)

Agrega al final de `almacenamiento.py`:

```python
def _item_a_texto(item):
    return (
        f"{item['codigo']}{SEP_CAMPOS_ITEM}{item['nombre']}"
        f"{SEP_CAMPOS_ITEM}{item['cantidad']}{SEP_CAMPOS_ITEM}{item['precio_unitario']}"
        f"{SEP_CAMPOS_ITEM}{item['subtotal']}"
    )


def _texto_a_item(texto):
    codigo, nombre, cantidad, precio_unitario, subtotal = texto.split(SEP_CAMPOS_ITEM)
    return {
        "codigo": codigo,
        "nombre": nombre,
        "cantidad": int(cantidad),
        "precio_unitario": float(precio_unitario),
        "subtotal": float(subtotal),
    }


def cargar_ventas(ruta):
    """Carga el historial de ventas desde un archivo de texto.

    Si el archivo no existe todavia, devuelve una lista vacia en vez de fallar.
    """
    ventas = []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                numero, fecha, bloque_items, total = linea.split(SEP_VENTA)
                items = [_texto_a_item(texto_item) for texto_item in bloque_items.split(SEP_ITEMS)]
                ventas.append({
                    "numero": int(numero),
                    "fecha": fecha,
                    "items": items,
                    "total": float(total),
                })
    except FileNotFoundError:
        print("No se encontro un historial de ventas previo; se inicia vacio.")
    return ventas


def guardar_ventas(ruta, ventas):
    """Guarda el historial completo de ventas, sobrescribiendo el contenido anterior."""
    with open(ruta, "w", encoding="utf-8") as archivo:
        for venta in ventas:
            bloque_items = SEP_ITEMS.join(_item_a_texto(item) for item in venta["items"])
            archivo.write(
                f"{venta['numero']}{SEP_VENTA}{venta['fecha']}"
                f"{SEP_VENTA}{bloque_items}{SEP_VENTA}{venta['total']}\n"
            )
```

📖 **Explicación**: acá está el verdadero desafío de persistencia del proyecto —
una venta tiene una cantidad **variable** de ítems. La solución usa dos
separadores anidados: `_item_a_texto`/`_texto_a_item` convierten **un solo ítem**
a/desde texto usando `,` entre sus campos; `guardar_ventas` une todos los ítems de
una venta con `SEP_ITEMS.join(...)` (`;`) para formar un único bloque de texto, y
ese bloque pasa a ser **un campo más** de la línea de la venta, separada por `|`
igual que número, fecha y total. Al cargar, el orden se invierte: primero
`linea.split(SEP_VENTA)` separa los cuatro campos generales (incluido el bloque de
ítems todavía unido), después `bloque_items.split(SEP_ITEMS)` separa cada ítem, y
por último `_texto_a_item` separa los campos de cada ítem por `,`. Los dos
guiones bajos al principio de `_item_a_texto` y `_texto_a_item` son una convención
de Python para marcar que son funciones de **uso interno** del módulo (nadie
afuera de `almacenamiento.py` necesita llamarlas directamente).

### Paso 10 — Encabezado y submenú de productos: altas y consultas (`main.py`)

```python
"""Punto de entrada del Gestor de Inventario y Ventas."""
import productos as productos_modulo
import ventas as ventas_modulo
import reportes
import almacenamiento

ARCHIVO_PRODUCTOS = "productos.txt"
ARCHIVO_VENTAS = "ventas.txt"


def pedir_numero(mensaje, tipo=float):
    """Pide un numero hasta recibir un valor valido, usando el tipo indicado (int o float)."""
    while True:
        texto = input(mensaje).strip()
        try:
            return tipo(texto)
        except ValueError:
            print("Eso no es un numero valido. Intenta de nuevo.")


def mostrar_menu_productos():
    print("\n--- Gestion de productos ---")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar por codigo")
    print("4. Buscar por nombre")
    print("5. Editar producto")
    print("6. Eliminar producto")
    print("7. Volver al menu principal")


def mostrar_producto(producto):
    print(
        f"[{producto['codigo']}] {producto['nombre']} | {producto['categoria']} | "
        f"precio: {producto['precio']} | stock: {producto['stock']} "
        f"(minimo: {producto['stock_minimo']})"
    )


def opcion_agregar_producto(catalogo):
    codigo = input("Codigo: ").strip()
    if not codigo:
        print("El codigo no puede estar vacio.")
        return
    nombre = input("Nombre: ").strip()
    categoria = input("Categoria: ").strip()
    precio = pedir_numero("Precio unitario: ", float)
    stock = pedir_numero("Stock inicial: ", int)
    stock_minimo = pedir_numero("Stock minimo: ", int)
    producto = productos_modulo.crear_producto(codigo, nombre, categoria, precio, stock, stock_minimo)
    agregado = productos_modulo.agregar_producto(catalogo, producto)
    if agregado:
        print(f"Producto '{nombre}' agregado.")
    else:
        print(f"Ya existe un producto con el codigo '{codigo}'.")


def opcion_listar_productos(catalogo):
    if not catalogo:
        print("No hay productos registrados todavia.")
        return
    print("Ordenar por: 1) Nombre  2) Stock")
    opcion = input("Elige una opcion: ").strip()
    if opcion == "2":
        lista = productos_modulo.ordenar_por_stock(catalogo)
    else:
        lista = productos_modulo.ordenar_por_nombre(catalogo)
    for producto in lista:
        mostrar_producto(producto)


def opcion_buscar_por_codigo(catalogo):
    codigo = input("Codigo a buscar: ").strip()
    producto = productos_modulo.buscar_por_codigo(catalogo, codigo)
    if producto is None:
        print(f"No existe ningun producto con el codigo '{codigo}'.")
    else:
        mostrar_producto(producto)


def opcion_buscar_por_nombre(catalogo):
    texto = input("Texto a buscar en el nombre: ").strip()
    encontrados = productos_modulo.buscar_por_nombre(catalogo, texto)
    if not encontrados:
        print("No se encontro ningun producto con ese texto.")
    for producto in encontrados:
        mostrar_producto(producto)
```

📖 **Explicación**: `import productos as productos_modulo` y `import ventas as
ventas_modulo` usan un alias para no confundir el módulo con las variables
`catalogo`/`historial_ventas` que van a circular por `main.py`. `pedir_numero`
generaliza el patrón de pedir un número hasta que sea válido (ya usado en el
Proyecto final 01): recibe el `tipo` (`int` o `float`) como parámetro, así una sola
función sirve para precio, stock, cantidad y número de venta. Nota que
`opcion_agregar_producto` **no** verifica el código duplicado por su cuenta: deja
que `agregar_producto` (Paso 2) lo haga, y solo decide qué mensaje mostrar según el
`True`/`False` que recibe — evita repetir la misma búsqueda dos veces.

### Paso 11 — Submenú de productos: editar, eliminar y el bucle (`main.py`)

Agrega debajo de las funciones del Paso 10:

```python
def opcion_editar_producto(catalogo):
    codigo = input("Codigo del producto a editar: ").strip()
    if productos_modulo.buscar_por_codigo(catalogo, codigo) is None:
        print(f"No existe ningun producto con el codigo '{codigo}'.")
        return
    print("Deja vacio un campo para no modificarlo.")
    texto_precio = input("Nuevo precio: ").strip()
    categoria = input("Nueva categoria: ").strip()
    texto_stock_minimo = input("Nuevo stock minimo: ").strip()

    precio = None
    if texto_precio:
        try:
            precio = float(texto_precio)
        except ValueError:
            print("El precio no es un numero valido; no se modifica.")

    stock_minimo = None
    if texto_stock_minimo:
        try:
            stock_minimo = int(texto_stock_minimo)
        except ValueError:
            print("El stock minimo no es un numero valido; no se modifica.")

    productos_modulo.editar_producto(
        catalogo, codigo,
        precio=precio,
        categoria=categoria if categoria else None,
        stock_minimo=stock_minimo,
    )
    print("Producto actualizado.")


def opcion_eliminar_producto(catalogo, historial_ventas):
    codigo = input("Codigo del producto a eliminar: ").strip()
    if productos_modulo.buscar_por_codigo(catalogo, codigo) is None:
        print(f"No existe ningun producto con el codigo '{codigo}'.")
        return
    if ventas_modulo.producto_tiene_ventas(historial_ventas, codigo):
        print("No se puede eliminar: el producto ya tiene ventas asociadas.")
        return
    productos_modulo.eliminar_producto(catalogo, codigo)
    print("Producto eliminado.")


def menu_productos(catalogo, historial_ventas):
    while True:
        mostrar_menu_productos()
        opcion = input("Elige una opcion: ").strip()
        if opcion == "1":
            opcion_agregar_producto(catalogo)
        elif opcion == "2":
            opcion_listar_productos(catalogo)
        elif opcion == "3":
            opcion_buscar_por_codigo(catalogo)
        elif opcion == "4":
            opcion_buscar_por_nombre(catalogo)
        elif opcion == "5":
            opcion_editar_producto(catalogo)
        elif opcion == "6":
            opcion_eliminar_producto(catalogo, historial_ventas)
        elif opcion == "7":
            break
        else:
            print("Opcion invalida, intenta de nuevo.")
        almacenamiento.guardar_productos(ARCHIVO_PRODUCTOS, catalogo)
```

📖 **Explicación**: en `opcion_editar_producto`, dejar un campo vacío significa "no
lo quiero cambiar": por eso cada campo vacío se convierte en `None` antes de
llamar a `editar_producto`, que ya sabe (Paso 3) que `None` significa "no tocar
este campo". Si se escribe algo que no es un número válido para precio o stock
mínimo, se avisa y ese campo en particular queda sin modificar, pero el resto de
la edición sigue su curso. `opcion_eliminar_producto` es donde se aplica la regla
de integridad: primero confirma que el producto existe, después consulta
`ventas_modulo.producto_tiene_ventas` (Paso 6) **antes** de borrar — si ya tiene
ventas asociadas, rechaza la eliminación con un mensaje claro, tal como pide el
enunciado. `menu_productos` es el submenú en bucle: después de **cada** opción
(menos "volver") guarda el catálogo en disco, para que ningún cambio se pierda
aunque el programa se cierre de forma inesperada.

### Paso 12 — Registrar una venta (`main.py`)

```python
def registrar_venta(catalogo, historial_ventas):
    print("\n--- Registrar venta ---")
    items = []
    while True:
        codigo = input("Codigo de producto (vacio para terminar la venta): ").strip()
        if not codigo:
            break
        producto = productos_modulo.buscar_por_codigo(catalogo, codigo)
        if producto is None:
            print(f"No existe ningun producto con el codigo '{codigo}'.")
            continue
        cantidad = pedir_numero("Cantidad: ", int)
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            continue
        if cantidad > producto["stock"]:
            print(f"Stock insuficiente: solo hay {producto['stock']} unidades de '{producto['nombre']}'.")
            continue
        item = ventas_modulo.crear_item(producto["codigo"], producto["nombre"], cantidad, producto["precio"])
        items.append(item)
        productos_modulo.descontar_stock(producto, cantidad)
        print(f"Agregado: {cantidad} x {producto['nombre']} = {item['subtotal']}")

    if not items:
        print("La venta no tiene items; no se registra.")
        return

    fecha = input("Fecha de la venta (por ejemplo 2026-09-24): ").strip()
    venta = ventas_modulo.confirmar_venta(historial_ventas, fecha, items)
    print(f"Venta numero {venta['numero']} registrada. Total: {venta['total']}")
    almacenamiento.guardar_productos(ARCHIVO_PRODUCTOS, catalogo)
    almacenamiento.guardar_ventas(ARCHIVO_VENTAS, historial_ventas)
```

📖 **Explicación**: esta es la función más importante del proyecto. El bucle `while
True` arma la lista `items` de a uno, pidiendo código y cantidad; un código vacío
es la señal para terminar de agregar ítems. Por cada ítem se valida, **en este
orden**: que el producto exista, que la cantidad sea mayor a cero, y que no supere
el stock disponible — si falla cualquiera de las tres, se avisa con `continue` y
la venta sigue armándose (no se rompe ni se cancela toda la venta por un ítem
inválido), tal como pide el enunciado. Cuando un ítem pasa las tres validaciones,
recién ahí se crea con `crear_item` y se descuenta el stock con
`descontar_stock` — descontarlo en este momento (y no al final) hace que, si el
mismo producto aparece en un segundo ítem de la misma venta, la validación de
stock ya vea el stock actualizado. Al salir del bucle, si `items` quedó vacío (el
usuario terminó sin confirmar ningún ítem), la venta **no se registra**; si tiene
al menos un ítem, se pide la fecha y se llama a `confirmar_venta` (Paso 5), y se
guardan **ambos** archivos (productos, porque cambió el stock, y ventas, porque hay
una venta nueva).

### Paso 13 — Consultar ventas (`main.py`)

```python
def mostrar_venta_resumen(venta):
    print(f"Venta #{venta['numero']} | {venta['fecha']} | total: {venta['total']}")


def mostrar_venta_detalle(venta):
    mostrar_venta_resumen(venta)
    for item in venta["items"]:
        print(
            f"  - {item['cantidad']} x {item['nombre']} ({item['codigo']}) "
            f"a {item['precio_unitario']} = {item['subtotal']}"
        )


def mostrar_menu_consultar_ventas():
    print("\n--- Consultar ventas ---")
    print("1. Listar todas las ventas")
    print("2. Ver detalle de una venta")
    print("3. Ventas por producto")
    print("4. Volver al menu principal")


def opcion_listar_ventas(historial_ventas):
    if not historial_ventas:
        print("Todavia no hay ventas registradas.")
        return
    for venta in historial_ventas:
        mostrar_venta_resumen(venta)


def opcion_detalle_venta(historial_ventas):
    numero = pedir_numero("Numero de venta: ", int)
    venta = ventas_modulo.buscar_venta_por_numero(historial_ventas, numero)
    if venta is None:
        print(f"No existe ninguna venta con el numero {numero}.")
    else:
        mostrar_venta_detalle(venta)


def opcion_ventas_por_producto(historial_ventas):
    codigo = input("Codigo de producto: ").strip()
    encontradas = ventas_modulo.ventas_de_producto(historial_ventas, codigo)
    if not encontradas:
        print("Ese producto no participo en ninguna venta.")
    for venta in encontradas:
        mostrar_venta_resumen(venta)


def menu_consultar_ventas(historial_ventas):
    while True:
        mostrar_menu_consultar_ventas()
        opcion = input("Elige una opcion: ").strip()
        if opcion == "1":
            opcion_listar_ventas(historial_ventas)
        elif opcion == "2":
            opcion_detalle_venta(historial_ventas)
        elif opcion == "3":
            opcion_ventas_por_producto(historial_ventas)
        elif opcion == "4":
            break
        else:
            print("Opcion invalida, intenta de nuevo.")
```

📖 **Explicación**: `mostrar_venta_resumen` (número, fecha, total) y
`mostrar_venta_detalle` (que reutiliza el resumen y además recorre `venta["items"]`)
separan **qué tan completa** es la información que se muestra; así
`opcion_listar_ventas` usa la versión corta para no saturar la pantalla con muchas
ventas, mientras que `opcion_detalle_venta` usa la versión completa para una sola
venta puntual, encontrada por número con `buscar_venta_por_numero` (Paso 6).
`opcion_ventas_por_producto` reutiliza `ventas_de_producto` (Paso 6) para listar en
qué ventas participó un código dado.

### Paso 14 — Reportes (`main.py`)

```python
def mostrar_menu_reportes():
    print("\n--- Reportes ---")
    print("1. Producto mas vendido")
    print("2. Ingresos totales")
    print("3. Alerta de stock bajo")
    print("4. Ventas por categoria")
    print("5. Ultimas 5 ventas")
    print("6. Volver al menu principal")


def opcion_producto_mas_vendido(historial_ventas):
    resultado = reportes.producto_mas_vendido(historial_ventas)
    if resultado is None:
        print("Todavia no hay ventas registradas.")
    else:
        codigo, nombre, cantidad = resultado
        print(f"Producto mas vendido: {nombre} ({codigo}) con {cantidad} unidades.")


def opcion_ingresos_totales(historial_ventas):
    total = reportes.ingresos_totales(historial_ventas)
    print(f"Ingresos totales: {total}")


def opcion_stock_bajo(catalogo):
    bajos = reportes.stock_bajo(catalogo)
    if not bajos:
        print("Ningun producto esta por debajo de su stock minimo.")
    for producto in bajos:
        mostrar_producto(producto)


def opcion_ventas_por_categoria(historial_ventas, catalogo):
    totales = reportes.ventas_por_categoria(historial_ventas, catalogo)
    if not totales:
        print("Todavia no hay ventas registradas.")
    for categoria, total in totales.items():
        print(f"{categoria}: {total}")


def opcion_ultimas_ventas(historial_ventas):
    recientes = reportes.ultimas_ventas(historial_ventas)
    if not recientes:
        print("Todavia no hay ventas registradas.")
    for venta in recientes:
        mostrar_venta_resumen(venta)


def menu_reportes(catalogo, historial_ventas):
    while True:
        mostrar_menu_reportes()
        opcion = input("Elige una opcion: ").strip()
        if opcion == "1":
            opcion_producto_mas_vendido(historial_ventas)
        elif opcion == "2":
            opcion_ingresos_totales(historial_ventas)
        elif opcion == "3":
            opcion_stock_bajo(catalogo)
        elif opcion == "4":
            opcion_ventas_por_categoria(historial_ventas, catalogo)
        elif opcion == "5":
            opcion_ultimas_ventas(historial_ventas)
        elif opcion == "6":
            break
        else:
            print("Opcion invalida, intenta de nuevo.")
```

📖 **Explicación**: cada opción de este submenú es una capa muy delgada sobre su
función equivalente de `reportes.py` (Paso 7): pide los datos que falten (ninguno,
en este caso, salvo mostrar resultados), llama a la función del módulo, y da
formato al resultado para la consola. Separar "calcular el reporte" (en
`reportes.py`) de "mostrarlo" (acá) permite, por ejemplo, probar
`reportes.ingresos_totales(historial_ventas)` desde una sesión interactiva de
Python sin tener que pasar por el menú.

### Paso 15 — El menú principal y `main()` (`main.py`)

Al final de `main.py`:

```python
def mostrar_menu_principal():
    print("\n=== Gestor de Inventario y Ventas ===")
    print("1. Gestionar productos")
    print("2. Registrar venta")
    print("3. Consultar ventas")
    print("4. Ver reportes")
    print("5. Salir")


def main():
    catalogo = almacenamiento.cargar_productos(ARCHIVO_PRODUCTOS)
    historial_ventas = almacenamiento.cargar_ventas(ARCHIVO_VENTAS)

    while True:
        mostrar_menu_principal()
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            menu_productos(catalogo, historial_ventas)
        elif opcion == "2":
            registrar_venta(catalogo, historial_ventas)
        elif opcion == "3":
            menu_consultar_ventas(historial_ventas)
        elif opcion == "4":
            menu_reportes(catalogo, historial_ventas)
        elif opcion == "5":
            almacenamiento.guardar_productos(ARCHIVO_PRODUCTOS, catalogo)
            almacenamiento.guardar_ventas(ARCHIVO_VENTAS, historial_ventas)
            print("Datos guardados. Hasta pronto!")
            break
        else:
            print("Opcion invalida, intenta de nuevo.")


if __name__ == "__main__":
    main()
```

📖 **Explicación**: `catalogo` y `historial_ventas` se cargan **una sola vez**, al
principio de `main()`, y de ahí en adelante se pasan como argumento a cada
submenú — son las dos únicas "fuentes de verdad" de todo el programa, y como
listas y diccionarios se pasan por referencia, cualquier cambio que haga un
submenú (agregar una venta, editar un producto) se ve reflejado inmediatamente en
esas mismas variables. La opción "5" guarda ambos archivos una última vez por las
dudas, y usa `break` para salir del bucle principal. Como cada submenú ya guarda
después de sus propias operaciones (Pasos 11 y 12), los datos nunca dependen
exclusivamente de haber elegido "Salir": si alguien cierra la terminal a la fuerza
en medio de una sesión, lo último guardado sigue ahí.

### Paso 16 — Probar el programa completo

Guarda todos los archivos y, en la terminal integrada de VS Code, ejecuta:

```bash
python3 main.py
```

Recorre el mismo escenario que pide el enunciado:

1. Agrega al menos 4 productos en 2 categorías distintas, alguno con stock por
   debajo de su mínimo.
2. Registra 3 ventas con distintos ítems; en alguna, pide más cantidad de la que
   hay en stock y comprueba que el programa la rechaza sin romperse (el mensaje
   "Stock insuficiente..." y la venta sigue armándose con otros ítems).
3. Consulta el detalle de una de esas ventas por su número.
4. Pide los cinco reportes y verifica a mano que los números coinciden con lo
   registrado.
5. Intenta eliminar un producto ya vendido (debe rechazarse) y uno que nunca se
   vendió (debe funcionar).
6. Sal del programa (opción 5) y vuelve a abrirlo: catálogo, stocks actualizados e
   historial de ventas deben verse exactamente igual.
7. Prueba dejar algún dato vacío o con letras donde se espera un número: el
   programa debe avisar y seguir funcionando (ya cubierto por `pedir_numero` en
   el Paso 10, y por las validaciones del Paso 12).

Si corriste este escenario, vas a ver en `productos.txt` y `ventas.txt` el mismo
formato que describe el comentario del Paso 8, y al reabrir el programa el stock
y el historial van a coincidir exactamente con lo que quedó al salir.

---

## 🏁 Verificación final

El proyecto está completo cuando se puede marcar todo esto:

- [ ] El programa se ejecuta con `python3 main.py` sin errores y sin instalar
      nada.
- [ ] Se puede agregar, listar (por nombre y por stock), buscar (por código y por
      nombre parcial), editar y eliminar productos, respetando la regla de no
      eliminar uno ya vendido.
- [ ] Se puede registrar una venta con varios ítems, validando stock en cada uno,
      y consultarla después por su número.
- [ ] Los cinco reportes (producto más vendido, ingresos totales, stock bajo,
      ventas por categoría, últimas 5 ventas) muestran datos correctos.
- [ ] Si se cierra el programa y se vuelve a abrir, catálogo y ventas siguen
      exactamente igual que al salir.
- [ ] Ningún dato no numérico, código inexistente, código duplicado, cantidad
      mayor al stock, o archivo ausente en la primera ejecución rompe el
      programa.

Si algo no funciona, conviene probar primero las funciones de `productos.py` y
`ventas.py` de forma aislada (por ejemplo, desde una sesión interactiva de Python)
antes de sospechar del menú.
