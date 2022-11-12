from random import randint

palpites = []
jogos = []
totalJogadas = 1


quantidadeJogadas = int(input('Quantos jogos você quer jogar: '))

while totalJogadas <= quantidadeJogadas:
    contador = 0
    while True:
        numero = randint(1,60)
        if numero not in palpites:
            palpites.append(numero)
            contador += 1
        if contador >= 6:
            break
    palpites.sort()
    jogos.append(palpites[:])
    palpites.clear()
    totalJogadas += 1
print('-=' * 3, f'SORTEADO {quantidadeJogadas} JOGOS', '-='*3 )
for indice, lista1 in enumerate (jogos):
    print(f'Jogo {indice+1}: {lista1}')

