print(5/2)

print(5%2)

print(5**2)

print(15//4)

#Operadores Aritmeticos
"""|Suma
|
|
|
|
|

"""



#Los numeros los podemos expresar con un guion bajo que les brinde mayor claridad de lectura.



x = 1_250_000 + 3_240_000
y = 1250000 + 3240000
print(x,y)



#Por defectos los numeros en py son decimales, pero tambien podemos expresarlo en formato binario, octal y hexadecimal. 0b, 0o y 0x respectivamente.



print (12)

print (0b101)

print (0o12)

print (0x12)
print (hex(0o174))

print (bin(5))

print (oct(0xA21))



#Operadores lógicos a nivel de bits
"""AND &
OR |
XOR ^"""


print (2&3)

print (2 & 3) # 10 & 11 = 10 = 2
print (2|3) # 10 | 11 = 11 = 3
print (2 ^3) # 10  ^ 11 = 11 = 1



#¿Cual seria el resultado de las siguentes operaciones?

print ( 1 & 3 ) # 01 & 11 =
print ( 21 | 12 ) #
print(bin(21))
print ( 5 & 8 ) #

print(bin(5))
print(bin(8))
x = 0b101
y = 0b1000
print ( x & y )

print(bin(21))
print(bin(12))
x = 0b10101
y = 0b1100
print (x | y)

print(bin(1))
print(bin(3))
x = 0b1
y = 0b11
print (x & y)

print (3 > 5) #false
print ()
print ()
print ()
print ()
print ()

#Números flotantes

print ( 2**3 ) #8
print ( 2E3 ) #2000
print ( 2.5E2 ) #250
print ( .5E4 ) #5000

#Tipos de cadena

#Objetos inmutables a los que les podemos aplicar diferentes métodos. Otra caracteristica es que cada cadena está conformada por un onjunto de caracteres a los cuales podemos acceder mediante sus índices.

x = 3
y = 5
z = x + y
print(z)

cad = "Pythonton"
print(type(cad))
print(cad)
print (cad[0]) #Imprime la letra segun la posición
print (cad[3]) #Imprime la letra segun la posición

print (cad.count("o")) #Cuenta el numero de veces que se repite la vocal en la palabre

"""Cadena con múltiples líneas"""

#Cadenas multilineas
cad = """Escucha hermano
       la canción de la alegria """
print(cad)

cad2 = "\nEl canto alegre\ndel que espera\nun nuevo\ndia" #Manera de dar salto de lineas mas facil
print(cad2)



"""Concatenación y formateo de cadenas"""

#Concatenación y formateo de cadenas
print ("1) Hola " + "Mundo " + "Python " + str(3)) #Manera de concatenar el texto #1
print ("1) Hola, " "Mundo", "Python 3", 3) #Manera de concatenar el texto #2
lenguaje,version = "python", 3 #Asignación multiple, esto apartir de comas declarando las variables y los datos de estas
print(lenguaje)
print(version)



lenguaje,version = "Python", 3
print("3) Hola mundo %s %s " %(lenguaje,version)) #Otra manera de asignar variables

print("4) Hola mundo {} {}".format(lenguaje, version)) #Esta función ata el formato y el string

print(f"5) Hola mundo {lenguaje} {version}") #Liga la variable para poder llamarla/buscarla dentro de una función print

print ("6) Hola", lenguaje, "mundo")



"""Dato curioso es que en py podemos multiplicar las cadenas"""

cadena = "si"
print((cadena*3, "Este amor es tan profundo"))
print((("*"*8)+ "\n")*4)

print("+"+10*"-"+"+") #Ejercicio Cuadrado
print (("|" + " " * 10 + "|\n" )* 5, end ="")
print("+"+10*"-"+"+")

"""Slicing de Caenas
Tomamos parte de las cadenas"""

cadena = "lenguaje de programación python"
print(cadena[0:8]) #Con esto podemos traer cierta parte de la variable, en este caso del caracter numero 0 al 8.
print(cadena[9:11]) #Con esto podemos traer cierta parte de la variable, en este caso del caracter numero 9 al 12.
print(cadena[12:24])#Con esto podemos traer cierta parte de la variable, en este caso del caracter numero 12 al 24.
print(cadena[25:31]) #Con esto podemos traer cierta parte de la variable, en este caso del caracter numero 25 al 31.

"""Comprendiendo los valores por defecto y valores negativos en el slicing"""

cadena = "lenguaje de programación python"
print(cadena[:3]) #Arranca desde el caracter numero 3
print(cadena[25:]) #Arranca desde el caracter numero 25
print(cadena[-6:-2]) #Retrocede esos valores
print(cadena[-9])

"""Conversiones entre tipos

"""

a,b = "3", "5" #Forma de sumar variables y no solo junte los dos numeros

print (a+b) #Unir los numeros
print (int(a)+int(b)) #Suma de los dos numeros



"""Metodo de cadenas 
A las cadenas les podemos aplicar una serie de motodos útiles predefinidos en python. Aca un par de ejemplos :
"""

cadena_uno = "Mi probe angelito".lower() #lower es que coje todo en minuscula y lo asigna a la cadena_dos para asi poner todo en mayuscula
cadena_dos = cadena_uno.upper()

print(cadena_dos) #Imprimimos la variable cadena_dos, que al usar upper, devuelve la frase en mayuscula

numero_de_o = cadena_uno.count("o") #devuelve el numero de vecves que se encuentra en la subcadena

print(numero_de_o) #Llamamos a la variable para saber cuantas veces esta la letra o

print(f"La letra 'o' esta {numero_de_o} veces en la palabra/frase '{cadena_uno}'") #Imprimimos el numero de veces que esta la palabra en la frase

"""**Lectura de datos**

La función input permite realizar la lectura de datos de entrada por parte del usuario. La función input devuelve lo ingresado por el usuario en forma de cadena, si se desea capturar un dato de otro tipo se debe hacer una respectiva conversión.
"""

marca = input ("Ingrese la marca del auto: ") #Nos ejecuta una cuadro donde leera los datos, en esta caso deberas ingresar el nombre de la marca que mas te guste.
print("La marca del carro ingresada por el usuario es", marca) #Al ingresar la marca te saltara el mensaje puesto.

precio = int(input("Ingrese precio: ")) #Hacemos otra preuba con ingresar el precio
print(f"El auto marca {marca} tiene un precio de ${precio} y con el descuento del 10% quedaria en {precio*0.9}")#Damos el precio y le aplicamos un descuento del 10%

print("El auto marca {} tiene un precio de ${:,} y con el descuento del 10% quedaria en ${:,}".format(marca,precio,precio*0.9)) #Formateamos el valor para que nos lo de en nuestra moneda, en este caso la Colombiana, basicamente con el format le especificamos los espacios que va a formatear.



"""Apropiación"""



"""1. Realice un programa que calcule el indice de cosecha de un cultivo en función de frutos recolectados y la cantidad de frutos producidos en total.
Formula :
indicedecosecha = (cantidad de frutos recolectados / cantidad de frutos producidos ) * 100%
"""

cantidad_de_frutos_recolectados = input ("Ingrese la cantidad de frutos recolectados : ")
cantidad_de_frutos_producidos = input ("Ingrese la cantidad de frutos producidos : ")

indice_de_cosecha = (cantidad_de_frutos_recolectados / cantidad_de_frutos_producidos ) 