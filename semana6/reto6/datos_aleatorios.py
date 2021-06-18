import heroes
from random import randint, uniform, choice
from pprint import pprint


def store_dict_generator():
    """Esta función genera el diccionario de la tienda aleatoreamente considerando las cantidades, precios y valores.

    Returns:
        store_dict (dict): Diccionario de la tienda con diccionarios internos corespondientes a los atributos de cada producto.
    """
    
    # Genero aleatoriamente los datos de los productos
    heroes_names = [heroes.gen() for _ in range(20)]
    # Genero aleatoriamente los datos del codigo de barras
    barcodes = [randint(10000, 99999) for _ in range(20)]
    # Genero aleatoriamente los datos de las cantidades
    quantities = [randint(1, 30) for _ in range(20)]
    # Genero aleatoriamente los datos de los precios
    prices = [round(uniform(100, 5000), 1) for _ in range(20)]

    # Creo la lista de diccionarios de los códigos de barras
    barcode_labels = ["Codigo"] * 20
    barcode_dicts = [{code_label: code} for (code_label, code) in zip(barcode_labels, barcodes)]

    # Creo la lista de diccionarios de los códigos de las cantidades
    quantity_labels = ["Cantidad"] * 20
    quantity_dicts = [{quantity_label: quantity} for (quantity_label, quantity) in zip(quantity_labels, quantities)]

    # Creo la lista de diccionarios de los precios
    price_labels = ["Precio"] * 20
    price_dicts = [{price_label: price} for (price_label, price) in zip(price_labels, prices)]

    # Concateno los diccioanrios de códigos de baras, cantidades y precios
    attributes_dict = {}
    for _ in range(20):
        attributes_dict[_] = {**barcode_dicts[_], **quantity_dicts[_], **price_dicts[_]}

    # Creo diccionario de la tienda con el nombre de los productos
    store_dict = dict(zip(heroes_names, list(attributes_dict.values())))

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

