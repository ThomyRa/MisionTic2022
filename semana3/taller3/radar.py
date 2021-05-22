""" Programa Apoyo multas#
    incorpora al modulo multas.py
    Oscar Franco-Bedoya
    Mayo 3-2021 """

#---------------- Zona librerias------------
import multas as mult
from arte import logo
import textwrap


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación
# =====================================================================
# Imprimo el logo de la parte superior
print(logo)
# pido los datos del problema
dist1 = float(input("Ingrese la distancia 1: \n>>> "))
dist2 = float(input("Ingrese la distancia 2: \n>>> "))
tiempo = float(input("Ingrese el tiempo:  \n>>> "))
grad_alco = float(input("Ingrese el grado de alcoholemia: \n>>> "))
# Llamo la función multar_velocidad
txt_multa, txt_alco = mult.multar_velocidad(dist1, dist2, tiempo, grad_alco)
# Imprimo el resultado de evaluar la velocidad y el grado de alcoholemia
print("".center(80, "="))
print(txt_multa.center(80))
print("".center(80, "="))
for _ in textwrap.wrap(txt_alco, width=80):
    print(_)
print("".center(80, "="))