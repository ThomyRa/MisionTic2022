""" Programa IoT#
    Realiza lel calculo de estadisticas de Una 
    Smarth Home
    incorpora al modulo smarth_home.py
    Thomas Ramírez Rozo
    Junio 4-2021 """

from collections import namedtuple
from pprint import pprint


def string_splitter(smart_home_report):
    """ 
    Parameters
    ----------
  lista_datos:string
      Una cadena con los datos de todos los IoT de una smarth-home 
    Returns
    -------
    lista_IoT:[(namedtuple)]
      una lista de tuplas cada una de ellas con los datos de un dispositivo IoT     
    """  
    devices_list = smart_home_report.split("@")
    del(devices_list[-1])
    return devices_list


def calcular_estadisticas(lista_IoT):
    """ 
    Parameters
    ----------
  lista_IoT:[(namedtuple)]
      Una lista de tuplas con los datos de los dispositivos IoT 
    Returns
    -------
    estadistica:(total_on, total_off)
      una tupla con  el total de dispositivos IoT en estado ON y otra con el total de estado     
    """
    # Instancio la namedtuple
    Device = namedtuple("Device", "type id state")

    # Obtengo los valores de la tupla a partir de la lista dividida para cada dispositivo
    namedtuples_values = [item.split(",") for item in lista_IoT]

    # Guardo los valores de cada deispositivo en una named tuple para cuantificar los que están en ON y en OFF
    on_devices = []
    on_count = 0
    off_devices = []
    off_count = 0
    for each_namedtuple in namedtuples_values:
        device = Device._make(each_namedtuple)
        if device.state == "ON":
            on_devices.append(device)
            on_count += 1
        else:
            off_devices.append(device)
            off_count += 1

    print("Los dispositivos en ON son:")
    
    pprint(on_devices)
    print("\n")
    print("Los dispositivos en OFF son:")
    pprint(off_devices)
