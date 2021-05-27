""" Modulo Ciclos
    Funciones para practicas con ciclos
    Thomas Ramírez Rozo
    Mayo 26-2021 """

# Definición de Funciones

def simulador_caida_libre(altura):
    g = 9.8
    t = 1
    distancias = [0,]
    dist = (1/2) * g * (t ** 2)
    while altura > dist:
        dist = round((1/2) * g * (t ** 2))
        t += 1
        dist_cercana = min(distancias, key=lambda _:abs(_-altura))
        print(f"La distancia al suelo transcurridos {t} segundos son: {dist_cercana}m ")
        distancias.append(dist)
    

def generador_generaciones(generacion):
    num_personas = 2 ** generacion
    for idx in range(0, generacion):
        personas = 2 ** idx
        print(f"Generación: {idx}   Personas: {personas}".ljust(num_personas + 4, " ") + ("*"*personas).center(num_personas, " "))
        # print(("*"*personas).center(num_personas, " "))
  
    
    
  
  
# def constructor_triangulos(pisos):
#   #TODO Comentar código
#   #TODO Implementar la función
#   return "No implementada aún"

# def constructor_tableros(longitud):
#   #TODO Comentar código
#   #TODO Implementar la función
#   return "No implementada aún"