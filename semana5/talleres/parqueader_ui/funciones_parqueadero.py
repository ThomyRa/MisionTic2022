from collections import namedtuple
import stack_puestos as stack
import typing

Puesto = namedtuple('Puesto','nivel numero')


def crear_parqueadero(numero_niveles,cantidad_puestos):
  parqueadero=stack.Stack()
  cont_niveles=1
  while cont_niveles <= numero_niveles:
    cont_vehiculos=1
    while cont_vehiculos <= cantidad_puestos:
      parqueadero.push(Puesto(cont_niveles,cont_vehiculos))
      cont_vehiculos+=1
    cont_niveles+=1
  return parqueadero

def obtener_puesto_libre(parqueadero):
  puesto= parqueadero.top()
  parqueadero.pop()
  return puesto

def ingresar_puesto_libre(parqueadero,puesto):
  parqueadero.push(puesto)

  


def ocupar_puesto_parqueadero(placa,parqueadero,vehiculos_en_parqueadero): 
  if vehiculos_en_parqueadero.get(placa)==None:
    puesto_libre=obtener_puesto_libre(parqueadero)
    vehiculos_en_parqueadero[placa]=puesto_libre
    return placa,puesto_libre
  else:
    return None

def liberar_puesto_parqueadero(placa,parqueadero,vehiculos_en_parqueadero):
  if vehiculos_en_parqueadero.get(placa)!=None:
    puesto_libre=vehiculos_en_parqueadero[placa]
    del vehiculos_en_parqueadero[placa]
    ingresar_puesto_libre(parqueadero,puesto_libre)

vehiculos_en_parqueadero=typing.Dict[str, str]