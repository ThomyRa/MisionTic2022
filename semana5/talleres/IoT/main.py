""" Programa IoT#
    Realiza lel calculo de estadisticas de Una 
    Smarth Home
    incorpora al modulo smarth_home.py
    Thomas Ramírez Rozo
    Junio 4-2021 """

#---------------- Zona librerias------------
import smart_home as sh
import random

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

#======================================================================

#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

dispositivos = {"electricos": ["luces", "tomas"], "sensor": ["humedad", "temperatura"], "alarma": ["movimiento", "apertura"]}

tipo_dispositivo = random.choice(list(dispositivos.keys()))
id_dispositivo = random.choice(dispositivos[tipo_dispositivo])

print(tipo_dispositivo + "  " + id_dispositivo)