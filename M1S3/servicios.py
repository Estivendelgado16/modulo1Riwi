inventario = []

def agregarProducto():
    while True:
        nombre = input("ingresa el nombre del producto: ").title()
        precio = float(input("precio: $ "))
        cantidad = int(input("cantidad: "))
        
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        inventario.append(producto)
        print(inventario)
        break


def mostrarInventario():
    if not inventario:
        print("No hay inventario")
    else:
        for producto in inventario:
            print(f"nombre: {producto['nombre']} | precio: $ {producto['precio']} | cantidad: {producto['cantidad']}")

def buscarProducto():

    enconProduc = input("Ingresa el producto que quiere buscar: ").title()


    if not inventario:
        print("No hay inventario")
    else:
        encontrado = False
        for producto in inventario:
            if producto['nombre'] == enconProduc:
                encontrado = True
                break
        
        if encontrado:
            print("producto existente")

    
def actualizarProducto():
    print()

def eliminarProducto():
    print()

def calcEstadistica():
    print()