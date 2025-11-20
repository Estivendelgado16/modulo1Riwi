# Lista global para guardar los productos
inventario = []

def agregar_producto():

    while True:
        nombre = input("\nIngresa el nombre del producto: ").strip().lower()
        precio = float(input("ingresa el precio: "))
        cantidad = int(input(" ingresaa la cantidad: "))

        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        inventario.append(producto)  
        print(f"\nProducto '{producto['nombre']}' agregado con éxito.")
        break



def mostrar_inventario():
    
        if not inventario:
            print("\nEl inventario está vacío.")
        else:
            print("\n📦 Inventario actual:")
            for producto in inventario:
                print(f"- {producto['nombre']}, {producto['precio']}, ({producto['cantidad']}) unidades")
                
        while True:
            print("\nQue deseas hacer ahora?\n" 
                "\n 1.volver al menu pricipal " 
                "\n 2.Salir del programa")

            opcion = int(input("\nSelecciona una opcion (1 o 2)"))

            if opcion == 1:
                 print("\nvolviendo al menu principal")
                 return
            elif opcion == 2:
                 print("\nsaliendo del programa")
                 exit()
            else: 
                 print("opcion no valida")


        
        


def eliminar_producto():

    if not inventario:
        print("el inventario esta vacio")
        return
    
    print("productos disponibles")
    for producto in inventario:
        print(f"-{producto['nombre']}")

    delete = input("Que producto quiere eliminar")
    
    productEncontrado = None
    for producto in inventario:
         if producto["nombre"] == delete:
            productEncontrado = producto
            break
         
    if productEncontrado:
        inventario.remove(productEncontrado)
        print(f"producto {delete} eliminado con exito")
    else:
        print(f"No se encontró el producto '{delete}'.")



def estadistica():

        totalUnidades = sum(producto['cantidad'] for producto in inventario)
        totalPrecio = sum(producto["precio"] * producto["cantidad"] for producto in inventario)

        print(f"Total de unidades: {totalUnidades}")
        print(f"Valor total del inventario: {totalPrecio}")
        









while True:
    try:
        print(f"\n------ Menu de Inventario ------ "
             " \n 1. Agregar Producto "
             " \n 2. Mostrar Inventario "
             " \n 3. Eliminar Producto "
             " \n 4. Estadistica"
             " \n 5. Salir")

        opcion = int(input("\nSeleccione una opcion (1-4): "))
    
        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            mostrar_inventario()    
        elif opcion == 3:
            eliminar_producto() 
        elif opcion == 4:
            estadistica()
        elif opcion == 5:
            print("Saliendo del programa...")
            break
            
            
    except ValueError as e:
            print("Opcion no valida. Por favor intente de nuevo. {e}")



