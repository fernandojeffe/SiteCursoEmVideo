from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint (1,6), 'Jogador 2': randint (1,6), 'Jogador 3': randint (1,6), 'Jogador 4' : randint (1,6)}

ranking = []
print ('Valores sorteados: ')
for chave, valores in jogo.items():
    print(f'{chave} tirou {valores} no dado! ')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 15)
for indice, valor in enumerate(ranking):
    print(f'  {indice+1}° lugar: {valor[0]} com {valor[1]}.')
    sleep(1)
