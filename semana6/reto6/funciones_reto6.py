import sys
import os
import datetime


import sys
import os

def show_store_dict(dictionary):
    """Imprimo el diccionario de la tienda con sus cantidades

    Args:
        dictionary (disct): Diccionario completo de la tienda.
    """
    print("".ljust(27, "*"))

    for key, value in dictionary.items():
        print(key.ljust(25, ".") + str(value[1]).rjust(2))
    print("".ljust(27, "*") + "\n")


def receipt_impression(dictionary):
    """Imprimo el recibo que se le entregará al usuario. Recibe el diccionario con cantidades, precios y precios parciales de la venta.

    Args:
        dictionary (dict): Diccionario con cantidades, precios y precios parciales de la venta.
    """
    total_price = 0
    print("".ljust(58, "="))
    print("Recibo".center(58))
    print("".ljust(58, "="))
    print("Comic".ljust(25, ".") + "Cant.".rjust(2) + "Precio".rjust(8, ".") + "Precio Total".rjust(20, "."))

    for key, value in dictionary.items():
        print(key.ljust(25, ".") + str(value[0]).rjust(2) + str(value[1]).rjust(11, ".") + str(value[2]).rjust(20, "."))
        total_price += value[2]
    print("".ljust(58, "="))
    print("TOTAL".ljust(4), "." + str(round(total_price, 1)).rjust(51, "."))
    print("".ljust(58, "="))
    print("\n")


def temporal_sales_impression(dictionary):
    """Imprimo el recibo que se le entregará al usuario. Recibe el diccionario con cantidades, precios y precios parciales de la venta.

    Args:
        dictionary (dict): Diccionario con cantidades, precios y precios parciales de la venta.
    """
    total_price = 0
    print("".ljust(58, "="))
    print("Ventas del día".center(58))
    print("".ljust(58, "="))
    print("Comic".ljust(25, ".") + "Cant.".rjust(2) + "Precio".rjust(8, ".") + "Precio Total".rjust(20, "."))

    for key, value in dictionary.items():
        print(key.ljust(25, ".") + str(value[0]).rjust(2) + str(value[1]).rjust(11, ".") + str(value[2]).rjust(20, "."))
        total_price += value[2]
    print("".ljust(58, "="))
    print("TOTAL".ljust(4), "." + str(round(total_price, 1)).rjust(51, "."))
    print("".ljust(58, "="))
    print("\n")


def show_dict(dictionary):
    """Imprimo diccionario cuando el argumento de entrada es un diccionario suyos elementos llave-valor estan constituídos por las llaves en formato cadena y los valores un número entero.

    Args:
        dictionary (dict): Diccionario suyos elementos llave-valor estan constituídos por las llaves en formato cadena y los valores un número entero.
    """
    print("".ljust(27, "*"))
    for key, value in dictionary.items():
        print(key.ljust(25, ".") + str(value).rjust(2))
    print("".ljust(27, "*")+"\n")


def store_sale(store_dict, user_dict):
    """Realiza la venta si los productos en la tienda son mayores a los solicitados por el usuario, pero si la cantidad solitada es mayor a la cantidad en la tienda, se le vcende sólo las existencias. En ambos casos se actualiza el inventario de la tienda.

    Args:
        store_dict (dict): Diccionario completio de la tienda.
        user_dict (dict): Diccionario del usuario con las cantidades que desea

    Returns:
        store_stock_updated (dict): Inventario actualizado de la tienda
        comics_sold (dict): Lista de productos vendidos al usuario usada posteriormente en el reporte.
    """
    comics_sold = {}
    store_stock_updated = {}
    for ku, vu in user_dict.items():
        for ks, vs in store_dict.items():
            if ks == ku:
                stock_availible = vs[1]
                user_request = vu
                diff = stock_availible - user_request
                if vu >= vs[1]:
                    store_stock_updated[ks] = 0
                    comics_sold[ks] = vs[1]
                else:
                    store_stock_updated[ks] = diff
                    comics_sold[ks] = vu
    return store_stock_updated, comics_sold


def final_report(store_dict, store_stock_updated):
    """Actualiza todo el diccionario de la tienda usando los datos actualizados obtenidos luego de realizar la venta.

    Args:
        store_dict (dict): Diccionario completo de la tienda.
        store_stock_updated (dict): Diccionario cólo con los valores de las cantidades actualizadas de los productos.

    Returns:
        store_dict (dict): Diccionario completo de la tienda actualizado.
    """
    for store_key, store_value in store_dict.items():
        for stock_key, stock_value in store_stock_updated.items():
            if store_key == stock_key:
                store_dict[store_key][1] = store_stock_updated[store_key]
    return store_dict


def store_receipt(comics_sold, store_dict):
    """Genero el recibo que se le entregará al uauario mediante la creación de listas para guardar los precios, las cantidades y los precios parciales.

    Args:
        comics_sold (dict): Diccionarios con los artículos vendidos.
        store_dict (dict): Diccionario completo de la tienda.

    Returns:
        comic_prices (list): Lista con los precios de los artículos.
        comic_quants (list): Lista con las cantidades de los artículos.
        parcial_price (list): Lista con los precios parciales de los artículos.
    """
    comic_prices = []
    comic_quants = []
    parcial_price = []
    for sale_key, sale_value in comics_sold.items():
        for store_key, store_value in store_dict.items():
            if store_key == sale_key:
                price = store_dict[store_key][2]
                comic_prices.append(price)
                comic_quantity = comics_sold[sale_key]
                comic_quants.append(comic_quantity)
                parcial_price.append(round((price * comic_quantity), 1))

    return comic_prices, comic_quants, parcial_price


