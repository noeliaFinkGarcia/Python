# Funciones
# Recibir dos numeros y mostrar la suma aritmetica en pantalla. Invocar para comprobar

def suma_dos_numeros (numero1,numero2) :
    suma = numero1 + numero2
    print (suma)

num1 = float (input ("Ingresa un numero para sumar "))
num2 = float (input ("Ingresa el segundo numero "))
print ("El resultado de la suma de los numeros ingresados es: \r\n")
suma_dos_numeros(num1,num2)

# Recibir dos numeros y retornar la suma de ambos. Invocar para comprobar

def suma_dos_numeros_retorno (numero1, numero2):
    return (numero1 + numero2)

num3 = float (input ("Ingresa un numero para sumar "))
num4 = float (input ("Ingresa el segundo numero "))
print ("El resultado de la suma de los numeros ingresados es: \r\n")
print(suma_dos_numeros_retorno(num3,num4))
print ("\r\n")

# Recibe un string y devuelve el numero de caracteres. Invocar, ingresar nombre por teclado y mostrar cant de letras

def contar_letras(cadena) :
    return(len(cadena))

nombre = input ("Ingresa tu nombre. Con una funcion voy a decirte cuantas letras tiene: \r\n")
print ("Tu nombre tiene ", contar_letras(nombre), " letras \r\n")

# Recibir base y exponente y devolver resultado de potenciacion.

def potencia (base, exponente) :
    return pow (base, exponente)

# Pruebo si funciona
print (potencia(2,3))

# Recibe un string y lo devuelve en mayusculas

def poner_en_mayusculas (palabra) :
    return palabra.upper()


nombre = input ("Ingresa tu nombre, lo devolvere en mayusculas: \r\n")
print (poner_en_mayusculas(nombre))

# Modificar el script anterior y que devuelva todo en minusculas y todo en mayusculas

def poner_en_mayusculas_y_minusculas (palabra) :
    return palabra.upper(), palabra.lower()


# Pruebo 
nombre = input ("Ingresa tu nombre: \r\n")
print (poner_en_mayusculas_y_minusculas(nombre))

# Recibe dos string como parámetro y retorne True si nombre1 tiene más letras que nombre2, o False en caso contrario.

def mas_letras(nombre1, nombre2) :
    if(len(nombre1) > len(nombre2)) :
        return True
    else :
        return False


# Pruebo
nomb1 = "noelia"
nomb2 ="anyelen"
print(mas_letras(nomb1, nomb2))


# Recibe cadena, la devuelve. Se invoca en otro programa. Quedaría así

def leer_cadena():
    cadena = input("Ingrese una cadena de texto: ")
    return cadena


# Si esto fuera un main, la invocacion seria asi.
import modulo_cadena

cadena_ingresada = modulo_cadena.leer_cadena()

print("La cadena ingresada es:", cadena_ingresada)
