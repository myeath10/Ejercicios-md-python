'''Ordenar una lista de numeros de forma ascendente'''
lista = []
print("¿Cuántos numeros desea poner?: ")
num = int(input())
c = 0

while c < num:
    print("Ingrese el número", c + 1)
    nom = input()
    lista.append(nom)
    c+=1

lista.sort()
print(lista)
lista.reverse()
print(lista)