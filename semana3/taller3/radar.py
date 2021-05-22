""" Programa Apoyo multas#
    incorpora al modulo multas.py
    Thomas Ramirez Rozo
    Mayo 21-2021 """

#---------------- Zona librerias------------
import multas as mult
from arte import logo
import textwrap


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación
# =====================================================================
# Imprimo el logo de la parte superior
def calcular_vel():
    print(logo)
    # pido los datos del problema
    dist1 = float(input("Ingrese la distancia 1: \n>>> "))
    dist2 = float(input("Ingrese la distancia 2: \n>>> "))
    tiempo = float(input("Ingrese el tiempo:  \n>>> "))
        # Calculo velocidad
    vel = abs(dist1 - dist2) / tiempo
    return round(vel, 2)


def imprimir_velocidad(velocidad):
    print("".center(80, "="))
    print(f"Su velocidad es de: ".ljust(80 - len(str(velocidad)) - 2 - 5, ">") + "  " f"{vel} km/h".rjust(len(str(velocidad))))
    print("".center(80, "="))


vel = calcular_vel()
imprimir_velocidad(vel)

# Llamo la función multar_velocidad
txt_multa, txt_alco = mult.multar_velocidad(vel)

# Imprimo el resultado de evaluar la velocidad y el grado de alcoholemia
print("".center(80, "="))
print(txt_multa.center(80))
print("".center(80, "="))
for _ in textwrap.wrap(txt_alco, width=80):
    print(_)
print("".center(80, "="))