# Recibe un nombre, saluda y cuenta las letras del nombre
nombre = input ("Ingresa tu nombre ")
print ("Hola, ", nombre, ".Tu nombre tiene ", len(nombre), " letras.\r\n")

# Recibe dos numeros por teclado y devuelve la suma de ambos
numero1 = int(input ("Ingresa un numero entero: "))
numero2 = int(input ("Ingresa un segundo numero entero: "))
suma = numero1 + numero2
print ("La suma de los numeros ingresados es: ", suma, "\r\n")

# Calcular el perimetro de un rectangulo, con los datos ingresados por teclado
base = float(input("Ingresa la base del rectangulo: "))
altura = float(input("Ingresa la altura del rectangulo: "))
perimetro = 2 * (base+altura)
print ("El perimetro de su rectangulo es: ", perimetro, "\r\n")

# Ingresar por teclado apellido, notas y devolver apellido, notas y promedio
apellido = input("Ingresa tu apellido \r\n")
nota1 = float(input("Ingresa la nota del primer parcial: \r\n"))
nota2 = float(input("Ingresa la nota del segundo parcial: \r\n"))
promedio = (nota1+nota2)/2
print ("Alumno: ", apellido, "\r\n Parcial 1: ",nota1, "\r\n Parcial 2: ",nota2,"\r\n Promedio: ", promedio, "\r\n")

# Recibir base y exponente por teclado y devolver el resultado
base1 = int (input ("Ingresa el valor de la base: "))
exponente = int (input ("Ingresa el valor del exponente: "))
resultado = pow (base1, exponente)
print ("El resultado de elevar ", base1, "al exponente ", exponente, " es: ",resultado,"\r\n")