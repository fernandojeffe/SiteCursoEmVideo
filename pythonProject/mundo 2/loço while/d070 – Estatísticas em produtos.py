total = totalmil = menor = cont = 0
barato = ' '

while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço do pruduto: R$: '))
    cont += 1
    total += preço
    if preço > 1000:
        totalmil += 1
    if  cont == 1 or preço < menor:
        menor = preço
        barato  = nome
    saida = ' '
    while  saida not in 'SN':
        saida = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if saida == 'N':
        break

print('{:-^40}'.format('Fim do programa'))
print(f'O total da sua compra foi de {total:.2f}')
print(f'Temos {totalmil} produtos custando mais de R$1000,00')
print (f'O produto mais barato foi {barato} que custa R${menor:.2f}')