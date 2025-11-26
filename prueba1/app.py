
import servicios

while True:
    try: 
        menu = int(input(""
        "---- menu ----\n"
        "1. Registrar Producto\n"
        "2. Consultar Productos\n"
        "3. actualizar productos\n"
        "4. Eliminar Producto\n"
        "5. Vender Producto\n"
        "6. registrar cliente\n"
        "0. Salir\n"
        "\nIngrese una opción: "))


        if menu == 1:
            servicios.addProduct()
        elif menu == 2:
            servicios.searchProducts()
        elif menu == 3:
            servicios.upDateProduct()
        elif menu == 4:
            servicios.deleteProduct()
        elif menu == 5:
            servicios.sellProduct()
        elif menu  == 6:
            servicios.registerClient()
        elif menu == 0:
            break

    except ValueError:
        print("Por favor ingrese una opción válida.")
        