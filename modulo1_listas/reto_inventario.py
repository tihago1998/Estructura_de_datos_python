    # Reto Módulo 1: Gestión de Inventario
# Inventario: lista de sublistas [nombre, cantidad, precio]

inventario = []


def añadir_producto(nombre, cantidad, precio):
    """Añade un producto nuevo o actualiza el stock si ya existe."""
    for producto in inventario:
        if producto[0] == nombre:
            producto[1] += cantidad
            return
    inventario.append([nombre, cantidad, precio])


def actualizar_precio(nombre, nuevo_precio):
    """Modifica el precio de un producto existente."""
    for producto in inventario:
        if producto[0] == nombre:
            producto[2] = nuevo_precio
            return
    print(f"Producto '{nombre}' no encontrado.")


def registrar_venta(nombre, cantidad):
    """Descuenta stock si hay suficiente."""
    for producto in inventario:
        if producto[0] == nombre:
            if producto[1] >= cantidad:
                producto[1] -= cantidad
            else:
                print(f"Stock insuficiente de '{nombre}'.")
            return
    print(f"Producto '{nombre}' no encontrado.")


def mostrar_inventario():
    """Imprime el estado final del inventario."""
    print("--- Inventario ---")
    for nombre, cantidad, precio in inventario:
        print(f"{nombre}: {cantidad} unidades - ${precio}")


# --- Prueba del sistema ---
añadir_producto("teclado", 10, 50000)
añadir_producto("mouse", 20, 25000)
añadir_producto("teclado", 5, 50000)   # actualiza stock existente

actualizar_precio("mouse", 22000)

registrar_venta("teclado", 3)
registrar_venta("mouse", 25)           # debe mostrar stock insuficiente

mostrar_inventario()