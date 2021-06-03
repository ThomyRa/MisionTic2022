# Método IDEAL: Disponibilidad de prodictos.

## Análisis - Identificar el problema

### ¿Cuál es el problema?

Gestionar el inventario de la tienda para facilitar el proceso de pedido con antelación.

### ¿Quienes son los interesados?

#### Cliente: 

La tienda

#### Usuario:

El administrador de la tienda

### ¿Cúal es el objetivo que se busca?

Gestionar de manera fácil el proceso de compra y venta de productos de una tienda de cara a el acaecimiento el abastecimiento en caso de escases de productos.

### ¿Existen restricciones?

Notificar a los usuarios en caso de no haber existencias y reportar las bajas existencias al administrador.

## Definir el problema

### ¿Qué información conozco (Qué nos dan)?

* Por cada producto de la tienda, tengo:
  * Número de identificación.
  * Código de barras.
  * Nombre del producto.
  * Cantidad Disponible.
  * Valor unitario.
* Para cada usuario tengo el artículo que desea comprar y su cantidad.

### ¿Qué información debo conocer para lograr el objetivo?

* Las cantidades y existencias de los productos luego de realizar la venta.
* Las cantidades y existencias de los productos en el inventario de la tienda.
* El registro de artículos vendidos a los usuarios.
  

### Dividir el problema en sub-problemas

* Obtener la lista con los nombres de los articulos y sus respectivas cantidades para la tienda y para los usuarios.
* Encontrar los articulos solicitados por el usuario.
* Revisar la cantidad disponible de productos para la venta.
* Realizar la venta teniendo en cuenta los artículos disponibles y la cantidad solicitada por los usuarios.
* Generar el reporte luego de la venta.

## Estrategia

### Ejemplos particulares

Realizar operaciones con listas, manejo de ciclos para recorrerlas y búsqueda de elementos.

### Proponer una estrategia

Tomamos la lista del usuario y convertimos los id's a nombres, esto para trabajar mejor las transacciones de la tienda y sus existencias.
A partir del inventario de la tienda, realizar la resta de productos teniendo en cuenta que si no hay existencias, no se puede vender nada, sólo se puede vender  las existencias del inventario, es decir, no se puede vender más de lo que uno tiene y realizar la venta normalmente en caso de tener más productos en inventario que la cantidad pedida por el usuario.

![Imagen Método Ideal](https://i.ibb.co/CKwn0N3/metodo-ideal.jpg)

## Algoritmo

![Algoritmo](https://i.ibb.co/PzvHY3p/algoritmo.jpg)