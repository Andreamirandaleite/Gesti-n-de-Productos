import re

# Lista de productos
productos = []

# Función para cargar datos desde un archivo en el formato específico
def cargar_datos():
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                # Utilizamos regex para extraer nombre, precio y cantidad (en este caso el "Xkg" como unidad).
                match = re.match(r"(.+):\s(\d+\.?\d*)\s.*", linea.strip())
                if match:
                    nombre = match.group(1).strip()
                    precio = float(match.group(2))
                    cantidad = "Xkg"  # Asumimos que es por kilogramo
                    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    except FileNotFoundError:
        print("No se encontró el archivo productos.txt. Iniciando con una lista vacía.")

# Función para guardar datos en un archivo
def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']}: {producto['precio']} gs {producto['cantidad']}\n")
    print("Datos guardados en productos.txt")

# Función para añadir un producto
def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    try:
        precio = float(input("Introduce el precio del producto (en gs): "))
        cantidad = input("Introduce la unidad (ej. 'Xkg' para por kilogramo): ")
        productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        print("Producto añadido exitosamente.")
    except ValueError:
        print("Error: El precio debe ser un número.")

# Función para ver todos los productos
def ver_productos():
    if productos:
        print("\nLista de productos:")
        for producto in productos:
            print(f"{producto['nombre']}: {producto['precio']} gs {producto['cantidad']}")
    else:
        print("No hay productos para mostrar.")

# Función para actualizar un producto
def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            try:
                nuevo_nombre = input("Introduce el nuevo nombre (dejar en blanco para no cambiar): ")
                nuevo_precio = input("Introduce el nuevo precio (dejar en blanco para no cambiar): ")
                nueva_cantidad = input("Introduce la nueva unidad (dejar en blanco para no cambiar): ")

                if nuevo_nombre:
                    producto["nombre"] = nuevo_nombre
                if nuevo_precio:
                    producto["precio"] = float(nuevo_precio)
                if nueva_cantidad:
                    producto["cantidad"] = nueva_cantidad

                print("Producto actualizado.")
                return
            except ValueError:
                print("Error: El precio debe ser un número.")
    print("Producto no encontrado.")

# Función para eliminar un producto
def eliminar_producto():
    nombre = input("Introduce el nombre del producto a eliminar: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            productos.remove(producto)
            print("Producto eliminado.")
            return
    print("Producto no encontrado.")

# Función para el menú principal
def menu():
    cargar_datos()
    while True:
        print("\nSistema de Gestión de Productos")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

# Ejecutar el programa
menu()
