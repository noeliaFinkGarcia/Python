# ****** SEMANA 5 ******
# *** TP 7 ***
#Cree un script para mostrar los primeros 100 n�meros enteros positivos,comenzando desde el 1.

from pickle import FALSE
from re import I
from tkinter import TRUE
import math


#for i in range(1,101,1) :
#    print (int(i))


 #Modifique el script del ejercicio anterior para que se muestren s�lo los n�meros pares. 
 #Para saber si un n�mero es par, utilice el operador de m�dulo (%).

#def es_par(numero):
#    par=FALSE
#    if(numero%2 == 0) :
#        par=TRUE
#        return par

#for i in range(1,101,1) :
#    if(es_par(i)) :
#        print (i)


#Cree un script para calcular el resultado de sumar los n�meros desde el 75 al 150.

#suma=0
#for i in range(75,151,1) :
#    suma+=i
#print (suma)
 

#Cree un script que le solicite al usuario ingresar un n�mero entero, y muestre
#en pantalla el factorial de dicho n�mero. NOTA: puede obviar la validaci�n en
#este ejercicio, pero recuerde que la funci�n range no incluye al valor m�ximo
#enviado como par�metro.
#factorial de n = n! = 1 * 2 * 3 * ... * (n - 1) * n


# Funci�n para calcular el factorial de un n�mero 

#def calcular_factorial(numero):
#    if numero == 1:
#        return 1
#    else:
#        factorial = numero * calcular_factorial(numero-1)
#        return factorial

## Solicitar un n�mero entero al usuario
#numero = int(input("Por favor, ingrese un numero entero: "))
#print("Vamos a calcular el factorial del numero ingresado")
#factorial = calcular_factorial(numero)
#print("El factorial de " + str(numero) + " es: "+ str(factorial))


#Cree un script que le solicite al usuario ingresar 10 n�meros enteros, y por cada uno, 
#informarle si el mismo es positivo, negativo, o cero.

#def pnc (numero):
#    if numero > 0 :
#        print ("El numero ingresado es positivo. \r\n")
#    elif numero < 0 :
#        print ("El numero ingresado es negativo. \r\n")
#    else :
#     print ( "El numero ingresado es cero. \r\n")



#for i in range (1,11) :
#    numero = int(input("Ingresa un numero, te digo si es positivo, negativo o cero. \r\n"))
#    str(pnc(numero))

#Cree un script que le solicite al usuario ingresar 10 n�meros, y una vez
#ingresados, le muestre en pantalla cu�l es el m�ximo, y en qu� posici�n lo
#ingres�. Por ejemplo, si el usuario ingresa los n�meros 2, 63, -3, 20, 55, 89, 7, 32, 9,
#y 33, se le deber�a mostrar el mensaje �El mayor n�mero ingresado es 89, y lo
#ingresaste en la posici�n 6�. NOTA: las posiciones posibles comienzan desde 1.

#numeros = []
#for i in range(10):
#    numero = int(input("Ingrese un numero: "))
#    numeros.append(numero)

#maximo = max(numeros)
#posicion = numeros.index(maximo) + 1

#print("El mayor numero ingresado es", maximo, "y lo ingresaste en la posicion", posicion)

#Extienda el script del ejercicio anterior para que tambi�n informe el n�mero m�nimo ingresado, y su posici�n.

#numeros = []
#for i in range(10):
#    numero = int(input("Ingrese un numero: "))
#    numeros.append(numero)

#maximo = max(numeros)
#posicion_maximo = numeros.index(maximo) + 1
#minimo = min(numeros)
#posicion_minimo = numeros.index(minimo) + 1

#print ("El mayor numero ingresado es ", str(maximo), "y lo ingresaste en la posicion ", str(posicion_maximo), "\r\n")
#print ("El mayor numero ingresado es ", str(minimo), "y lo ingresaste en la posicion ", str(posicion_minimo), "\r\n")


#Un cliente ha solicitado un programa que le permita ingresar los mililitros de
#lluvia ca�dos diariamente en una semana, para que el programa le informe en
#pantalla el promedio de precipitaci�n de esa semana. El cliente tambi�n desea
#saber cu�l fue el d�a en que m�s llovi� en la semana.
#A modo ilustrativo, un reporte generado por el programa deber�a verse como
#sigue, luego de haber le�do las precipitaciones de los 7 d�as de la semana:
#El promedio de precipitaciones fue de XX mls. diarios.
#El d�a de m�s precipitaciones fue el xxxxxx (nombre del d�a).
#Tenga en cuenta que la numeraci�n de los d�as de la semana comienza con el 1
#para el d�a domingo.
#Codifique el programa para dar soluci�n a lo solicitado por el cliente.


# Creamos una lista vac�a para almacenar las precipitaciones diarias
precipitaciones = []
dias_de_la_semana = ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']

# Pedimos al usuario que ingrese las precipitaciones de cada d�a de la semana
for i in range(7):
    precipitacion_diaria = float(input("Ingrese la precipitacion del dia : "))
    precipitaciones.append(precipitacion_diaria)

# Calculamos el promedio de precipitaciones
promedio = sum(precipitaciones) / len(precipitaciones)

# Buscamos el d�a con mayor precipitaci�n
dia_max_precipitacion = precipitaciones.index(max(precipitaciones)) 

# Mostramos los resultados

print("El promedio de precipitaciones fue de ",str(promedio), "  mls. diarios.")
print("El dia de mas precipitaciones fue el dia: ", dias_de_la_semana[dia_max_precipitacion])


