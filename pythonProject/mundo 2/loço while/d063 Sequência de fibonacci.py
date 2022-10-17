print('-'*30)
print('Sequência de fibonacci')
print("-"*30)
num = int(input('Informe quantos elementos voê quer ver: '))
termo1 = 0
termo2 = 1
print('~'*30)
print('{} -> {}'.format(termo1,termo2),end='')
cont = 3
while cont <= num:
    termo3 = termo1 + termo2
    print(' -> {}'.format(termo3),end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print('Fim')