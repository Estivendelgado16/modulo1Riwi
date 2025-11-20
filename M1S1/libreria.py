
while True: 
    nombre_producto = input("Ingrese nombre del libro: ")
    if not nombre_producto:
        print("\nEl nombre no puede estar vacío. Por favor, ingrese un nombre válido.")

    elif not nombre_producto.replace(" ", "").isalpha():
        print("\nEl nombre solo debe contener letras y espacios. Por favor, ingrese un nombre válido.")
    else:
        break
    

while True:    
    try:
        precio_unitario = float(input("\nIngrese el precio del producto: "))
        if precio_unitario < 0:
            print("\nEl precio no puede ser negativo. Por favor, ingrese un precio válido.")
        else:
            break
    except ValueError:
        print("\nError: el precio debe ser un número válido.")
         
while True:
    try:
        cantidad = int(input("\nIngrese la cantidad: "))
        if cantidad <= 0:
            print("\nLa cantidad debe ser mayor que cero.")
        else:
            break
    except ValueError:
        print("\nError: la cantidad debe ser un número entero.")

costo_total = precio_unitario * cantidad

print(f"Producto: {nombre_producto}| precio unitario: {precio_unitario}| cantidad: {cantidad}| costo total: {costo_total}")





