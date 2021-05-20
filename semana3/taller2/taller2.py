""" Programa calculadora artimética super amigable#
    Realiza las 4 operaciones (+,-,* /)
    dada como entrada una cadena de caracteres
    incorpora al modulo calculadora_aritmetica.py
    Thomas Ramirez Rozo
    Mayo 3-2021 """

# ---------------- Zona librerias------------
import calculadora_aritmetica as calc

# ======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

# ----------Definición de Funciones (Dividir)------------


def parser_cadena(cadena_entrada):
    """Esta función recibe una expresion matemática en forma de
    cadena de caracteres y la divide extrayendo los operandos y
    el operador

    Args:
        cadena_entrada (float): Expresión matemática en forma de cadena
        de caracteres

    Returns:
        num1 (float): Primer operando
        operador (string): Operador
        num2 (float): Segundo operando
    """

    # Divido la cadena de caracteres por el caracter espacio ' '
    num1, operador, num2 = cadena_entrada.split(" ")
    return float(num1), operador, float(num2)

# ======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

# ======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

def pedir_cadena():
    """Esta función pide una cadena de caracteres y la retorna

    Returns:
        cadena_entrada (str): cadena ingresada por el usuario
    """
    print("Ingrese la operación que desea realizar")
    cadena_entrada = input(">>> ")
    return cadena_entrada


def pedir_numero():
    """Esta función pide al usuario un número de punto flotante y lo retorna

    Returns:
        num {float}: Valor númerico de tipo float
    """
    num = float(input("Ingrese un operando por favor: "))
    return num


num1, operacion, num2 = parser_cadena(pedir_cadena())

# Realizo la operación dependiendo del tipo de operador
if operacion == "+":
    suma = calc.sumar_numeros(num1, num2)
    print(f" {num1} {operacion} {num2} = {suma}")
elif operacion == "-":
    resta = calc.restar_numeros(num1, num2)
    print(f" {num1} {operacion} {num2} = {resta}")
elif operacion == "*":
    multiplicacion = calc.multiplicar_numeros(num1, num2)
    print(f" {num1} {operacion} {num2} = {multiplicacion}")
else:
    # Repito hasta que el usuario ingrese un valor diferenre de cero
    while num2 == 0:
        print("Ingrese un valor diferente a cero para la division.")
        num2 = pedir_numero()
    division = calc.dividir_numeros(num1, num2)
    print(f" {num1} {operacion} {num2} = {division}")
