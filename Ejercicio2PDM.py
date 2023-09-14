'''Encontrar el valor minimo y maximo de luna lista numerica'''
def min_max(numeros):
    minimo = numeros[0]
    maximo = numeros[0]
    for b in numeros:
        if b < minimo:
            minimo = b
        if b > maximo:
            maximo = b
    return minimo, maximo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min_max(lista))
