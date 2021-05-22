""" Programa para apoyar al marinero Seijo
    MisiónTIC 2022
    Thomas Ramírez Rozo
    Mayo 22-2021 """
    
## crear función para buscar el Codigo
def buscar_codigo(codigo):
    valor_boleano = True
    valor_boleano = valor_boleano and codigo[4].isdigit()
    if valor_boleano == True:
        if codigo[0].isupper():
            if codigo.find("@") != -1:
                if not codigo.find(" ") != -1:
                    if "+" in codigo or "=" in codigo or "&" in codigo:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
