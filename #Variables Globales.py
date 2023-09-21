#Variables Globales
#global variable
#variable = 2
# def glob():
#   variable = 1
#   print("Hola variable")
global var 
var = 2
def global_variable():
    global var
    var = 2
    return var

if __name__ == '__main__':
    print(var)
    print(global_variable())

