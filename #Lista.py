# Lista
lista = [1, 3, 2, "america"]
lista2 = [4, 5, "Halloween"]
lista12 = lista + lista2
list_slice = lista12[1:4]
list_slice.extend(lista2)
list4 = lista[3] * 16
print(lista12)
print(list_slice)
print(list4)
list5 = lista.pop()
print(lista)
list6 = lista.sort()
print(lista)

