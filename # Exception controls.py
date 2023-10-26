# Exception controls

#dividendo = 1
#divisor = 0

#try:
#   result = dividendo/divisor
#except ZeroDivisionError:
#    print("can't divide by zero")
#else:
#    print("It didn't divide by zero")
#finally:
#    print("Aguacate")

#try:
#    global value
#    value = int(input('Ingresa un número natural: '))
#print('El recíproco de', value, 'es', 1/value)        
#except ValueError:
#    print("Type your value correct, enter")
#else:
#    print("Data correct")

def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero"
    except ValueError:
        return "Error: ingrese un valor numerico correcto"
    except Exception as e:
        return "Error inesperado:" + str(e)
    
result1 = dividir(4,2)
result2 = dividir(10,5)
result3 = dividir("-",10)
result4 = dividir(5,0)
result5 = dividir("Uno","b")