import datos_aleatorios as da
import formating_data as format_d
import funciones_reto6 as fun
import data_visualization as da_vis
from arte import logo
from pprint import pprint


# Genero el diccionario de la tienda
# store_dict = da.store_dict_generator()

# TODO Generar ek diccionario para los productos de la tienda y usuario
# TODO Función para visualizar productos
# TODO Función que realice la venta de los productos solicitados por un usuario y genera el pago solicitado por el usuario
# TODO Crear una función que imprima un report de disponibilidad de productos en el establecimiento al finalizar el día
# TODO Guardar reporte de un archivo de las ventas del día y en otro archivo los productos de la tienda. Colocar fecha del reporte
# TODO Al finalizar realizar una grafica de cantidad vendida de cada uno de los productos.


t_store_dict = da.store_dict_generator()
store_dict = format_d.format_store_dictionary(t_store_dict)

pprint(store_dict)


# t_formated_store_dict = []
# for _ in range(len(formated_store_dict)):
#     t_formated_store_dict.append(list(formated_store_dict[_]))
#     print(t_formated_store_dict[_])


temporal_sales_dict = {}

while True:
    print(logo)
    print("Esta es la tienda de historietas Freak Comics.")
    print("Presione [1] para visualizar el inventario de la tienda.")
    print("Presione [2] para atender a un cliente y realizar la venta.")
    print("Presione [3] para cerrar la tienda y ver el reporte de las ventas del día.")
    print("Presione [4] para generear los repostes de ventas y disponibilidad despues de cerrar la tienda.")
    print("Presione 'Q' para finalizar.")
    store_choice = input(">>> ")
    if store_choice.lower() == "q":
        break
    elif store_choice == "1":
        print("El inventario de la tienda es el siguiente:")
        # Imprimo el inventario de la tienda antes de realizar la venta al usuario.
        format_d.show_full_store_dict(t_store_dict)
        # da_vis.graph_store_stock(store_dict)
    elif store_choice == "2":
        # Genero el diccionario del usuario
        user_dict = da.user_dict_generator(store_dict)
        store_stock_updated, comics_sold, sales_dict = fun.serve_client(store_dict, user_dict, temporal_sales_dict)
    elif store_choice == "3":
        fun.temporal_sales_impression(sales_dict)
    elif store_choice == "4":
        fun.sales_report_generator(sales_dict)
        max_len_key = fun.store_stock_alert_generator(store_stock_updated)
        fun.store_stock_alert_txt_generator(store_stock_updated, max_len_key)
        da_vis.graph_store_stock(sales_dict)