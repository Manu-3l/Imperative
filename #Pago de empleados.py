#Pago de empleados

def calculate(name, cc, salary):
    bonus = salary * 0.10
    subsidy = salary * 0.20
    healthcare = salary * 0.04
    allowance = salary * 0.04
    retesource = salary * 0.05
    total = salary + bonus + subsidy
    discount = healthcare + allowance + retesource
    net = total - discount
    print("Nombre: {}".format(name))
    print("Documento: {}".format(cc))
    print("-------pagos------")
    print("Salario: {}".format(salary))
    print("Bonificación de servicio: {}".format(bonus))
    print("Subsidio de transporte: {}".format(subsidy))
    print("-------pagos------")
    print("Salud: {}".format(healthcare))
    print("Pensíon: {}".format(allowance))
    print("Retención en la fuente: {}".format(retesource))
    print("-------pagos------")
    print("Total pagos: {}".format(total))
    print("Total descuentos: {}".format(discount))
    print("Neto a pagar: {}".format(net))
    print("-------pagos------")
    

    pass

if __name__ == "__main__":
    start = 0
    quantity = float(input("digite la cantidad de empleados: "))
    while start < quantity:
        a = input("Introduzca su documento de identidad: ")
        b = input("Introduzca nombre completo: ")
        c = float(input("Introduzca su salario: "))
        calculate(b, a, c)
        start =+ 1
