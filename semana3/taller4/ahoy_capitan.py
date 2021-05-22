""" Programa para apoyar al marinero Seijo
    MisiónTIC 2022
    Thomas Ramírez Rozo
    Mayo 22-2021 """

import utilidades as util
from arte import logo

def obtener_articulo(creatura):
    """Esta función retorna el articulo correspondiente al tipo de creatura que Seijo Alonso vea.

    Args:
        creatura (str): Creatura vista por Seijo

    Returns:
        articulo (str): Artículo corrspondiente al tipo de creatura.
    """
    if creatura == "Kraken":
        articulo = "un"
    elif creatura == "Sirenas":
        articulo = "unas"
    elif creatura == "Ballena":
        articulo = "una"
    elif creatura == "Hipocampo":
        articulo = "un"
    elif creatura == "Macaraprono":
        articulo = "una"
    elif creatura == "Pulpo":
        articulo = "un"
    elif creatura == "Leviatanes":
        articulo = "unos" 
    else:
        articulo = "unas"
    return articulo


def obtener_preposicion(direccion):
    """Esta función retorna la preposición correspondiente a la dirección por donde Seijo vea la creatura.

    Args:
        direccion (str): Dirección por donde Seijo io la creatura.

    Returns:
        preposición: Preposición que sirve para la primera oración con la dirección por donde aparece la creatura.
    """
    if direccion == "babor" or direccion == "estribor":
        preposicion = "a"
    else :
        preposicion = "por"
    return preposicion

# Imprimi el logo
print(logo)

# Obtengo la creatura
creatura = util.aparecer_criatura()
# Obtengo el artículo
articulo = obtener_articulo(creatura)
# Obtengo la dirección
direccion = util.aparecer_direccion()
# obtengo la preposición
preposicion = obtener_preposicion(direccion)

# Imprimo
print("\n")
print(f"Ahoy! capitan, {articulo} {creatura}, {preposicion} {direccion}!!")
