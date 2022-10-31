from operator import truediv
from re import I


lista = []
while True:
    numero = int(input('Digite o valor: '))
    lista.append(numero)

    saida =' '
    while saida not in 'SN':
        saida = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if saida in 'N':
        break
    
print('-='*30)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os alores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista! ')
else:
    print('O valor 5 não faz parte da lista!')