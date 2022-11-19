jogador = {}
partidas = []
jogador ['nome'] = str(input('Nome do jagador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range (0,tot):
    partidas.append(int(input(f'quantos gols na {c+1}ª partida ? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' *30 )
print(jogador)
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas. ')
for i, v in enumerate (jogador['gols']):
    print(f'   => Na partidada {i+1}ª, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols ')