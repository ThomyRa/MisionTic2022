#Completar con la solución del reto
# importar modulos necesarios
# la función esta por completar en Verificador.py
import verificador as ver 

# Ejemplo de un código de Piso 1: Piso#1&

# funciones
def leer_codigo():
  codigo = input("Ingrese el código: ")
  #TODO: completar código
  se_encuentra = ver.buscar_codigo(codigo) #True si se encuentra el código  #TODO: completar código
  return se_encuentra, codigo

def cerca_mercado(codigo):
    if codigo[4] >= 3 and codigo[4] >= 5:
        return "si"
    return "no"
    
## Agregar variables de entrada
## Llamar funciones
## Imprimir salida

codigo_ok, codigo=leer_codigo()
print ("SE REALIZARA LA SIGUIENTE ENCUESTA")
if codigo_ok == True:
    cerca_supermerca = cerca_mercado(codigo)
    if cerca_supermerca == "si":
        pregunta = input("¿Esta usted cerca del supermercado [SI]/[NO]?\n>>> ").lower()
        if pregunta == 'si':
            input("¿Cual es el piso en el que se encuentra?:")
            compra_super = input("¿Ha hecho una compra en el supermercado [SI]/[NO]?\n>>> ").lower()
            compra_almacen=input("¿Ha hecho una compra en algun almacen [SI] [NO]?\n>>> ").lower()
        if compra_super == 'si' or compra_almacen == 'si':
            input ("¿Requiere conseguir transporte?")
        else:
            
        

