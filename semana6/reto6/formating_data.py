def max_len(store_dict):
    maximun_len = len(max(store_dict.keys(), key=len))
    return maximun_len


def show_full_store_dict(t_store_dict):
    
    product_len = max_len(t_store_dict)
    print("".ljust(product_len + 50, "="))
    print("El inventario de lienda es: ".center(product_len + 50))
    print("".ljust(product_len + 50, "="))
    
    print("Producto".ljust(product_len + 5, ".") + "Cantidad".rjust(15, ".") + "Precio".rjust(15, ".") + "Codido".rjust(15, "."))
    print("".ljust(product_len + 50, "="))  
    
    for store_key, store_value in t_store_dict.items():
        product = store_key
        quants = store_value["Cantidad"]
        price = "$" + str(store_value["Precio"])
        barcode = store_value["Codigo"]

        print(product.ljust(product_len + 5, ".") + str(quants).rjust(15, ".") + price.rjust(15, ".") + str(barcode).rjust(15, "."))
    print("".ljust(product_len + 50, "="))


def format_store_dictionary(t_store_dict):
    quants = [list(t_store_dict.values())[idx]["Cantidad"] for idx in range(len(list(t_store_dict.values())))]

    prices = [list(t_store_dict.values())[idx]["Precio"] for idx in range(len(list(t_store_dict.values())))]

    barcodes = [list(t_store_dict.values())[idx]["Codigo"] for idx in range(len(list(t_store_dict.values())))]

    attribute_list = list(zip(barcodes, quants, prices))

    t_formated_store_dict = [list(attribute_list[_]) for _ in range(len(attribute_list))]   

    store_dict = dict(zip(t_store_dict.keys(), t_formated_store_dict))
    return store_dict