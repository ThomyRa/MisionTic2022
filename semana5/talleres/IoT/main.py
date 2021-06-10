""" Programa IoT#
    Realiza lel calculo de estadisticas de Una 
    Smarth Home
    incorpora al modulo smarth_home.py
    Thomas Ramírez Rozo
    Junio 4-2021 """

#---------------- Zona librerias------------
from collections import namedtuple
import smart_home as sh
import random


def string_generator():
    device_type = random.choice(list(device.keys()))
    device_id = random.choice(device[device_type])
    device_state = random.choice(state) 
    string_report = device_type + "," + device_id + "," + device_state + "@"
    return string_report


def string_report():
    num_devices = int(input("Cuantos dispositivos tiene el smart home?\n>>> "))
    count = 0
    smart_home_report = ""
    while count <= num_devices - 1:
        smart_home_report += string_generator()
        count += 1
    return smart_home_report


device = {"electricos": ["luces", "tomas"], "sensor": ["humedad", "temperatura"], "alarma": ["movimiento", "apertura"]}

state = ["ON", "OFF"]

smart_home_report = string_report()
devices_list = sh.string_splitter(smart_home_report)

sh.calcular_estadisticas(devices_list)