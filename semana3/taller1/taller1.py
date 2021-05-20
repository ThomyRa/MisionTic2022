""" Programa calculadora artimética amigable#
    Realiza las 4 operaciones (+,-,* /) 
    incorpora al modulo calculadora_aritmetica.py
    Thomas Ramirez Rozo
    Mayo 3-2021 """

# ---------------- Zona librerias------------
import calculadora_aritmetica as calc

# ======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

# ----------Definición de Funciones (Dividir)------------


def menu_operaciones():
    print(" Menu")
    print(" Ingresa un numero para realizar la operacion.")
    print(" 1. Calcular suma: [1]")
    print(" 2. Calcular la resta: [2]")
    print(" 3. Calcular multiplicación: [3]")
    print(" 4. Calcular división: [4]")

    opcion = input(">>> ")
    return opcion


# ======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
operacion = menu_operaciones()

# ======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================


def pedir_numero():
    """Esta función pide al usuario un número de punto flotante y lo retorna

    Returns:
        num {float}: Valor númerico de tipo float
    """
    num = float(input("Ingrese un operando por favor: "))
    return num

# Pido al usuario los numeros
num1 = pedir_numero()
num2 = pedir_numero()

# Realizo la operación dependiendo de la opción ingresada por el usuario
if operacion == "1":
    suma = calc.sumar_numeros(num1, num2)
    print(f"La suma es: {suma}")
elif operacion == "2":
    resta = calc.restar_numeros(num1, num2)
    print(f"La resta es: {resta}")
elif operacion == "3":
    multiplicacion = calc.multiplicar_numeros(num1, num2)
    print(f"La multiplicacion es: {multiplicacion}")
else:
    # Repito hasta que el usuario ingrese un valor diferenre de cero
    while num2 == 0:
        print("Ingrese un valor diferente a cero para la division.")
        num2 = pedir_numero()
    division = calc.dividir_numeros(num1, num2)
    print(f"La division es: {division}")
