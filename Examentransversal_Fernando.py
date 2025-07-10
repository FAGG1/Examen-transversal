# Diccionario de productos con información técnica
productos = {
    "A": ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    "B": ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    "C": ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

# Diccionario de stock con precios y cantidad disponible
stock = {
    "A": [387990, 10],
    "B": [749990, 2],
    "C": [349990, 1]
}

# Mostrar el stock disponible
def mostrar_stock_disponible(stock_dict):
    print(" Modelos disponibles:")
    for modelo, datos in stock_dict.items():
        precio, cantidad = datos
        if cantidad > 0:
            print(f"Modelo {modelo} - Precio: ${precio} - Stock: {cantidad} unidades")

# Buscar y mostrar información técnica de un modelo
def mostrar_info_modelo(modelo):
    if modelo in productos:
        print(f"Información del modelo {modelo}:")
        info = productos[modelo]
        print("Marca:", info[0])
        print("Pantalla:", info[1], "pulgadas")
        print("RAM:", info[2])
        print("Disco:", info[3])
        print("Capacidad:", info[4])
        print("Procesador:", info[5])
        print("Video:", info[6])
    else:
        print("Modelo no encontrado.")

# Simular una compra
def simular_compra(modelo, cantidad):
    if modelo in stock:
        precio, disponible = stock[modelo]
        if disponible >= cantidad:
            stock[modelo][1] -= cantidad
            total = precio * cantidad
            print(f" Compra exitosa. Total a pagar: ${total}")
        else:
            print(" No hay suficiente stock disponible.")
    else:
        print(" Modelo no encontrado en el inventario.")

# Ejemplo de uso
mostrar_stock_disponible(stock)
mostrar_info_modelo("A")
simular_compra("A", 2)
mostrar_stock_disponible(stock)