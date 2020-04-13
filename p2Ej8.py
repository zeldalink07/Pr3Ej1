from collections import Counter

def esPrimo(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
                break
        else:
            return True
    else:
        return False 

print('Ingresar un string')

cadena = str(input()).lower()

repeticiones = Counter(cadena)

#lista = Counter(cadena).items()
lista = []
for x, y in repeticiones.items():
    temp = [x,y]
    lista.append(temp)

cont = 0
for x in repeticiones.values():
    if esPrimo(x):
        primo = ' y es PRIMO.'

    else:
        primo = ' y NO es primo.'
    print('La letra ', lista[cont][0], ' aparece esta cantidad de veces: ', lista[cont][1], primo)
    cont += 1