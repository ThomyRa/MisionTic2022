#Completar con la solución del reto
# importar modulos necesarios
# la función esta por completar en Verificador.py
import verificador as ver 

# Ejemplo de un código de Piso 1: Piso#1&

# funciones
def leer_codigo():
  codigo = input("Ingrese el código: ")
  while len(codigo) != 6:
      print("Ha ingresado un código no valido.\n>>> ")
      codigo = input("Ingrese un código de 6 caracteres alanuméricos.")
  se_encuentra = ver.buscar_codigo(codigo)
  return se_encuentra, codigo

def cerca_mercado(codigo):
    if int(codigo[4]) >= 3 and int(codigo[4]) <= 5:
        return "si"
    return "no"


def lugar_parqueo():
    parq_preferencial = input("Ingrese el lugar donde se estacionó en formato [Piso] / [Numero estacionamiento]\n>>> ")
    es_num_piso = parq_preferencial[0].isdigit()
    es_slash = parq_preferencial[1] == "/"
    es_num_parq = parq_preferencial[2:].isdigit()
    while (not es_num_piso) and (not es_slash) and (not es_num_parq):
        parq_preferencial = input("Ingrese nuevamente el lugar donde se estacionó en formato [Piso] / [Numero estacionamiento]\n>>>")
    return parq_preferencial


def esta_estacionado():
    estacionado = input("Está estacionado en parqueadero preferencial [Si]/[No]?\n>>> ").lower()
    return estacionado

          
codigo_ok, codigo = leer_codigo()
while codigo_ok != True:
    codigo_ok, codigo = leer_codigo()

print ("SE REALIZARÁ LA SIGUIENTE ENCUESTA")
cerca_supermerca = cerca_mercado(codigo)
if cerca_supermerca == "si":
    esta_cerca_mercado = input("¿Esta usted cerca del supermercado [SI]/[NO]?\n>>> ").lower()
    if esta_cerca_mercado == 'si':
        piso_usuario = input("¿Cual es el piso en el que se encuentra?:")
        while piso_usuario != codigo[4]:
            piso_usuario = input("El código que ingreso no coincide con el el piso en el que se encuentra.\nIngrese nuevamente el piso.\n>>> ")
        compra_super = input("¿Ha hecho una compra en el supermercado [SI]/[NO]?\n>>> ").lower()
        compra_almacen=input("¿Ha hecho una compra en algun almacen [SI]/ [NO]?\n>>> ").lower()
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
            print("Tenemos excelentes descuentos en los almacenes y supermercado. Gracias por su visita.")
            print("¿Necesita ayuda para el transporte?\n Muchas gracias por su visita, vuelva pronto.")
        else:
            print("Tenemos excelentes descuentos en los almacenes y supermercado. Gracias por su visita.")
            print("Recuerde que por compras en nuestro centro comercial, se exonera el pago del parqueadero.")

    

