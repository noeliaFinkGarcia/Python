#Cree un script que le pida al usuario ingresar palabras, una a una, hasta que el
#usuario ingrese la palabra “parar”. A medida que se van ingresando las palabras,
#el programa simplemente debe mostrarlas en pantalla. Al detectar la palabra
#para detenerse, debe mostrar el mensaje “--- TERMINADO ---”.

from io import UnsupportedOperation
from operator import truediv
from pickle import TRUE
from tkinter import FALSE

#condicion_de_salida = TRUE
#clave = "parar"
#while condicion_de_salida :
#     palabra = input("Ingrese una palabra. \r\n")
#     if palabra == clave :
#         print ("---TERMINADO ---")
#         condicion_de_salida = FALSE
#     else : print(palabra.title())


#Cree un script que le solicite al usuario ingresar notas de parciales por teclado,
#hasta que el usuario ingrese el valor -1, indicando que ya no hay más notas para
#cargar. Una vez ingresadas las notas, el programa debe informar la nota
#promedio (tenga cuidado de no incluir al -1 dentro del promedio).

#contador = 0
#suma=0
#clave = -1
#condicion = TRUE

#while condicion :
#    nota = int(input("Ingrese nota. \r\n Ingrese -1 para terminar \r\n"))
#    if nota != clave :
#        suma+=nota
#        contador +=1
#    else : condicion = FALSE
#promedio = suma/contador
#print ("El promedio de las notas ingresadas es: ", str(promedio))


#Cree un script que le solicite al usuario leer un número entero entre 1 y 100. El
#programa debe ser capaz de solicitarle al usuario que reingrese el número
#cuantas veces sea necesario, hasta que el usuario provea un dato válido. Cada
#vez que detecte un error de validación, informele al usuario cuál fue el error, con
#los mensajes “El dato ingresado no es numérico.”, o “El número ingresado está
#fuera del rango permitido.”. Finalmente, cuando el usuario ingrese un dato
#válido, muestre el mensaje “[NÚMERO] es válido. Gracias!”.


condicion_de_salida = TRUE

while condicion_de_salida :
    numero = input("Ingrese un numero entero entre 1 y 100. \r\n")
    if not numero.isdigit() or int(numero) < 0 or int(numero)>100  :
        print ("El caracter ingresado no es numerico o esta fuera del rango especificado. Intente nuevamente\r\n")
    else : 
        print (numero, " es valido, Gracias!")
        condicion_de_salida = FALSE

        
