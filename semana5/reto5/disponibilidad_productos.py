import datos_aleatorios as da
import funciones_reto5 as fun
from arte import logo


# Genero el diccionario de la tienda
store_dict = da.store_dict_generator()

temporal_sales_dict = {}

while True:
    print(logo)
    print("Esta es la tienda de historietas Freak Comics.")
    print("Presione [1] para visualizar el inventario de la tienda.")
    print("Presione [2] para atender a un cliente y realizar la venta.")
    print(
        "Presione [3] para cerrar la tienda y ver el reporte de las ventas del día.")
    print(
        "Presione [4] para generear el reporte de disponibilidad de productos al finalizar el día.")
    print("Presione 'Q' para finalizar.")
    store_choice = input(">>> ")
    if store_choice.lower() == "q":
        break
    elif store_choice == "1":
        print("El inventario de la tienda es el siguiente:")
        # Imprimo el inventario de la tienda antes de realizar la venta al usuario.
        fun.show_store_dict(store_dict)
    elif store_choice == "2":
        # Cada vez que se realiza una venta genero un diccionario aleatorio para el usuario
        user_dict = da.user_dict_generator(store_dict)
        # Realizo la venta de los productos al usuario
        store_stock_updated, comics_sold, sales_dict = fun.serve_client(
            store_dict, user_dict, temporal_sales_dict)
    elif store_choice == "3":
        # Genero reporte de ventas del día.
        fun.temporal_sales_impression(sales_dict)
    elif store_choice == "4":
        # Genero reporte de disponibilidad de productos con alerta de bajas existencias.
        fun.store_stock_alert(store_stock_updated)
