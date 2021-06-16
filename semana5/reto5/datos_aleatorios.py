import heroes
from random import randint, choice, uniform

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

    # Emnpaqueto los valores de la lista correspondientes a los valores del diccionario
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
