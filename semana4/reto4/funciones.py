# funciones 
# función para realizar busqueda de que artículos venden en la tienda. 
# ingresar la lista de tienda y lista de cliente, solo con los nombre de los productos.
def buscar_articulo(Lista_tienda,Lista_cliente):
  """
  Agregar comentarios
  """
  lista_buscar  = []    
  for productos_cliente in Lista_cliente:
    indicador = False
    for productos in Lista_tienda:
      if productos == productos_cliente:
        indicador = True
        break
    lista_buscar.append(indicador)
  return lista_buscar

# función para realizar verificación de la cantidad del producto disponible.
# ingresar Lista de tienda y lista de cliente en estructura de lista de listas.
# [["Nombre a",cantidad],["Nombre b", cantidad]]
def verificar_cantidad(Lista_tienda_articulos,Lista_cliente):
  """
  Agregar comentarios
  """
  Lista_cantidad = []
  Lista_disponible = []
  for index1 in range(len(Lista_cliente)):
    for index2 in range(len(Lista_tienda_articulos)):
      if Lista_tienda_articulos[index2] == Lista_cliente[index1]:
        cantidad_tienda     = Lista_tienda_articulos[index2][1]
        cantidad_solicitado = Lista_cliente[index1][1]
        if  cantidad_tienda == 0:
          Lista_cantidad.append("producto sin existencias")
        elif cantidad_tienda >= cantidad_solicitado:
          cantidad_tienda   = cantidad_tienda - cantidad_solicitado
          Lista_disponible.append(cantidad_solicitado)
          Lista_tienda_articulos[index2][1] = cantidad_tienda
        else:
          Lista_cantidad.append("producto con pocas existencias")
          Lista_disponible.appens(cantidad_tienda)

  return Lista_cantidad,Lista_disponible,Lista_tienda_articulos

# función para visualizar la cantidad de artículos en total tiene el establecimiento.
# ingresar Lista de tienda en estructura de lista de listas
# [["Nombre a",cantidad],["Nombre b", cantidad]]
def cantidad_total(Lista_tienda):
  """
  Agregar comentarios
  """
  for index1 in range(len(Lista_tienda)):
    print("Articulo {art}, Cantidad {cant}".format(art=Lista_tienda[index1][0],cant=Lista_tienda[index1][1]))

# imprimir artículos en una lista solicitados.
# ingresar la lista de cliente, solo con los nombre de los productos.
def imprimir_productos(Lista_cliente):
  """
  Agregar comentarios
  """
  for producto in Lista_cliente:
    print(producto)

# Función para presentar la venta realizada al usuario.
def Venta_usuario():
  """
  Agregar comentarios
  """
  return