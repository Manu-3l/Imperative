#functions

def message():
    print("Hi world!")

def suma(a,b):
    total = a + b
    #print("La suma total es: {}" .format(total))
    return total
def dame_pi():
    #num_pi = 3.14159
    return 3.14159


#Entry point for initialization our programs
if __name__ == '__main__':
    #message()
    #suma(1,2)
    #num_1= int(input("enter a number one:"))
    #num_2= int(input("enter a number two:"))
    #x = suma(num_1, num_2)
    #print("The value of suma is: {}".format(x))
    devolver = dame_pi()
    print(devolver)
    print(dir(devolver))