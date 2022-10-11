from random import randint
from time import sleep
print("-=-"*17)
print('Vou pensar em um número de 0 a 5 Tente adivinhar!')
print("-=-"*17)
num = int(input('Digite um número: '))
print('processando...')
sleep(3)
sorteio = (randint (0,5))
escolhido = sorteio
if (num == sorteio):
    print('Voce acertou! Parabéns')
    if (num > 5):
        print ('numero mair digitado tente novamente')
else:
    print('Tente de novo!')
    print('O numero escolhido foi {}'.format(escolhido))