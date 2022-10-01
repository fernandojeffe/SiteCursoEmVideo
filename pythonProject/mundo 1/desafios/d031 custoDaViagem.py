dist = float(input('Qual a distancia em km da viagem? '))
'''if dist <= 200:
    somad = dist * .5
    print('O valor da corrida e de R${:.2f}'.format(somad))
if dist > 200:
    somadm = dist * .45
    print('O valor da corrida e de R${:.2f}'.format(somadm))
else:
    print('Tenha uma boa viagem!')'''
#opição ternaria
preço = dist * 0.50 if dist<=200 else dist * 0.45
print('E o preço da sua passagem e será de R$:{:.2f}'.format(preço))