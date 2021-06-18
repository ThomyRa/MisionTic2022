import matplotlib.pyplot as plt
import os


def graph_store_stock(sales_dict):
    my_path = os.getcwd()
    comics = list(sales_dict.keys())
    quants = list(sales_dict.values())
    
    quantities = [quants[_][0] for _ in range(len(list(sales_dict.values())))]
    plt.bar(comics, quantities)
    plt.ylabel("Cantidades")
    plt.title("Ventas del día")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(my_path + "/semana6/reto6/ventas_dia.jpg")
    plt.show()
    