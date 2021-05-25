""" 
    Módulo encargado de verificar que el codódigo ingresado sea correcto.
    MisiónTIC 2022
    Thomas Ramírez Rozo
    Mayo 22-2021 
"""
    
## crear función para buscar el Codigo
def buscar_codigo(codigo):
    valor_boleano = True
    valor_boleano = valor_boleano and codigo[4].isdigit()
    if valor_boleano == True:
        if codigo[0].isupper():
            if codigo.find("@") != -1:
                if not codigo.find(" ") != -1:
                    chars = ["+", "=", "&"]
                    if any(item in codigo for item in chars):
                        return True
                    else:
                        print("Ha ingresado un código invalido.\nEl código no debe contener alguno de los siguientes caracteres: '+', '=', '&'.")
                        return False
                else:
                    print("Ha ingresado un código invalido.\nEl código no debe contener espacios.")
                    return False
            else:
                print("Ha ingresado un código invalido.\nEl código contener el caracter '@'.")
                return False
        else:
            print("Ha ingresado un código invalido.\nEl código debe iniciar con mayuscula.")
            return False
    else:
        return False
