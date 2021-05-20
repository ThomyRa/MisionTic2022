""" Taller 2.3 Distancia mas corta #
    Thomas J. Ramírez Rozo
    Mayo 14 del 2021 """

# Definición de Funciones (Dividir)
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================
import math

def calcular_distancia_c1_a1(xc1,yc1,xa1,ya1):
    """Esta función calcula la distancia más corta entre dos puntos:
    las coordenadas del celular1 y la antena1

    Args:
        xc1 (float): coordenada x del celular1
        yc1 (float): coordenada y del celular1
        xa1 (float): coordenada x del antena1
        ya1 (float): coordenada y del antena1

    Returns:
        d_c1_a1 (float): Distancia más corta entre el celular1 y la antena1
    """
    # Calculamos la distancia a partir de las coordenadas 
    d_c1_a1 = math.sqrt((xa1 - xc1)**2 + (ya1 - yc1)**2)
    return d_c1_a1
#-------------------------------------------
def calcular_distancia_a1_ch(xa1,ya1,xch,ych):
    """Esta función calcula la distancia más corta entre dos puntos:
    las coordenadas del antena1 y la central1

    Args:
        xa1 (float): coordenada x de la antena1
        ya1 (float): coordenada y de la antena1
        xch (float): coordenada x de la centra holi
        ych (float): coordenada y de la centra holi

    Returns:
        d_a1_ch (float): Distancia más corta entre la antena1 y la central holi
    """
    # Calculamos la distancia a partir de las coordenadas 
    d_a1_ch = math.sqrt((xch - xa1)**2 + (ych - ya1)**2)
    return d_a1_ch
#-------------------------------------------
def calcular_distancia_ch_a2(xch,ych,xa2,ya2):
    """Esta función calcula la distancia más corta entre dos puntos:
    las coordenadas de la central holi y la antena2

    Args:
        xch (float): coordenada x central holi
        ych (float): coordenada y central holi
        xa2 (float): coordenada x antena 2
        ya2 (float): coordenada y antena 2

    Returns:
        d_ch_a2 (float): Distancia más corta entre la central holi y la antena2
    """
    # Calculamos la distancia a partir de las coordenadas
    d_ch_a2 = math.sqrt((xa2 - xch)**2 + (ya2 - ych)**2)
    return d_ch_a2
#-------------------------------------------
def calcular_distancia_a2_c2(xa2,ya2,xc2,yc2):
    """Esta función calcula la distancia más corta entre dos puntos:
    las coordenadas de la antena2 y el celular2

    Args:
        xa2 (float): Coordenada x de la antena2
        ya2 (float): Coordenada y de la antena2
        xc2 (float): Coordenada x del celular2
        yc2 (float): Coordenada y del celular2

    Returns:
        d_a2_c2 (float): Distrancia más corta entre la antena2 y el celular2
    """
    # Calculamos la distancia a partir de las coordenadas
    d_a2_c2 = math.sqrt((xc2 - xa2)**2 + (yc2 - ya2)**2)
    return d_a2_c2
#-------------------------------------------
def obtener_distancia_total (d1,d2,d3,d4):
    """Esta función suma todas las distancias obtenidas para obtener la distancia total.

    Args:
        d1 (float): Distancia más corta entre el celular1 y la antena1
        d2 (float): Distancia más corta entre el antena1 y la cebtral holi
        d3 (float): Distancia más corta entre central holi y la antena2
        d4 (float): Distancia más corta entre el antena2 y la celular2

    Returns:
        total_dist (float): Suma de cada una de las distancias
    """
    # Calculo la suma de las distancias
    total_dist = d1 + d2 + d3 + d4
    return total_dist

#======================================================================
#          E S P A C I O    P R E _ _ C O N F I G U R A D O
# =====================================================================

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
#lectura coordenadas celular 1
#TODO: instrucciones
cel1_cx = float(input("Ingrese coordenada X para el celular 1: "))
cel1_cy = float(input("Ingrese coordenada Y para el celular 1: "))
#lectura coordenadas antena 1
#TODO: instrucciones
antena1_cx = float(input("Ingrese coordenada X para la antena 1: "))
anetna1_cy = float(input("Ingrese coordenada Y para la antena 1: "))
#lectura coordenadas central holi 
#TODO: instrucciones
central_holiu_cx = float(input("Ingrese coordenada X para La central Holi: "))
central_holiu_cy = float(input("Ingrese coordenada Y para La central Holi: "))
#lectura coordenadas antena 2
#TODO: instrucciones
antena2_cx = float(input("Ingrese coordenada X para la antena 2: "))
antena2_cy = float(input("Ingrese coordenada Y para la antena 2: "))
#lectura coordenadas celular 1
#TODO: una vez haga os puntos anteriores quite el simbolo de comentarios
# y organice la identación
cel2_cx = float(input("Ingrese coordenada X para el celular 2: "))
cel2_cy = float(input("Ingrese coordenada Y para el celular 2: "))

d1=calcular_distancia_c1_a1(cel1_cx,cel1_cy,antena1_cx,anetna1_cy)
d2=calcular_distancia_a1_ch(antena1_cx,anetna1_cy,central_holiu_cx,central_holiu_cy)
d3=calcular_distancia_ch_a2(central_holiu_cx,central_holiu_cy,antena2_cx,antena2_cy)
d4=calcular_distancia_a2_c2(antena2_cx,antena2_cy,cel2_cx,cel2_cy)

distancia_total=obtener_distancia_total (d1,d2,d3,d4)
print("La distancia otal es",distancia_total)


