# Importar módulos
import funciones as fun
from random import randint
import heroes


def hero_list_gen():
    heroes_names = []
    heroes_names = [heroes.gen() for _ in range(20)]
    return heroes_names
    # hero_list = []
    # count = 0
    # while count < 20:
    #     hero_list.append(heroes.gen())
    #     count += 1
    # return hero_list


def bar_code_gen():
    barcode = []
    barcode = [randint(10000, 99999) for _ in range(20)]
    return barcode
    # barcode = []
    # count = 0
    # while count < 20:
    #     barcode.append(randint(10000, 99999))
    #     count += 1
    # return barcode
    
    
def quantity_gen():
    quantities = []
    quantities = [randint(0, 50) for _ in range(20)]
    return quantities
    # quantities = []
    # count = 0
    # while count < 20:
    #     quantities.append(randint(0, 50))
    #     count += 1
    # return quantities


def price_gen():
    prices = []
    prices = [round((randint(100, 5000) * 0.1), 1) for _ in range(20)]
    return(prices)
    # prices = []
    # count = 0
    # while count < 20:
    #     prices.append(round((randint(100, 5000) * 0.1), 1))
    #     count += 1
    # return prices

print(hero_list_gen())
print(bar_code_gen())
print(quantity_gen())
print(price_gen())