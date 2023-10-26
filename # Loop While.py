# Loop While

#a = 0

#while a < 20:
#    a += 2
#    print(a, end=" ")

#b = 1

#while b < 20:
#    b += 2
#    print(b, end=" ")

#while a < 10:
#    a += 1
#    if a == 8:
#        continue
#    print(a, end=" ")

primero = 3

while primero<=7:
		print ("Tabla del " + str(primero)	)
		segundo = 1
		while segundo<=10:
			print (str(primero)+ "X" + str(segundo)+"="+ str(primero*segundo))
			segundo+=1
		primero +=1
		print ("\n")
print ("Se termino")

