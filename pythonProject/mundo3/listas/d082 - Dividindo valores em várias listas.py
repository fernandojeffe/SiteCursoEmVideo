numero = []
pares = []
impares = []

while True:
     numero.append(int(input('Digite um número: ')))

     saida = ' '
     while saida not in 'SN':
          saida = str(input('Que continuar? [S/N]')).strip().upper()[0]
     if saida in 'N':
          break

for contador, valor in enumerate (numero):
     if valor % 2 == 0:
          pares.append(valor)
     elif valor % 2 == 1:
          impares.append(valor)
print('-=' * 30)
print(f'A lista completa é {numero}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
