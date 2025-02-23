print ("Hola mundo")
     
#Hola mundo

print ("Hola","Mundo","Python",3)
     
#Hola Mundo Python 3

print ("Adios mundo Python")
     
#Adios mundo Python

#Además de los valores a imprimir que pueden ser de cualquier tipo, la función print tiene dos parámetros adicionales con valores por defecto

#sep (separador) cuyo valor por defecto es un espacio " "

#end (final) cuyo valor por defecto es un salto de línea \n

#Podemos por lo tanto darle valores específicos a estos dos argumentos en caso de ser necesario.

"""Variables, tipos de datos, operadores"""


     
#Datos Numéricos
#Tipado Dinámico


x = 15
print("Tipo de datos de X:", type(x))
     
#Tipo de datos de X: <class 'int'>

x = 15
y = 2
print("Tipos de datos de  y:", type(y))
z = x/y
print (z)
print ("Tipo de dato de z", type(z))
x = "hola"
print(x)
print(type(x))
     
#Tipos de datos de  y: <class 'int'>
#7.5
#Tipo de dato de z <class 'float'>
#hola
#<class 'str'>
"""¿Podrías decirnos antes de ejecutar el siguiente código cuál es el resultado de cada operación:?"""
print(5/2)

print(5%2)

print(5**2)

