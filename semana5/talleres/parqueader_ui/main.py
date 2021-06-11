import funciones_parqueadero as parq

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

# Ejemplo de funcionamiento

vehiculos_en_parqueadero = {}
memo_park = parq.crear_parqueadero(2, 4)

puesto_asignado = parq.ocupar_puesto_parqueadero("NAR-110", memo_park, vehiculos_en_parqueadero)
# puesto_asignado = parq.ocupar_puesto_parqueadero("EPM-765", memo_park, vehiculos_en_parqueadero)
# print("Puesto Asignado", puesto_asignado)
# puesto_asignado = parq.ocupar_puesto_parqueadero("MAL-543", memo_park, vehiculos_en_parqueadero)
# print("Puesto Asignado", puesto_asignado)
# puesto_asignado = parq.ocupar_puesto_parqueadero("XLC-113",memo_park, vehiculos_en_parqueadero)
# print("Puesto Asignado", puesto_asignado)
# parq.liberar_puesto_parqueadero("MAL-543", memo_park, vehiculos_en_parqueadero)
# puesto_asignado = parq.ocupar_puesto_parqueadero("EPN-554", memo_park, vehiculos_en_parqueadero)
# print("Puesto Asignado", puesto_asignado)