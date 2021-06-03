def show_lists(lista):
    """Imprime el nombre y las cantidades de los productos en formato amogable al humano

    Args:
        lista (list): Lista en formato [Nombre, cantidad]
    """
    print("".ljust(27, "="))
    for item in lista:
        print(str(item[0]).ljust(25,".") + str(item[1]).rjust(2))
    print("".ljust(27, "=")+"\n")


def quantity_checker(store_quants, user_quants):
    """Revisa la cantidad de productos en la tienda y los agrega a una lista en caso de encontrarlos.

    Args:
        store_quants (list): Lista tienda formato [Nombre, Cantidad]
        user_quants (list): Lista usuario formato nombre cantidfad

    Returns:
        [availible_articles (list): Lista de artículos disponibles en la tienda en formato [nombre, cantidad]
    """
    availible_articles = []
    for store_item in store_quants:
        for user_item in user_quants:
            if user_item[0] == store_item[0]:
                availible_articles.append(store_item)
    return availible_articles


def store_sale(store_quants, user_quants):
    """Realiza la venta si los productos en la tienda son mayores a los solicitados por el usuario, pero si la cantidad solitada es mayor a la cantidad en la tienda, se le vcende sólo las existencias. En ambos casos se actualiza el inventario de la tienda. 

    Args:
        store_quants (list): Lista de la tienda en formato [Nombre, Cantidad]
        user_quants (list): Lista del usuario en formato [Nombre, Cantidad]

    Returns:
        new_store_quants (list): Inventario actualizado de la tienda
        comics_sold (list): Lista de productos vendidos al usuario usada posteriormente en el reporte.
    """
    new_store_quants = store_quants.copy()
    comics_sold = []
    for i in range(len(store_quants)):
        for j in range(len(user_quants)):
            if store_quants[i][0] == user_quants[j][0]:
                stock_availible = store_quants[i][1]
                user_request = user_quants[j][1]
                diff = stock_availible - user_request
                if user_quants[j][1] >= store_quants[i][1]:
                    comics_sold.append([user_quants[j][0], store_quants[i][1]])
                    new_store_quants[i][1] = 0
                else:
                    new_store_quants[i][1] = diff
                    comics_sold.append([new_store_quants[i][0], user_quants[j][1]])
    return new_store_quants, comics_sold


def sales_store_report(store_stock):
    """Lista generada después de la venta con los valores del inventario actualizados del inventario. Si hay 1 o menos productos, imprime "Bajas Existencias"

    Args:
        store_stock ([type]): [description]

    Returns:
        [type]: [description]
    """
    sales_report = store_stock[:]
    for comic in range(len(store_stock)):
        if store_stock[comic][1] <= 1:
            sales_report[comic][1] = "Bajas existencias."
    return sales_report