def serve_client(store_dict, user_dict, temporal_sales_dict):
    # Imprimo la lista de artículos con cantidades que el usuario desea comprar.
    print("La lista solicitada por el usuario es:")
    show_dict(user_dict)

    # Realizo la venta
    store_stock_updated, comics_sold = store_sale(store_dict, user_dict)

    # Muestro reporte de productos vendidos
    print("Los productos vendidos al usuario: \n")
    show_dict(comics_sold)

    # Actualizo el inventario de la venta con todos sus atributos
    report = final_report(store_dict, store_stock_updated)

    # Construyo el diccionario actualizado de la tienda usando sólo las cantidades en existencia luego de la venta.
    store_stock_updated = {key: value[1] for key, value in zip(report.keys(), report.values())}
    print("El inventario actualizado de la tienda es: \n")
    show_dict(store_stock_updated)

    # Obtengo los valores que se usarán en el recibo que se le entregará al usuario.
    prices, comic_quants, parcial_prices = store_receipt(comics_sold, store_dict)

    # Organizo los datos del recibo en una lista de atributos.
    receipt_attrs = [[comic_quant, price, parcial_price] for comic_quant, price, parcial_price in zip(comic_quants, prices, parcial_prices)]

    # Obtengo los nombres de los artículos.
    products = [name for name in user_dict.keys()]

    # Creo el diccionario con los datos del recibo.
    comics_sold = {product: receipt_attr for product, receipt_attr in zip(products, receipt_attrs)}
    print("El recibo para el usuario es: \n")
    receipt_impression(comics_sold)

    temporal_sales_dict = temporal_sales(comics_sold, temporal_sales_dict)
    return store_stock_updated, comics_sold, temporal_sales_dict


def temporal_sales(comics_sold, temporal_sales_dict):
    for key_comic, value_comic in comics_sold.items():
        if key_comic in temporal_sales_dict.keys():
            temporal_sales_dict[key_comic] += value_comic
        else:
            temporal_sales_dict[key_comic] = value_comic
    return temporal_sales_dict


def sales_report_generator(temporal_sales_dict):
    mypath = os.getcwd()
    print(mypath)
    restore_point = sys.stdout
    sys.stdout = open(mypath + "/semana6/reto6/ventas_dia.txt", "w")
    total_price = 0
    print("".ljust(58, "="))
    print("Ventas del día".center(58))
    print("".ljust(58, "="))
    print("Comic".ljust(25, ".") + "Cant.".rjust(2) + "Precio".rjust(8, ".") + "Precio Total".rjust(20, "."))

    for key, value in temporal_sales_dict.items():
        print(key.ljust(25, ".") + str(value[0]).rjust(2) + str(value[1]).rjust(11, ".") + str(value[2]).rjust(20, "."))
        total_price += value[2]
    print("".ljust(58, "="))
    print("TOTAL".ljust(4), "." + str(round(total_price, 1)).rjust(51, "."))
    print("".ljust(58, "="))
    print(f"Creado en: {datetime.datetime.now()}")
    sys.stdout.close()
    sys.stdout = restore_point
    
    
def store_stock_alert_generator(store_stock_updated):
    max_len_key = 0
    len_value = len("Bajas Existencias")
    for key, value in store_stock_updated.items():
        if store_stock_updated[key] <= 1:
            store_stock_updated[key] = "Bajas Existencias"
        if len(str(key)) > max_len_key:
            max_len_key = len(str(key))

    print("".ljust(max_len_key + len_value + 10, "="))
    print("Reporte de Disponibilidad".center(max_len_key + len_value + 10))
    print("".ljust(max_len_key + len_value + 10, "="))
    for key, value in store_stock_updated.items():
        print(key.ljust(max_len_key + 10, ".") +
              str(value).rjust(len_value, "."))
    print("".ljust(max_len_key + len_value + 10, "="))
    return max_len_key
    
    
def store_stock_alert_txt_generator(store_stock_updated, max_len_key):
    len_value = len("Bajas Existencias")
    mypath = os.getcwd()
    print(mypath)
    restore_point = sys.stdout
    sys.stdout = open(mypath + "/semana6/reto6/disponibilidad.txt", "w")
    print("".ljust(max_len_key + len_value + 10, "="))
    print("Reporte de Disponibilidad".center(max_len_key + len_value + 10))
    print("".ljust(max_len_key + len_value + 10, "="))
    for key, value in store_stock_updated.items():
        print(key.ljust(max_len_key + 10, ".") +
            str(value).rjust(len_value, "."))
    print("".ljust(max_len_key + len_value + 10, "="))
    print(f"Creado en: {datetime.datetime.now()}")
    sys.stdout = restore_point
    