from array import array
from base64 import b16decode
from binascii import a2b_base64
from ctypes.wintypes import CHAR
from re import A
from sre_constants import RANGE
from stringprep import c22_specials


print("Holis cara de colis")

numero_entero = 5
print ("El valor absoluto de "  +str(numero_entero) + " es: "+ str(abs(numero_entero) ))
print("\r\n")


nombre = "Noelia"
print ("Mi nombre ", nombre,  " tiene", len(nombre), "caracteres")
print("\r\n")

print ("Para mi segundo nombre uso un ciclo for")
nombre1 = "Anyelen"
contador = 0
for caracter in nombre1:
    contador += 1
print(nombre1 ," tiene ", contador, " caracteres.")

print("\r\n")
# Definir la base y el exponente como variables
base = 2
exponente = 3

# Calcular la potencia utilizando el operador **
resultado = base ** exponente

# Mostrar el resultado en pantalla

print("El resultado de elevar ", base, " a la potencia ", exponente, "es: ", resultado)

print("\r\n")
# Pedir al usuario que ingrese la base y el exponente
base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))


resultado = pow(base,exponente)

# Mostrar el resultado en pantalla
print("El resultado de elevar", base, "a la potencia", exponente, "es:", resultado)
print("\r\n")

print ("Calcular el perimetro de un rectangulo conociendo su base y altura y mostrar el resultado")

# Definir la base y la altura del rectángulo
baseRectangulo = 10
altura = 5

# Calcular el perímetro del rectangulo
perimetro = 2 * (baseRectangulo + altura)

print("El perimetro del rectangulo, cuando su base es ", baseRectangulo," y su altura es ",altura," resulta: ",perimetro)

#Calcular el area de un rectangulo, conociendo su base y altura y mostrar el resultado.

print ("\r\n Calcular el area de un rectangulo guardando los valores en variables y mostrar el resultado ")

base2 = 10
altura2 = 10
area = base2*altura2
print ("El area de un rectangulo de base " ,base2," y altura " ,altura2," es: ", area, "\r\n")


#Intercambiar variables 
print ("Intercambiar variables")
a=34
b=25
print ("variables iniciales: a=", a, " b=", b, "\r\n")
variableAuxiliar = b
b=a 
a=variableAuxiliar

print ("Variables intercambiadas: a= ",a, " b= ",b,"\r\n")

print ("Intercambiar variables sin usar variables auxiliares\r\n")

#Sintaxis de asignacion multiple
c = 34
d = 43

print ("Valores iniciales: c = ", c, " d = ", d, "\r\n")

c, d = d, c
print ("Los nuevos valores, usando asignacion multiple son: c = ", c, " d = ", d, "\r\n")

print ("Conociendo las dos notas de un alumno, calcular y mostrar el promedio \r\n")

nota1 = 8
nota2 = 10
promedio = (nota1+nota2)/2

print ("Siendo las notas nota1= " ,nota1, " nota2 = ", nota2, "el promedio es: ", promedio, "\r\n")

print ("Convertir pesos a otras monedas \r\n")

pesos = 10000
cantidadDolares = pesos / 80.50
cantidadReales = pesos / 14.1
cantidadEuros = pesos / 69.50

print ("Tenes en tu cuenta $", pesos, "\r\n")
print ("En dolares son: USD", cantidadDolares, "\r\nEn reales serian R$", cantidadReales, "\r\nEn euros son E$", cantidadEuros, "\r\n" )

