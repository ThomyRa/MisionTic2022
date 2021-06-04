import heroes
from random import randint
from pprint import pprint

heroes_names = [heroes.gen() for _ in range(20)]
barcodes = [randint(10000, 99999) for _ in range(20)]
quantities = [randint(0, 30) for _ in range(20)]
prices = [round((randint(100, 5000) * 0.1), 1) for _ in range(20)]


comic_attributes = [[barcode, quantity, price] for barcode, quantity, price in zip(barcodes, quantities, prices)]


store_dict = {comic_name: attributes for comic_name, attributes in zip(heroes_names, comic_attributes)}


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



