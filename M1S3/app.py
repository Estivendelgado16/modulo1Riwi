
import servicios

while True: 
    menu = int(input(
    "\n* TIENDA *\n"
    "\n1. Agregar\n"
    "2. Mostrar\n"
    "3. Buscar\n"
    "4. Actualizar\n"
    "5. Eliminar\n"
    "6. Estadísticas\n"
    "7. Guardar CSV\n"
    "8. Cargar CSV\n"
    "9. Salir\n"
    "\nOpción: "
    ))

    if menu == 1:
        servicios.agregarProducto()
    elif menu == 2:
        servicios.mostrarInventario()
    elif menu == 3:
        servicios.buscarProducto()
    elif menu == 4:
        servicios.actualizarProducto()
    elif menu == 5:
        servicios.eliminarProducto()
    elif menu == 6:
        servicios.calcEstadistica()
    elif menu == 9:
        break