print(15//4)

#Operadores Aritmeticos
"""
+	Suma
-	Resta
/	División
%	Residuo
*	Multiplicación
//	División entera
**	Exponenciación
~	Negación 
"""



#Los numeros los podemos expresar con un guion bajo que les brinde mayor claridad de lectura.



x = 1_250_000 + 3_240_000
y = 1250000 + 3240000
print(x,y)



#Por defectos los numeros en py son decimales, pero tambien podemos expresarlo en formato binario, octal y hexadecimal. 0b, 0o y 0x respectivamente.



"""¿Podrías indicarnos antes de ejecutar el siguiente código, cuál es el valor en decimal de los siguientes números?"""


print (12)
print (0b101)
print (0o12)
print (0x12)
print (hex(0o174))
print (bin(5))
print (oct(0xA21))
     
12
5
10
18
0x7c
0b101
0o5041



#Operadores lógicos a nivel de bits
"""
AND &

OR |

XOR ^
"""

print (2 & 3) # 10 & 11 = 10 = 2
print (2|3) # 10 | 11 = 11 = 3
print (2 ^3) # 10  ^ 11 = 11 = 1



#¿Cual seria el resultado de las siguentes operaciones?

print ( 1 & 3 ) # 01 & 11 =
print ( 21 | 12 ) #
print(bin(21))
print ( 5 & 8 ) #

print(bin(5)) # Le pedimos que pase ese numero a binario, entregandonos los valores
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

"""Aca un par de ejercicios para poner en practica lo repasado"""

        #Realice un programa que calcule el índice de cosecha de un cultivo en función de la cantidad de frutos recolectados y la cantidad de frutos producidos en total."""
            #Fórmula:
            
            """Índice de cosecha = (cantidad de frutos recolectados / cantidad de frutos producidos) * 100% """
#SOLUCIÓN
#Ejercicio 1
cantidad_recolectados = float(input("Ingrese la cantidad de frutos recolectados: ")) #Le pedimos al usuario que ingrese la cantidad de frtutos recolectados y para que no tire error y la función no tome el valor ingresado por string le pedimos que sea de valor INT, en este caso numero.
cantidad_producidos = float(input("Ingrese la cantidad de frutos producidos en total: "))

if cantidad_recolectados > 0 and cantidad_producidos > 0: #Le agregamos una condicional, para asi evitar errores de digitación, en este caso le pedimos que si el dato insertado en cantidad de frutos es recolectados es MAYOR a 0 se ejecute la  operación y imprima el resultado.
    indice_cosecha = (cantidad_recolectados / cantidad_producidos) * 100 #Calculamos el indice de cosecha dividiendo los datos insertados y multiplicandolos por 100.
    print(f"El índice de cosecha es: {indice_cosecha:.2f}%") #Le pedimos al sistema que imprima el resultado y para redondear y no tener tantos decimalos ingresamos la funcion .2f , que formatea el resultado y elimina los dos decimales para covertirlos en un %
else:
    print("La cantidad de frutos recolectados debe ser mayor a 0") #En caso de que la función no se cumpla no realizara la operación y impresión del resultado, sino que arrojara un mensaje de error donde saldra el porque de este.

#Ejercicio #2
#Dibujar la P de Python que abarque 7 filas y 5 columnas. Use solo una línea de código


print(4 * "P" + "\nP" + " " * 3 + "P" + "\nP" + " " * 3 + "P" + "\n" + 4 * "P", end="\nP\nP\nP")

#Explicación breve, \nP = Salto de columna insertando la letra P en la otra columna, \n, Salto de linea sin insertar ninguna valor, " " * 3, aca lo que hago es pedirle que al espacio en blanco que escribi le multiplique tres más, de esta forma haremos la forma de la letra P mejor.


#Ejercicio #3
#Un alumno desea saber cuál será su calificación final en la materia de Matemáticas. Dicha calificación se compone de los siguientes porcentajes: 55% del promedio de sus tres calificaciones parciales (se debe leer cada calificación parcial). 30% de la calificación del examen final. 15% de la calificación de un trabajo final.

calificacion_parcial1 = float(input("Ingrese la calificación de su primer parcial en el rango de 10 a 50 : ")) #Declaramos las variables y le pedimos al usuario que inserte los datos del numero 10 al sistema dependiendo sus resultados.
calificacion_parcial2 = float(input("Ingrese la calificación de su segundo parcial en el rango de 10 a 50: "))
calificacion_parcial3 = float(input("Ingrese la calificación de su tercer parcial en el rango de 10 a 50: ")) #Los resultados de estos 3 parciales seran sumados y dividios en tres para sacar un promedio de pasarlo y que sea una sola nota.
examen_final = float(input("Ingrese la calificación de su examen final en el rango de 10 a 50: "))
trabajo_final = float(input("Ingrese la calificación de su trabajo final en el rango de 10 a 50: "))
if 10 <= calificacion_parcial3 <= 50 and 10 <= calificacion_parcial1 <= 50 and 10 <= calificacion_parcial2 <= 50 and 10 <= examen_final <= 50 and 10 <= trabajo_final <= 50 :  #Creamos la condición, donde si calificación parcial es menor o igual que 10 y menor o igual que 50 la función sera cumplida, es la misma condición aplicada en todas las variables buscando que cada una cumpla la misma función
    promedio_total = (calificacion_parcial1 + calificacion_parcial2 + calificacion_parcial3) / 3  #Sacamos el promedio total de los parciales sumando todos los resultados y dividiendolos entre 3.
    resultado_final = (promedio_total * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15) #Ya con un promedio total de todos los parciales procedemos a hacer la operación, donde sumamos todos los resultados y le multiplicamos el porcentaje que le corresponde a cada uno, en este caso el resultado de los premido corresponde a un %50, examen final a %30 y trabajo final a %15
    print(f"Su calificación final en la materia de matemáticas es de: {resultado_final:.2f}") #Se imprime el resultado final
else: 
    print("Los datos ingresados no coinciden, porfavor intentelo de nuevo.") #En caso de no cumplir alguna función saltara el siguente mensaje.            

#Ejercicio 4
#Recibir una frase por parte del usuario y devolver el número de palabras que se encuentran en la frase.

fraseinsertada = input("Ingrese una frase: ")  # Solicita la frase al usuario
cantidad_de_palabras = fraseinsertada.count(" ") + 1  # Cuenta los espacios y suma 1 para obtener el número de palabras, es decir cada espacio insertado se le sumara "1" para asi llevar la cuenta de palabras.
print(f"La frase ingresada tiene {cantidad_de_palabras} palabras.")  # Muestra el resultado y imprime el resultado

#Ejercicio 5       
#Recibir una frase y transformarla a mayúscula sostenida e invirtiendo su contenido</p>
frase = (input("Escriba la frase que quiere inverter y transformar a mayuscula: ")) #Pedimos que ingrese la frase 
frase_mayuscula_invertida = frase.upper()[::-1] #Creamos la variable para implementar los cambios que necesitamos, en este caso la función upper nos ayudara a obtener la cadena de caracteres de la variable frase y los convertira a mayuscula y [::-1] nos ayudara a abarcar todos los caracteres y invertirlos.
print(f"La frase en mayuscula y invertida se interpretaria de la siguente manera: {frase_mayuscula_invertida}")
