""" Reto semana 4
    Fundamentos de Programación
    MisonTiC 2022
    Thomas Ramirez Rozo
    Mayo 30-2021 """

import funciones as fun
from random import randint
import heroes
from arte import logo


def hero_list_gen():
    """Genera aleatoiamente 20 nombres de héroes usando el módulo heroes

    Returns:
        heroes_names (list): Lista de 20 posiciones con los nombres de los héroes
    """
    heroes_names = [heroes.gen() for _ in range(20)]
    return heroes_names
    # hero_list = []
    # count = 0
    # while count < 20:
    #     hero_list.append(heroes.gen())
    #     count += 1
    # return hero_list


def bar_code_gen():
    """Genera aleatoriamente 20 números entre 10000 y 99999 correspondiente al código de barras del producto.

    Returns:
        barcode (list): Lista de 20 posiciones con los códigos de barras
    """
    barcode = [randint(10000, 99999) for _ in range(20)]
    return barcode
    # barcode = []
    # count = 0
    # while count < 20:
    #     barcode.append(randint(10000, 99999))
    #     count += 1
    # return barcode


def quantity_gen():
    """Genera aleatoriamente 20 numeros cortrespondientes a cada producto en inventario

    Returns:
        quantities (list): Lista de 20 posiciones corresponiente a la cantidad de productos en inventario.
    """
    quantities = [randint(0, 30) for _ in range(20)]
    return quantities
    # quantities = []
    # count = 0
    # while count < 20:
    #     quantities.append(randint(0, 50))
    #     count += 1
    # return quantities


def price_gen():
    """Genera aleatoriamente 20 numeros cortrespondientes al precio de cada producto

    Returns:
        prices (list): Lista de 20 posiciones corresponiente a la cantidad de productos en inventario.
    """
    prices = [round((randint(100, 5000) * 0.1), 1) for _ in range(20)]
    return(prices)
    # prices = []
    # count = 0
    # while count < 20:
    #     prices.append(round((randint(100, 5000) * 0.1), 1))
    #     count += 1
    # return prices


def store_list_gen():
    """Genera la lista de la tienda con cada uno de los atributos para cada producto. Cada elemento de lista es una sub-lista con los valores de Nombre, Código de barras, Precio, Cantidad e ID.

    Returns:
        store_list (list): Lista con los atributos de los productos de la tienda.
    """
    store_list = [[id_num, bar_code, heroe, quantity, price] for [id_num, bar_code, heroe, quantity, price] in zip(range(20), bar_codes, heroes, quantities, prices)]
    # product = []
    # for id_num, bar_code, heroe, quantity, price in zip(range(20), bar_codes, heroes, quantities, prices):
    #     product = [id_num, bar_code, heroe, quantity, price]
    #     store_list.append(product)
    return store_list


def comic_store_options():
    """Genera el menú de atención al usuario

    Returns:
        usr - 1 (int): Número entero correspondiente al usuario a atender.
    """
    print("Bienvenido a la tienda de comics Freak Comics.")
    print("En estos momentos se encuentran en el mostrador 6 usuarios, ¿a cual desea antender?")
    usr = int(input("Ingrese un numero entre 1 y 6:\n>>> "))
    return (usr - 1)


def user_name_extractor(store_list, user_list):
    """Extrae los nombres de la lista de la tienda y los remplaza en los ids de la ista del usuario.

    Args:
        store_list (list): Lista de la tienda con los atributos para cada producto
        user_list (list): Lista del usuario en formato id, cantidad

    Returns:
        article (lista): Lista del usuario en formato Nombre, Cantidad
    """
    updated_user_list = []
    for i in range(len(store_list)):
        for j in range(len(user_list)):
            if user_list[j][0] == store_list[i][0]:
                updated_user_list.append(store_list[i][2])
    return updated_user_list


def users_id_updater(users_list):
    """Aplica la modificación del id a la lista de todos los usuarios.

    Args:
        users_list (list):  Lista de usuarios con su lista de productos.

    Returns:
        updated_users_list (list): Id modificado para todos la lista de todos los usuarios
    """
    updated_users_list = [user_id_fixer(user_list) for user_list in users_list]
    # updated_users_list = []
    # for user_list in users_list:
    #     updated_users_list.append(user_id_fixer(user_list))
    return updated_users_list


