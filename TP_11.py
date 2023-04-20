#def ingresarNumeros (lista, valor) :
#    lista.append(int(valor))
#    return lista


## Pruebo la funcion
#mensaje = "Ingrese un numero ('salir para terminar')"
#lista_de_numeros = []
#condicion_de_salida = True
#while ( condicion_de_salida ) :
#    valor = input(mensaje)
#    if(valor != "salir")  :
#      ingresarNumeros (lista_de_numeros,valor)
#      condicion_de_salida = True
#    else : condicion_de_salida = False

#print ("Lista ingresada: ",lista_de_numeros)


def es_primo(numero):
    # Función auxiliar para determinar si un número es primo o no
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def lista_de_primos(numeros):
    # Devuelve una lista con todos los números que sean primos
    primos = []
    for numero in numeros:
        if es_primo(numero):
            primos.append(numero)
    return primos

  

    
    
        
