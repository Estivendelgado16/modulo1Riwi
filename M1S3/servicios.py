import csv
# Lista global para guardar los productos
inventario = []


#funcion para agregar productos 
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


#funcion para mostar los productos
def mostrarInventario():
    if not inventario:
        print("No hay inventario")
    else:
        for producto in inventario:
            print(f"nombre: {producto['nombre']} | precio: $ {producto['precio']} | cantidad: {producto['cantidad']}")


#funcion para buscar 
def buscarProducto():

    enconProduc = input("Ingresa el producto que quiere buscar: ").title()

    #valido que no este vacio
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

#funcion para actualizar
def actualizarProducto():
    #valido que no este vacio
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


#funcion para eliminar
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
    
#funcion para estadistica 
def calcEstadistica():
    if not inventario:
        print("Nohay inventario")
    else:
        totalProductos = len(inventario)
        totalValor = sum(productos['precio'] * productos['cantidad'] for productos in inventario)
        print(f"Total de productos: {totalProductos}")
        print(F"Valor total de productos: $ {totalValor}")

#funcion para guardar el inventario en cvs
def guardarCSV():
    with open("inventario.csv", "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["nombre", "precio", "cantidad"])  

        for producto in inventario:
            writer.writerow([producto["nombre"], producto["precio"], producto["cantidad"]])

    print("Inventario guardado en inventario.csv")

#funcion para cargar el cvs
def cargarCSV():
    try:
        with open("inventario.csv", "r", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)
            inventario.clear() 

            for fila in reader:
                inventario.append({
                    "nombre": fila["nombre"],
                    "precio": float(fila["precio"]),
                    "cantidad": int(fila["cantidad"])
                })

        print("Inventario cargado correctamente")

    except FileNotFoundError:
        print("No existe un archivo CSV, se creará uno cuando guardes.")

