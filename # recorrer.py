# recorrer
import random
a = 0


lista = list()
lista = [1, 2, 3, 4, 5]
for i in lista:
    print("el valor de: ", i)

# ejercicio en clase, genere una lista vacia, y añade 10 elementos de manera aleatoria
# del 1 al 16 y luego ordenarlas de manera ascendente y descendente

lista1 = list()
if __name__ == "__main__":
    for i in range(11):
        x = random.randint(1, 16)
        lista1.append(x)
        i += 1
    print(lista1)
    lista2 = lista1.sort()
    print(lista1)
    lista2 = lista1.reverse()
    print(lista1)
