#Censo virtual

name_list = []
last_list = []
cc = []
date_list = []
place = []
address_list = []
type_list = []
family_list = [0]

def family_head(first_name, last_name, typeid, id, birth_date, birthplace, address):
        name_list.append(first_name)
        last_list.append(last_name)
        type_list.append(typeid)
        cc.append(id)
        date_list.append(birth_date)
        place.append(birthplace)
        address_list.append(address)

def family_member(first, last, ty, idn, family):
        name_list.append(first)
        last_list.append(last)
        type_list.append(ty)
        cc.append(idn)
        family_list.append(family)


def show (z):
    if z == 0:
            print("Nombre: {}" .format(name_list[z]))
            print("apellido: {}" .format(last_list[z]))
            print("Tipo documento: {}" .format(type_list[z]))
            print("Numero documento: {}" .format(cc[z]))
            print("Fecha de nacimiento: {}" .format(date_list[z]))
            print("lugar de nacimiento: {}" .format(place[z]))
            print("dirección: {}" .format(address_list[z]))
    else:
            print("Nombre: {}" .format(name_list[z]))
            print("apellido: {}" .format(last_list[z]))
            print("Tipo documento: {}" .format(type_list[z]))
            print("Numero documento: {}" .format(cc[z]))
            print("parentesco: {}" .format(family_list[z]))

        
    

if __name__ == '__main__':
    start = 0
    x = 0
    a = input("Introduzca su nombre: ")
    b = input("Introduzca su apellido: ")
    c = input("Introduzca su tipo de documento: ")
    d = float(input("Introduzca su documento: "))
    e = input("Introduzca su fecha de nacimiento: ")
    f = input("Introduzca su lugar de nacimiento: ")
    g = input("Introduzca su dirección: ")
    h = int(input(("Introduzca la cantidad de miembros en la familia: ")))
    family_head(a, b, c, d, e, f, g)
    while start < h:
        ak = input("Introduzca su nombre: ")
        bk = input("Introduzca su apellido: ")
        ck = input("Introduzca su tipo de documento: ")
        dk = float(input("Introduzca su documento: "))
        ek = input("Introduzca su parentezco: ")
        family_member(ak, bk, ck, dk, ek)
        start += 1
    h += 1
    for x in range(h):
        print(x)
        show(x)