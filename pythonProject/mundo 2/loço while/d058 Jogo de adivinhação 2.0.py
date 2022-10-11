from random import randint
from time import sleep

print("-=-"*17)
print('Vou pensar em um número de 1 a 10 Tente adivinhar!')
print("-=-"*17)

sorteio = (randint (1,10))
escolhido = sorteio
num = 0
'''print('processando...')
sleep(3)'''

while escolhido != num:
    num = int(input('Digite um número entre 1 a 10 : '))
    if (num == sorteio):
        print('Voce acertou! Parabéns')
        print('O numero escolhido foi {}'.format(escolhido))
    else:
        print('Tente de novo!')

