"""
    Reto semana 3 Fundamentos de Programación Grupo - 21
    Centro Comercial ASCII
    MisionTIC 2022
    Thomas Ramírez Rozo
    May 25 2021
"""
import verificador as ver 


def leer_codigo():
    """Esta función garantiza que el código enviado a la función buscar_codigo(), tenga 6 caracteres. Adicionalmente, llama a buscar_codigo() quien le devuelve True o False de pendiendo del codigo ingresado.

    Returns:
        se_encuentra (bool): Valor booleano que me indica si el codigo ingresado cumple o no con las restricciones.
        codigo (str): Código ingresado por el usuario.
    """
    codigo = input("Ingrese el código: ")
    while len(codigo) != 6:
        print("Ha ingresado un código no valido.\n>>> ")
        codigo = input("Ingrese un código de 6 caracteres alanuméricos.")
    se_encuentra = ver.buscar_codigo(codigo)
    return se_encuentra, codigo


def cerca_mercado(codigo):
    """Esta función determina si el usuario se encuentra cerca del super mercado (entre los pisos 3 y 5).

    Args:
        codigo (str): Código ingresado por el usuario.

    Returns:
        (str): Retorno 'si' si el usuario esta cerca, y 'no' si no.
    """
    if int(codigo[4]) >= 3 and int(codigo[4]) <= 5:
        return "si"
    return "no"


def lugar_parqueo():
    """Esta función recibe y garantiza que el usuario ingrese un valor válido para el lugar dónde se estacionó el usuario.

    Returns:
        parq_preferencial (str): Lugar de estacionamiento del vehículo del usuario.
    """
    parq_preferencial = input("Ingrese el lugar donde se estacionó en formato [Piso] / [Numero estacionamiento]\n>>> ")
    es_num_piso = parq_preferencial[0].isdigit()
    es_slash = parq_preferencial[1] == "/"
    es_num_parq = parq_preferencial[2:].isdigit()
    while (not es_num_piso) and (not es_slash) and (not es_num_parq):
        parq_preferencial = input("Ingrese nuevamente el lugar donde se estacionó en formato [Piso] / [Numero estacionamiento]\n>>>")
    return parq_preferencial


def esta_estacionado():
    """Esta suncipon le pregunta al usuario si se encuentra estacionado.

    Returns:
        estacionado (str): Cadena correspondiente a la respuesta del usuario.
    """
    estacionado = input("Está estacionado en parqueadero preferencial [Si]/[No]?\n>>> ").lower()
    return estacionado

# Leo código          
codigo_ok, codigo = leer_codigo()

# Repito hasta que el usuario ingrese un valor válido del código.
while codigo_ok != True:
    codigo_ok, codigo = leer_codigo()

# Empiezo encesta
print ("SE REALIZARÁ LA SIGUIENTE ENCUESTA")
cerca_supermerca = cerca_mercado(codigo)

esta_cerca_mercado = input("¿Esta usted cerca del supermercado [SI]/[NO]?\n>>> ").lower()
if esta_cerca_mercado == 'si':
    piso_usuario = input("¿Cual es el piso en el que se encuentra?:")
    while piso_usuario != codigo[4]:
        piso_usuario = input("El código que ingreso no coincide con el el piso en el que se encuentra.\nIngrese nuevamente el piso.\n>>> ")
compra_super = input("¿Ha hecho una compra en el supermercado [SI]/[NO]?\n>>> ").lower()
compra_almacen=input("¿Ha hecho una compra en algun almacen [SI]/[NO]?\n>>> ").lower()
# TODO
if compra_super == "si" or compra_almacen == "si":
    estacionado = esta_estacionado()
    if estacionado == "si":
        lugar_estacionamiento = lugar_parqueo()
        print("Por favor dirijase a la recepción para registrar la compra y el parqueadero.\nGracias por su visita, vuelva pronto.")
    else:
        transporte = input("¿Necesita ayuda para el transporte?\n>>> ").lower()
        if transporte == "si":
            print("En 5 minutos arrivará un taxi hacia aquí.")
        else:
            print("Muchas gracias por su visita, vuelva pronto.")
else:
    estacionado = esta_estacionado()
    if estacionado == "no":
        transporte = input("¿Necesita ayuda para el transporte? [Si]/[No]\n>>> ").lower()
        print("Tenemos excelentes descuentos en los almacenes y supermercado. Gracias por su visita.")
        print("Muchas gracias por su visita, vuelva pronto.")
    else:
        print("Tenemos excelentes descuentos en los almacenes y supermercado. Gracias por su visita.")
        print("Recuerde que por compras en nuestro centro comercial, se exonera el pago del parqueadero.")



