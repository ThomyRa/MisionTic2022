# # Taller 01 Semana 02: Hola Mundo
#   ## Objetivo
#   Familiarizarse con el entorno de desarrollo Repl.it realizando una serie de ejercicios básicos utilizando la instrucción *print*

#   Estos ejercicios deben ser realizados en el archivo main.py
  
#   ### Ejercicio 1: Mis datos personales
# Construir un programa que muestre en pantalla sus datos personales uno en cada línea (nombre apellidos, dirección, teléfono, barrio, ciudad)

#   ### Ejercicio 2: C-3PO
#   El robot R2D2 siempre esta con su amigo C-3PO, debemos hacer un programa que dibuje en pantalla a este personaje 

# ![alt text](https://raw.githubusercontent.com/oscarhf/Materiales_de_apoyo/master/C3.png)

def presentar_datos_personales():
    print("Thomas")
    print("Ramirez Rozo")
    print("Avenida Simepre Viva 123")
    print("123456789")
    print("Barrio")
    print("Ciudad")
    

def dibujar_C_3_PO():    
    print("    / ~ \   ")
    print("   | o o )  ")
    print("    \ = /   ")
    print("   --   --   ")
    print(" /     -   \ ")
    print("/ /|/ . \|\ \ ") 
    print("\ \ \ _ / | |")
    print(" \ |\ _ / | |")
    print("  # _   _/ #")
    print("   |  |  |")
    print("   |  |  |")
    print("   [  ][ ]")
    print("   |  |  |")
    print("  /   ][  \ ")
    
    
def iniciar_aplicación():
    presentar_datos_personales()
    dibujar_C_3_PO()
    
iniciar_aplicación()    