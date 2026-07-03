nombre_cliente = ("")
producto_seleccionado = []
precio_producto = 0
cantidad_pedida = 0
total_a_pagar = 0

def agregar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    while not validar_nombre_cliente(nombre):
        print("Error: El nombre del cliente no puede estar vacío.")
        nombre = input("Ingrese el nombre del cliente: ")

def menu():
    print(" ===== CAFÉ DEL CÓDIGO =====")
    print("1. Ver menú de productos")
    print("2. Realizar un pedido")
    print("3. Ver resumen de ventas del día")
    print("4. Salir")
    print("============================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-4): "))
            if opcion in [1, 2, 3, 4]:
                return opcion
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def mostrar_menu_productos():
    print(" ===== MENÚ DE PRODUCTOS =====")
    print("1. Café Americano - $4.000")
    print("2. Café Latte - $3.500")
    print("3. Té Verde - $2.500")
    print("4. Pastel de Chocolate - $4.000")
    print("5. Salir del menú de productos")
    print("==============================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            if opcion in [1, 2, 3, 4, 5]:
                return opcion
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def realizar_pedido():
    global producto_seleccionado, precio_producto, cantidad_pedida, total_a_pagar
    while True:
        mostrar_menu_productos()
        opcion_producto = leer_opcion()
        
        if opcion_producto == 1:
            producto_seleccionado.append("Café Americano")
            precio_producto = 4000
        elif opcion_producto == 2:
            producto_seleccionado.append("Café Latte")
            precio_producto = 3500
        elif opcion_producto == 3:
            producto_seleccionado.append("Té Verde")
            precio_producto = 2500
        elif opcion_producto == 4:
            producto_seleccionado.append("Pastel de Chocolate")
            precio_producto = 4000
        elif opcion_producto == 5:
            print("Saliendo del menú de productos...")
            print(f"Total a pagar: ${total_a_pagar}")
            break

        cantidad_pedida = int(input(f"Ingrese la cantidad de {producto_seleccionado[-1]}: "))
        total_a_pagar += precio_producto * cantidad_pedida
        print(f"Producto agregado: {producto_seleccionado[-1]} x {cantidad_pedida} - Total parcial: ${total_a_pagar}")

def ver_resumen_ventas():
    print(" ===== RESUMEN DE VENTAS DEL DIA =====")
    print(f"Cliente: {nombre_cliente}")
    print("Productos pedidos:")
    for producto in producto_seleccionado:
        print(f"- {producto}")
    print(f"total a pagar: ${total_a_pagar}")

def validar_nombre_cliente(valor):
    return valor.strip() != ""

def validar_producto(valor):
    return valor.strip() != ""

def validar_cantidad(valor):
    try:
        cantidad = int(valor)
        return cantidad > 0
    except ValueError:
        return False

def validar_precio(valor):
    try:
        precio = float(valor)
        return precio > 0
    except ValueError:
        return False
    
def validar_total(valor):
    try:
        total = float(valor)
        return total >= 0
    except ValueError:
        return False

def validar_opcion(valor):
    try:
        opcion = int(valor)
        return opcion in [1, 2, 3, 4, 5]
    except ValueError:
        return False

def leer_opcion():
    while True:
        opcion = input("Seleccione una opción (1-5): ")
        if validar_opcion(opcion):
            return int(opcion)
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def validar_mostrar_menu(valor):
    return valor.strip() != ""

def main():
    while True:
        menu()
        opcion = leer_opcion()
        
        if opcion == 1:
            mostrar_menu_productos()
        elif opcion == 2:
            agregar_cliente()
            realizar_pedido()
        elif opcion == 3:
            ver_resumen_ventas()
        elif opcion == 4:
            print("Gracias por su visita.Que tenga un buen dia!")
            break
main()