def user_id_fixer(user_list):
    """Acomoda el id de los artículos de la tienda para que empiece en cero para facilitar su trabajo con listas

    Args:
        user_list (list): Lista con los productos de los usuarios

    Returns:
        new_user_list (list): Lista actualizada con los id modificados.
    """
    new_user_list = []
    for article in user_list:
        article[0] = article[0] - 1
        new_user_list.append(article)
    return new_user_list


def store_names_quantities_extractor(store_list):
    """Extrae el nombre y las cantidades de los productos de la tienda y los empaqueta en una lista en formato [nombre, cantidad]

    Args:
        store_list (list): Lista completa de la tienda con atributos

    Returns:
        quant_name (list): Lista de la tienda en formato [nombre, cantidad] 
    """
    quant_name = [[article[2], article[3]] for article in store_list]
    # articles_name_quant = []
    # for article in store_list:
    #     articles_name_quant.append([article[2], article[3]])
    return quant_name


def user_name_quantity_extractor(article_names, user_list):
    """Extrae el nombre y las cantidades de la lista del usuario y los empaqueta en una lista en formato [nombre, cantidad]

    Args:
        article_names (list): Lista de los productos de la tienda en formato [nombre, cantidad]
        user_list (list): Lista de los productos de cada usuario

    Returns:
        update_user_list (list): Lista en formato [nombre, cantidad] correspondiente para cada usuario
    """
    sorted_products = sorted(user_list)
    update_user_list = []
    for name, user_product in zip(article_names, sorted_products):
        update_user_list.append([name, user_product[1]])
    return update_user_list

# Creo listas para las propiedades de los productos de la tienda
heroes = hero_list_gen()
bar_codes = bar_code_gen()
quantities = quantity_gen()
prices = price_gen()
store_list = store_list_gen()

# Lista de los productos y cantidades de cada usuario
user_list_1 = [[1, 10], [3, 25], [9, 1], [6, 20], [8, 5], [7, 3]]
user_list_2 = [[19, 5], [10, 6], [11, 8], [2, 4], [4, 9], [1, 7]]
user_list_3 = [[18, 9], [13, 6], [15, 4], [5, 2], [10, 4], [20, 2]]
user_list_4 = [[2, 5], [3, 1], [5, 2], [8, 3], [9, 1], [19, 2]]
user_list_5 = [[16, 2], [17,  3], [18, 4], [12, 5], [8, 6], [6, 7]]
user_list_6 = [[5, 8], [10,  3], [12, 4], [1, 6], [16, 7], [10, 1]]

# Lista de los usuarios
users_list = [user_list_1, user_list_2, user_list_3,
              user_list_4, user_list_5, user_list_6]

# Actualizo el id de la lista del usuario para que empiece en cero
updated_users_list = users_id_updater(users_list)

# Imprimo el arte
print(logo)

# Imprimo las opciones de atención al cliente
user = comic_store_options()

# Remplazo los id de los productos de la tienda por su nombre
articles_in_user_list = user_name_extractor(
    store_list, updated_users_list[user])

# Extraigo la lista de los productos de la tienda en formato [nombre, cantidad]
store_quantities = store_names_quantities_extractor(store_list)

# Extraigo la lista de los productos del usuario en formato [nombre, cantidad]
user_quantities = user_name_quantity_extractor(
    articles_in_user_list, users_list[user])
print("El usuario solicitó las siguientes historietas en las siguientes cantidades:\n")
fun.show_lists(user_quantities)


print("De la lista del usuario, tenemos la siguiente cantidad de comics disponibles\n")
# Reviso las existencias en el inventario
user_quantities_in_store = fun.quantity_checker(
    store_quantities, user_quantities)
# Imprimo inventario
fun.show_lists(user_quantities_in_store)

print("Luego de la venta al usuario, el inventario de la tienda es el siguiente:\n")
# Realizo la venta
store_stock_updated, comics_sold = fun.store_sale(
    store_quantities, user_quantities)
fun.show_lists(store_stock_updated)

print("Productos vendidos al usuario\n")
fun.show_lists(comics_sold)
print("Luego de la venta al usuario, el inventario de la tienda es el siguiente:")
# Luego de la venta muestro el reporte
sales_report = fun.sales_store_report(store_stock_updated)
fun.show_lists(sales_report)
