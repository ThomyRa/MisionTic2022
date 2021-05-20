""" Programa calculadora artimética amigable#
    Realiza las 4 operaciones (+,-,* /) 
    incorpora al modulo calculadora_aritmetica.py
    Oscar Franco-Bedoya
    Mayo 3-2021 """

#---------------- Zona librerias------------
import calculadora_aritmetica as calc

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def menu_operaciones():
  # print("==================================================")
  print(" Menu")
  # print("==================================================")
  print(" Ingresa un numero para realizar la operacion.")
  # print("==================================================")
  print(" 1. Calcular suma: [1]")
  # print("==================================================")
  print(" 2. Calcular la resta: [2]")
  # print("==================================================")
  print(" 3. Calcular multiplicación: [3]")
  # print("==================================================")
  print(" 4. Calcular dicvisión: [4]")
  # print("==================================================")
   
  opcion = input(">>> ")
  return opcion


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
operacion=menu_operaciones()

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

num1 = float(input("Ingrese primer operando: "))
num2 = float(input("Ingrese segundo operando: "))

if operacion == "1":
  suma = calc.sumar_numeros(num1, num2)
  print(suma)
elif operacion == "2":
  resta = calc.restar_numeros(num1, num2)
  print(resta)
elif operacion == "3":
  multiplicacion = calc.multiplicar_numeros(num1, num2)
  print(multiplicacion)
else:
  while num2 == 0:
    print("Ingresa un valoor diferente de cero para la division: ")
    num2 = float(input("Ingrese segundo operando: "))
  division = calc.dividir_numeros(num1, num2)
  print(division)