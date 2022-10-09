cont = 0
soma = 0

for c in range (1,7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
     soma += num
     cont += 1

print('A soma de dos números e de {}'.format(soma))

