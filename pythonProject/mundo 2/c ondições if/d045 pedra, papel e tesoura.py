#nesse codigo não consegui fazer
from pickle import FROZENSET
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input('qual é a sua jogada? '))


print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1) 

# processo para substituir o numero randomico pela lista 
print ('-='*11)
print ('O jogador jogou {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[computador]))
print ('-='*11)

if computador == 0: #Pedra
    if jogador == 0:
        print('Deu empate!')
    elif jogador == 1:
        print ('Jogador ganhou! ')
    elif jogador == 2:
        print('Computador Ganhou')
    else:
        print('Jogada inválida')
elif computador == 1: #Papel
    if jogador == 0:
        print('Compudar ganhou!')
    elif jogador == 1:
        print ('Deu empate!')
    elif jogador == 2:
        print('Jogador Ganhou')
    else:
        print('Jogada inválida')
elif computador == 2: #Tesoura
    if jogador == 0:
        print('Jogador ganhou!')
    elif jogador == 1:
        print ('Computador Ganhou')
    elif jogador == 2:
        print ('Deu empate!')
    else:
        print('Jogada inválida')
else:
    print('Opção inválida')
    