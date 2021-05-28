""" Modulo Listas
    Funciones para practicas con listas
    Oscar Franco-Bedoya
    Mayo 10-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
import random


def generar_lista():
    tamaño_lista = int(input("Ingrese el tamaño de la lista: \n>>> "))
    mi_lista = []
    for _ in range(tamaño_lista):
        mi_lista.append(random.randint(0, 10))

    print(f"A continuacion se generará una lista aletoria de tamaño {tamaño_lista} y con numeros aleatorios de 0 a 10")

    print("Su lista es:")
    print(mi_lista)
    return mi_lista


def suma_acumulativa(mi_lista):
    suma = [0] * len(mi_lista)
    valor_acumulado = 0
    for idx in range(len(mi_lista)):
        valor_acumulado += mi_lista[idx]
        suma[idx] += valor_acumulado
    print(suma)


def traductor_pig_latin(lista_palabras):
    my_word = random.choice(lista_palabras)
    es_vocal = id_letra_inicial(my_word)
    if es_vocal:
        final_word = my_word.lower() + "yay"
        return final_word
    else:
        letra_ini = my_word[0]
        new_word = my_word.replace(letra_ini, '', 1)
        final_word = new_word + letra_ini + "ay"
        return final_word


def id_letra_inicial(word):
    vowels = ["a", "e", "i", "o", "u"]
    if word[0] in vowels:
        es_vocal = True
    else:
      es_vocal = False
    return es_vocal
  
  
def identificador_frutas(frutas):
    frutas_A = []
    for fruta in frutas:
        if "a" in fruta:
            frutas_A.append(fruta)
    return frutas_A
  

def pedirCadena():
    cadena = input('Ingrese una cadena de valores alfabeticos: ')
    return cadena.lower()


def son_palindromos(cadena):
    cadena = cadena.replace(" ", "")
    cadena1 = cadena
    cadena2 = cadena[::-1]
    if cadena1 == cadena2:
        return print("La cadena es palindroma")
    return print("La cadena no es palindroma")
