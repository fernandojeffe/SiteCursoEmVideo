lista = ('Lapis ' , 1.75,
         'Boorracha', 2,
         'Cadernno', 15.95,
         'Estojo', 5.89,
         'Apontador', 2.55,
         'Mochila', 120.99,
         'Canetas', 22,
         'livros', 34.87)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for posição in range (0,len(lista)):
    if posição % 2 == 0:
        print(f'{lista[posição]:.<30}',end=' ')
    else:
        print(f'R${lista[posição]:>7.2f}')
print('-'*40)