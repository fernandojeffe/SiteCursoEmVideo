listaPrincipal = []
listaTemporaria = []
maior = menor = 0
while True:
    listaTemporaria.append(str(input('Nome: ')))
    listaTemporaria.append(float(input('Peso: ')))
    
    if len(listaPrincipal) == 0:
        maior = menor = listaTemporaria[1]
    else:
        if listaTemporaria[1] > maior:
            maior = listaTemporaria[1]
        if listaTemporaria[1] < menor:
            menor = listaTemporaria[1]
    
    listaPrincipal.append(listaTemporaria[:])
    listaTemporaria.clear()
   
    saida = ' '
    while saida not in 'SN':
        saida = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if saida == 'N':
        break
print ('-=' * 20)
print(f'Ao todo, você cadastrou {len(listaPrincipal)} pessoas.')
print(f'O maior peso foi de {maior}Kg. peso de ',end='')

for pessoas in listaPrincipal:
    if pessoas[1] == maior:
        print (f'[{pessoas[0]}]',end='')
print()

print(f'O menor peso foi de {menor}Kg. peso de ',end='')
for pessoas in listaPrincipal:
    if pessoas in listaPrincipal:
        if pessoas[1] == menor:
            print (f'[{pessoas[0]}]',end='')
print()