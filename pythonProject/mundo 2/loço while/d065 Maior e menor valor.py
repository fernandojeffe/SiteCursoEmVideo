maor = menor = cont = media = soma = 0
saida = ''

while saida in 'Ss':
    num = int(input('Informe o valor: '))
    cont += 1 
    soma += num 
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    saida = str(input('deseja informar algum nùmero [S/N]')).strip().upper()
    
        
media = soma/cont
print ('Você digitol {} números e a media é de {}'.format(cont,media))
print('O maior valor foi {} e o menor foi de {} '.format(maior,menor))
