# ****** SEMANA 5 ******
# *** TP 7 ***
#Cree un script para mostrar los primeros 100 números enteros positivos,comenzando desde el 1.

from pickle import FALSE
from re import I
from tkinter import TRUE
import math


#for i in range(1,101,1) :
#    print (int(i))


 #Modifique el script del ejercicio anterior para que se muestren sólo los números pares. 
 #Para saber si un número es par, utilice el operador de módulo (%).

#def es_par(numero):
#    par=FALSE
#    if(numero%2 == 0) :
#        par=TRUE
#        return par

#for i in range(1,101,1) :
#    if(es_par(i)) :
#        print (i)


#Cree un script para calcular el resultado de sumar los números desde el 75 al 150.

#suma=0
#for i in range(75,151,1) :
#    suma+=i
#print (suma)
 

#Cree un script que le solicite al usuario ingresar un número entero, y muestre
#en pantalla el factorial de dicho número. NOTA: puede obviar la validación en
#este ejercicio, pero recuerde que la función range no incluye al valor máximo
#enviado como parámetro.
#factorial de n = n! = 1 * 2 * 3 * ... * (n - 1) * n


# Función para calcular el factorial de un número 

#def calcular_factorial(numero):
#    if numero == 1:
#        return 1
#    else:
#        factorial = numero * calcular_factorial(numero-1)
#        return factorial

## Solicitar un número entero al usuario
#numero = int(input("Por favor, ingrese un numero entero: "))
#print("Vamos a calcular el factorial del numero ingresado")
#factorial = calcular_factorial(numero)
#print("El factorial de " + str(numero) + " es: "+ str(factorial))


#Cree un script que le solicite al usuario ingresar 10 números enteros, y por cada uno, 
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

#Cree un script que le solicite al usuario ingresar 10 números, y una vez
#ingresados, le muestre en pantalla cuál es el máximo, y en qué posición lo
#ingresó. Por ejemplo, si el usuario ingresa los números 2, 63, -3, 20, 55, 89, 7, 32, 9,
#y 33, se le debería mostrar el mensaje “El mayor número ingresado es 89, y lo
#ingresaste en la posición 6”. NOTA: las posiciones posibles comienzan desde 1.

#numeros = []
#for i in range(10):
#    numero = int(input("Ingrese un numero: "))
#    numeros.append(numero)

#maximo = max(numeros)
#posicion = numeros.index(maximo) + 1

#print("El mayor numero ingresado es", maximo, "y lo ingresaste en la posicion", posicion)

#Extienda el script del ejercicio anterior para que también informe el número mínimo ingresado, y su posición.

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
#lluvia caídos diariamente en una semana, para que el programa le informe en
#pantalla el promedio de precipitación de esa semana. El cliente también desea
#saber cuál fue el día en que más llovió en la semana.
#A modo ilustrativo, un reporte generado por el programa debería verse como
#sigue, luego de haber leído las precipitaciones de los 7 días de la semana:
#El promedio de precipitaciones fue de XX mls. diarios.
#El día de más precipitaciones fue el xxxxxx (nombre del día).
#Tenga en cuenta que la numeración de los días de la semana comienza con el 1
#para el día domingo.
#Codifique el programa para dar solución a lo solicitado por el cliente.


# Creamos una lista vacía para almacenar las precipitaciones diarias
precipitaciones = []
dias_de_la_semana = ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']

# Pedimos al usuario que ingrese las precipitaciones de cada día de la semana
for i in range(7):
    precipitacion_diaria = float(input("Ingrese la precipitacion del dia : "))
    precipitaciones.append(precipitacion_diaria)

# Calculamos el promedio de precipitaciones
promedio = sum(precipitaciones) / len(precipitaciones)

# Buscamos el día con mayor precipitación
dia_max_precipitacion = precipitaciones.index(max(precipitaciones)) 

# Mostramos los resultados

print("El promedio de precipitaciones fue de ",str(promedio), "  mls. diarios.")
print("El dia de mas precipitaciones fue el dia: ", dias_de_la_semana[dia_max_precipitacion])


