#Acierto multiplicación
import random
rights = 0
fails = 0
a = 0


while a < 13:
    try:
        name = input("Introduzca su nombre: ")
        for x in range(12):
              first = random.randint(-5,15)
              second = random.randint(-5,15)
              product = first * second
              print ("El primer numero es: {}".format(first))
              print ("El segundo numero es: {}".format(second))
              x = int(input("Cual es la multiplicación entre los dos: "))
              if x == product:
                     rights += 1
                     x += 1
                     continue
              else:
                     fails += 1
                     print("La respuesta es : {}".format(product))
                     x += 1
                     continue      
    except ValueError:
                print("Oops!  That was no valid number.  Try again...")
    print(name)
    print("Tus aciertos fueron: {}".format(rights))
    print( "y tus fallos: {}".format(fails))
    a += 13
    
        


