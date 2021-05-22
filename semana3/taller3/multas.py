""" Modulo Multas
    Funciones para el cálculo de multas
    de tránsito 
    Thomas J. Ramírez Rozo
    Mayo 21-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def multar_velocidad(vel):
    """Esta función calcula la velocidad de un vehicilo y determina
    si se le debe multar o no. En caso de multa por velocidad velocidad,
    retorna, verifica el grado de alcohol y devuelve la multa en sí y la
    sanción adicional dependiendo del grado de alcohol.

    Args:
        dist1 (float): Distancia uno.
        dist2 (float): Distancia dos.
        tiempo (float): Lapso de tiempo que tarda los haces de luz.
        grad_alco (float): Grado de alholemia del conductor.

    Returns:
        texto_multa (str), texto_alcolemia (str): Texto de la multa y la sanción
    """
    # Inicializo cadena vacia
    texto_alcolemia = ""
    # Evaluo el tipo de multa dependiendo de la velocidad
    if vel > 1 and vel <= 20:
        texto_multa = "Llamado de atención por baja velocidad."
    elif vel > 21 and vel <= 60:
        texto_multa = "Normal."
    elif vel > 61 and vel <= 80:
        texto_multa = "Llamado de atención por alta velocidad."
    elif vel > 81 and vel <= 120:
        texto_multa = "Multa tipo I."
        # Como hay exceso de velocidad llamo a la prueba de alcoholemia
        texto_alcolemia = multar_alcoholemia()
    else:
        texto_multa = "Multa tipo II e inmovilización del vehículo."
        # Como hay exceso de velocidad llamo a la prueba de alcoholemia
        texto_alcolemia = multar_alcoholemia()
    return texto_multa, texto_alcolemia


def multar_alcoholemia():
    """Esta función determina y retorna qué tipo de sanción adicional obtiene el conductor si conduce con exceso de velocidad dependiendo del grado de alcoholemia.

    Args:
        grad_alco (float): Cantidad de alcohol en la sangre mg de etanol/ml

    Returns:
        texto_alcoholemia (float): Sanción adicional dependiendo del grado de alcohol.
    """
    print("Debido a exceso de velocidad, se le practicará prueba de alcoholemia.")
    grad_alco = int(input("Ingrese el grado de alcoholemia: \n>>> "))
    # Retorno el tipo de sancion dependiendo del grado de alcoholemia.
    if grad_alco < 20:
        texto_alcoholemia = ""
    elif grad_alco >= 20 and grad_alco <= 39:
        texto_alcoholemia = "Además de las sanciones previstas en la presente ley, se decretará la suspensión de la licencia de conducción entre seis (6) y doce (12) meses."
    elif grad_alco >= 40 and grad_alco <= 99:
        texto_alcoholemia = "Adicionalmente a la sanción multa, se decretará la suspensión de la Licencia de Conducción entre uno (1) y tres (3) años."
    elif grad_alco >= 100 and grad_alco <= 149:
        texto_alcoholemia = "Adicionalmente a la sanción multa, se decretará la suspensión de la Licencia de Conducción entre tres (3) y cinco (5) años, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de cuarenta (40) horas."
    else:
        texto_alcoholemia = "Adicionalmente a la sanción de la sanción de multa, se decretará la suspensión entre cinco (5) y diez (10) años de la Licencia de Conducción, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de ochenta (80) horas."
    return texto_alcoholemia
