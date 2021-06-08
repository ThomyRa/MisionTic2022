import heroes
from random import randint, choice, uniform
import funciones_reto5 as fun
from arte import logo


def store_dict_generator():
    """Para cada producto de la tienda genero aleatoriamente su nombre, código de barras, cantidades, precios.

    Returns:
        store_dict (dict): Diccionario con los productos de la tieda, siendo las llaves el nombre del producto y los valores una lista con su código de barras, cantidad y precio.
    """
    # Genero los datos aleatorios
    heroes_names = [heroes.gen() for _ in range(20)]
    barcodes = [randint(10000, 99999) for _ in range(20)]
    quantities = [randint(1, 30) for _ in range(20)]
    prices = [round(uniform(100, 5000), 1) for _ in range(20)]

    # Emnpaqueto los valores de la lista que correspondientes a los valores del diccionario
    comic_attributes = [[barcode, quantity, price] for barcode, quantity, price in zip(barcodes, quantities, prices)]

    # Genero diccionario de la tienda
    store_dict = {comic_name: attributes for comic_name, attributes in zip(heroes_names, comic_attributes)}
    return store_dict


def user_dict_generator(store_dict):
    """Creo el diccionario correspondiente a las compras del usuario, tomando el nombre del artículo del diccionario de la tienda y generando las cantidades a comprar, aleatoreamente.

    Args:
        store_dict (dict): Diccionario de la tienda de dónde se obtienen los nombres de los artículos

    Returns:
       user_dict (dict): Diccionario con el nombre de los artículos y las cantidades que desea comprar.
    """
    # Obtengo las llaves del diccionario de la tienda
    comics_names = list(store_dict.keys())

    # Obtengo 6 nombres aleatoriuos para los productos de los usuarios
    user_products = [choice(comics_names) for _ in range(6)]
    # Genero las cantidades del usuario
    user_quantities = [randint(1, 30) for _ in range(6)]
    # Empaqueto el diccionario del usuario
    user_dict = {user_product: user_quantity for user_product, user_quantity in zip(user_products, user_quantities)}
    return user_dict


# Genero el diccionario de la tienda
store_dict = store_dict_generator()
# Gebero el diccionario del usuario
user_dict = user_dict_generator(store_dict)

print(logo)


print("El inventario de la tienda es el siguiente:")
# Imprimo el inventario de la tienda antes de realizar la venta al usuario.
fun.show_store_dict(store_dict)

# Imprimo la lista de artículos con cantidades que el usuario desea comprar.
print("La lista solicitada por el usuario es:")
fun.show_dict(user_dict)

# Realizo la venta
store_stock_updated, comics_sold = fun.store_sale(store_dict, user_dict)

# Muestro reporte de productos vendidos
print("Los productos vendidos al usuario: \n")
fun.show_dict(comics_sold)

# Actualizo el inventario de la venta con todos sus atributos
report = fun.final_report(store_dict, store_stock_updated)

# Construyo el diccionario actualizado de la tienda usando sólo las cantidades en existencia luego de la venta.
store_stock_updated = {key: value[1] for key, value in zip(report.keys(), report.values())}
print("El inventario actualizado de la tienda es: \n")
fun.show_dict(store_stock_updated)

# Obtengo los valores que se usarán en el recibo que se le entregará al usuario.
prices, comic_quants, parcial_prices = fun.store_receipt(comics_sold, store_dict)

# Organizo los datos del recibo en una lista de atributos.
receipt_attrs = [[comic_quant, price, parcial_price] for comic_quant, price, parcial_price in zip(comic_quants, prices, parcial_prices)]

# Obtengo los nombres de los artículos.
products = [name for name in store_stock_updated.keys()]

# Creo el diccionario con los datos del recibo.
receipt_dict = {product: receipt_attr for product, receipt_attr in zip(products, receipt_attrs)}
print("El recibo para el usuario es: \n")
fun.receipt_impression(receipt_dict)
