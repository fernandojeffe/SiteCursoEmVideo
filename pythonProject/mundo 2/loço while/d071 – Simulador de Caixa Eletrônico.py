print ('='*30)
print('{:^30}'.format('Banco Curso em video'))
print('='*30)
valor = int(input('Qual valor você quer sacar R$'))
total = valor
cedulas = 50
totalcedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print(f'Total de {totalcedulas} cédulas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totalcedulas = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre')