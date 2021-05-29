""" Modulo Ciclos
    Funciones para practicas con ciclos
    Thomas Ramírez Rozo
    Mayo 26-2021 """

# Definición de Funciones


def simulador_caida_libre(altura):
    g = 9.8
    t = 1
    distancias = [0, ]
    dist = (1/2) * g * (t ** 2)
    while altura > dist:
        dist = round((1/2) * g * (t ** 2))
        t += 1
        dist_cercana = min(distancias, key=lambda _:abs(_-altura))
        print(f"La distancia al suelo transcurridos {t} segundos son: {dist_cercana}m ")
        distancias.append(dist)


def generador_generaciones(generacion):
    num_personas = 2 ** generacion
    for idx in range(0, generacion + 1):
        personas = 2 ** idx
        print(f"Generación: {idx}   Personas: {personas}".ljust(round(num_personas/2) + 4, " ") + ("*"*personas).center(num_personas, " "))


def constructor_triangulos(pisos):
    cadena_horizontal = ""
    num_consecutivo = 0
    for piso in range(pisos + 1):
        for num in range(piso):
            num_consecutivo += 1
            cadena_horizontal += str(num_consecutivo) + " "
        print(cadena_horizontal)
        cadena_horizontal = ""


def constructor_tableros(longitud):
    flag = 0
    for idx in range(longitud):
        filas_tablero(longitud, flag)
        flag = 1
    # lado_interno = round(longitud/2)
    # cuadrados_negros = ""
    # for _ in range(longitud):
    #     cuadrado_negro = generador_cuadrados(lado_interno, "*")
    #     cuadrados_negros += cuadrado_negro
    # print(cuadrados_negros)
    # for blancos in range(1, longitud, 2):
    #     print(generador_cuadrados(lado_interno, "+"))


def filas_tablero(longitud, flag):
    flag = 0
    cuadrado_interno = ""
    lado_interno = round(longitud / 2)
    for _ in range(longitud):
        # if _ % 2 == 0:
        if flag == 0:
            char = "*"
            cuadrado_interno += (char + "  ")*lado_interno
            # print(cuadrado_interno)
        else:
            char = " "
            cuadrado_interno += (char + "  ")*lado_interno
            # print(cuadrado_interno)
        if flag == 0:
            flag = 1
        else:
            flag = 0
    print(cuadrado_interno)


# def generador_cuadrados(lado_interno, char):
#     cuadrado_interno = ""
#     for _ in range(lado_interno):
#         cuadrado_interno += (char + "  ")*lado_interno + "\n"
#     return cuadrado_interno


# def generador_cuadrados_blancos(lado_interno):
#     cuadrado_interno = ""
#     for _ in range(lado_interno):
#         cuadrado_interno += "  +"*lado_interno + "\n"
#     return cuadrado_interno
