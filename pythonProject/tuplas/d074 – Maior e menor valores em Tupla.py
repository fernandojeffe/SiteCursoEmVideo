from random import randint
núm = (randint(1, 10), randint(1, 10), randint(1,10), randint(1, 10), randint(1,10))
print('Os valores sorteados foram: ',end=' ')
for n in núm:
    print(f'{n}',end=' ')
print(f'\nO maior valor foi de {max(núm)}')
print(f'O menor valor foi de {min(núm)}')