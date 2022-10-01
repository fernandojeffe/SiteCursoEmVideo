from random import shuffle
n1 = (input('Informe o primeiro nome: '))
n2 = (input('Informe o segundo nome: '))
n3 = (input('Informe o terceiro nome: '))
n4 = (input('Informe o qurto nome: '))
lista =[n1, n2, n3, n4]
shuffle (lista)
print('A ordem de aprensentação será de:')
print(lista)