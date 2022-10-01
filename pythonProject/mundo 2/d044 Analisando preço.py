print('\033[33m#\033[m'*30)
print('Informe o valor do produto')
print('Escolha a forma de pagamento')
print('\033[33m#\033[m'*30)
print('1 para pagamento a vista')
print('2 para pagamento no cartão')
print('\033[34m#\033[m'*30)
produto = float(input('Qual o valor do produto: '))
escolha = int(input('escolha a forma de pagamento? '))
if escolha == 1:
    desconto = (produto *10)/100
    preçoFinal= produto - desconto
    print('Seu desconto a vista e de R${:.2f} e o preço ficara de R${:.2f}'.format(desconto,preçoFinal))
elif escolha == 2:
    base = int(input('Digite [1] para a vista\nDigite [2] para parcelar\n'))
    if base == 1:
        desconto1 = (produto*5)/100
        preçoFinal1 = produto - desconto1
        print('Seu desconto a vista e de R${:.2f} e o preço ficara de R${:.2f}'.format(desconto1,preçoFinal1))
    elif base == 2:
        parcela = int(input('Em quantas vezes será parcelado? '))
        if parcela < 2:
            dividido = produto / parcela
            print('O preço ficara R${:.2f} em 2 parcelas de R${:.2f}'.format(produto,dividido))
        elif parcela > 3:
            descdiv = (produto*30)/100
            preçoFinal3 = produto - descdiv
            parcediv  = preçoFinal3 / parcela
            print('O preço com desconto de R${:.2f} ficara com preço final de {:.2f}\n em {:.0f} parcelas de R${:.2f}'.format(descdiv,preçoFinal3,parcela,parcediv))
else:
    print ('Opão errada! tente novamente')