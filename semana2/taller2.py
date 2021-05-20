""" Taller 2.2 Espacios de Color #
    Thomas J. Ramírez Rozo
    Mayo 13 del 2021 """

# Definición de Funciones (Dividir)

# ======================================================================
#          E S P A C I O    P R E _ _ C O N F I G U R A D O
# =====================================================================


def convertir_yiq_a_rva(y, i, q):
    """ 
    Parameters
    ----------
    y,i,q:float
       valores del espacio de color YIQ
    Returns
    -------
    r,v,a:float
       valores del espacio de color RVA    
    """
    r = y+0.955*i+0.618*q
    v = y-0.271*i-0.645*q
    a = y-1.11*i+1.7*q

    return r, v, a
# -------------------------------------------


def convertir_yiq_a_ycbcr(y, i, q):
    """ 
    Parameters
    ----------
    y,i,q:float
       valores del espacio de color YIQ
    Returns
    -------
    y,cb,cr:float
       valores del espacio de color YCbCr
    """
    # Se hace aqui la conversión intermedia
    r = y + (0.955*i) + (0.618 * q)
    v = y - (0.271 * i) - (0.645 * q)
    a = y - (1.11 * i) + (1.7 * q)

    # Se hace aqui la conversión que se pide
    y = (0.299 * r) + (0.587 * v) + (0.114 * a)
    cb = (0.1687 * r) - (0.3313 * v) - (0.5 * a)
    cr = (0.5 * r) - (0.418 * v) + (0.0813 * a)

    return y, cb, cr
# ======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================


def convertir_rva_a_yiq(r, v, a):
    """Esta función calcula los planos rva del espacio de color YIQ a partir 
    de los valos del espacio de color rva

    Args:
        r (float): Plano r del espacio de color rva
        v (float): Plano v del espacio de color rva
        a (float): Plano a del espacio de color rva

    Returns:
        y, i, q (float): Valores de los planos de espacio de color YIQ
    """

    # Se hace aquí la conversión que se pide
    y = (0.596 * r) - (0.275 * v) - (0.321 * a)
    i = (0.212 * r) - (0.528 * v) + (0.311 * a)
    q = (0.299 * r) + (0.587 * v) + (0.114 * a)
    return y, i, q
# -------------------------------------------


def convertir_rva_a_ycbcr(r, v, a):
    """Esta función calcula los planos  del espacio de color YCbCr a partir 
    de los valos del espacio de color rva

    Args:
        r (float): Plano r del espacio de color rva
        v (float): Plano v del espacio de color rva
        a (float): Plano a del espacio de color rva

    Returns:
        y, Cb, Cr (float): Valor de kis planos del espacio de color YCbCr
    """
    # Se hace aquí la conversión que se pide
    y = (0.299 * r) + (0.587 * v) + (0.114 * a)
    cb = (0.1687 * r) - (0.3313 * v) - (0.5 * a)
    cr = (0.5 * r) - (0.418 * v) + (0.0813 * a)
    return y, cb, cr
# -------------------------------------------


def convertir_ycbcr_a_yiq(y, cb, cr):
    """Esta función calcula los planos del espacio de color YIQ a partir 
    de los valos del espacio de color YCbCr

    Args:
        y (float): Plano Y del espacio de color YCbCr
        cb (float): Plano Cb del espacio de color YCbCr
        cr (float): Plano Cr del espacio de color YCbCr

    Returns:
        y, i, q (float): Valor de kis planos del espacio de color YIQ
    """
    # Se hace la primera conversión aquí
    r = y + (1.402 * cr)
    v = y + (0.344 * cb) - (0.714 * cr)
    a = y + (1.772 * cb)

    # Se hace la segunda conversión aquí
    y = (0.596 * r) - (0.275 * v) - (0.321 * a)
    i = (0.212 * r) - (0.528 * v) + (0.311 * a)
    q = (0.299 * r) + (0.587 * v) + (0.114 * a)
    return y, i, q


def convertir_ycbcr_a_rva(y, cb, cr):
    """Esta función calcula rva planos del espacio de color rva a partir 
    de los valos del espacio de color YCbCr

    Args:
        y (float): Plano Y del espacio de color YCbCr
        cb (float): Plano Cb del espacio de color YCbCr
        cr (float): Plano Cr del espacio de color YCbCr

    Returns:
        r, v, a (float): Valor de kis planos del espacio de color rva
    """
    r = y + (1.402 * cr)
    v = y + (0.344 * cb) - (0.714 * cr)
    a = y + (1.772 * cb)
    return r, v, a


# ======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

# lectura espacio de color RVA
r = float(input("Digite el valor de r:"))
v = float(input("Digite el valor de v:"))
a = float(input("Digite el valor de a:"))


# lectura espacio de color YIQ
y = float(input("Digite el valor de Y:"))
i = float(input("Digite el valor de I:"))
q = float(input("Digite el valor de Q:"))

# lectura espacio de color YCbCr
y = float(input("Digite el valor de Y:"))
cb = float(input("Digite el valor de Cb:"))
cr = float(input("Digite el valor de Cr:"))


# Llamado/invocación de funciones

# Se utilizan otras variables para gurdar lo que retorna la funciòn
# para no cambiar el valor de las entradas por teclado

rt, vt, at = convertir_yiq_a_rva(y, i, q)
print("la conversión de YIQ a rva es", "r=", rt, "v=", vt, "a=", at)
yt, cbt, crt = convertir_yiq_a_ycbcr(y, i, q)
print("la conversión de YIQ a YCbCr es", "Y=", yt, "Cb=", cbt, "Cr=", crt)

# ======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================

# Llamo y asigno el valor que retorna la función convertir_rva_a_yiq
y_rva2YIQ, i_rva2YIQ, q_rva2YIQ = convertir_rva_a_yiq(y, cb, cr)
print("La conversión de rva a YIQ es", "Y=",
      y_rva2YIQ, "I=", i_rva2YIQ, "Q=", q_rva2YIQ)

# Llamo y asigno el valor que retorna la función convertir_rva_a_ycbcr
y_rva2YCbCr, cb_rva2YCbCr, cr_rva2YCbCr = convertir_rva_a_ycbcr(r, v, a)
print("La conversión de rva a YCbCr es", "Y=", y_rva2YCbCr,
      "Cb=", cb_rva2YCbCr, "Cr=", cr_rva2YCbCr)

# Llamo y asigno el valor que retorna la función convertir_ycbcr_a_yiq
y_YCbCr2YIQ, i_YCbCr2YIQ, q_YCbCr2YIQ = convertir_ycbcr_a_yiq(y, cb, cr)
print("La conversión de YCbCr a YIQ es", "Y=",
      y_YCbCr2YIQ, "I=", i_YCbCr2YIQ, "Q=", q_YCbCr2YIQ)

# Llamo y asigno el valor que retorna la función convertir_ycbcr_a_rva
r_YCbCr2rva, v_YCbCr2rva, a_YCbCr2rva = convertir_ycbcr_a_rva(y, cb, cr)
print("La conversión de YCbCr a rva es", "r=",
      r_YCbCr2rva, "v=", v_YCbCr2rva, "a=", a_YCbCr2rva)
