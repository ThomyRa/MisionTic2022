""" Modulo Multas
    Funciones para el cálculo de multas
    de tránsito 
    Thomas J. Ramírez Rozo
    Mayo 21-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def multar_velocidad(dist1, dist2, tiempo, grad_alco):
  #TODO: Documentar función 
  texto_alcolemia = ""
  #TODO: Implementar función
  vel = abs(dist1 - dist2) / tiempo
  
  if vel > 1 and vel <= 20:
      texto_multa = "Llamado de atención por baja velocidad."
  elif vel > 21 and vel <= 60:
      texto_multa = "Normal."
  elif vel > 61 and vel <= 80:
      texto_multa = "Llamado de atención por alta velocidad."
  elif vel > 81 and vel <= 120:
      texto_multa = "Multa tipo I."
      texto_alcolemia = multar_alcoholemia(grad_alco)
  else:
      texto_multa = "Multa tipo II e inmovilización del vehículo."
      texto_alcolemia = multar_alcoholemia(grad_alco)
  return texto_multa, texto_alcolemia

def multar_alcoholemia(grad_alco):
#TODO: Documentar función 
  texto_alcoholemia=""
  #TODO: Implementar función
  if grad_alco > 20 and grad_alco <= 39:
      texto_alcoholemia = "Además de las sanciones previstas en la presente ley, se decretará la suspensión de la licencia de conducción entre seis (6) y doce (12) meses."
  elif grad_alco > 40 and grad_alco <= 99:
      texto_alcoholemia = "Adicionalmente a la sanción multa, se decretará la suspensión de la Licencia de Conducción entre uno (1) y tres (3) años."
  elif grad_alco > 100 and grad_alco <= 149:
      texto_alcoholemia = "Adicionalmente a la sanción multa, se decretará la suspensión de la Licencia de Conducción entre tres (3) y cinco (5) años, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de cuarenta (40) horas."
  else:
      texto_alcoholemia = "Adicionalmente a la sanción de la sanción de multa, se decretará la suspensión entre cinco (5) y diez (10) años de la Licencia de Conducción, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de ochenta (80) horas."
  return texto_alcoholemia


