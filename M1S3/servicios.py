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
    if not inventario:
        print("No hay inventario")
    else:
        actualizarProduc = input("Ingresa el producto que quiere actualizar: ").title()
        for producto in inventario:
            if producto['nombre'] == actualizarProduc:
                nuevoNombre = input("ingresa nuevo nombre del producto: ").title()
                nuevoPrecio = float(input("ingresa el nuevo precio: $ "))
                nuevaCantidad = int(input("ingresa la nueva cantidad: "))
                producto['nombre'] = nuevoNombre
                producto['precio'] = nuevoPrecio
                producto['cantidad'] = nuevaCantidad
                print("Producto actualizado")
                break
        else:
            print("Producto no encontrado")

def eliminarProducto():
    if not inventario:
        print("No hay inventario")
    else:
        eliminarProducto = input("Ingresa el producto que quiere eliminar: ").title()
        for i in enumerate(inventario):
            if i[1]['nombre'] == eliminarProducto:
                del inventario[i[0]]
                print("Producto eliminado")
                break
        else:
            print("Producto no encontrado")
    

def calcEstadistica():
    print()