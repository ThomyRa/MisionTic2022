# Diseño de sistema
La función que se plantea, tiene como objetivo realizar un sistema que permita el
desplazamiento de los usuarios en el centro comercial, para los diferentes niveles por
medio de un elevador, que al oprimir un botón el sistema identifique y tenga en cuenta
que cada piso contiene un Código (cadena de caracteres) de identificación. Este Código es
una cadena de 6 caracteres que debe cumplir con las siguientes restricciones y las cuales
deben ser validadas por la aplicación:

• Se debe verificar que el Código sea de tipo str.
• En la posición 4 de la cadena Código debe ir siempre el carácter con el número del
piso.
• El carácter en la primera posición del Código debe ser Letra en mayúscula.
• El Código debe contener en cualquier posición de la cadena el carácter arroba (‘#’)
• El Código no debe contener ningún espacio.
• El Código debe tener al menos uno de los siguientes símbolos (‘+’,’=’,’&’)