'''#generar una lista de numeros primos hasta el rango dado'''
primos = []
N = 1000

for a in range(2,N + 1):
    primo = True
    for b in range(2, a):
        if a % b == 0:
            primo = False
            break

    if primo:
        primos.append(a)
        print(a)