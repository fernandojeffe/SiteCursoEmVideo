print('\033[32m-*\033[m'*15)
print('\033[34mSimulação de venda de imóveis\033[m')
print('\033[32m-*\033[m'*15)
valor = float(input('Qual o valor do imóvel R$ : '))
sal = float(input('Qual é o salario do comprador R$ : '))
anos = int(input('Quantos anos pretende parcelar? : '))
parcela = valor/(anos*12)
salparc = sal*30/100
if parcela  <= salparc:
    print('\033[1;32;46mSua compra foi aprovada\033[m')    
    print('O valor do imovel e de R$:{:.2f} sua parcela e de R$:{:.2f} '.format(valor, parcela))
else:
    print('\033[1;31;46mSua compra foi negada!\033[m')
    print('Não desesta do seu sonho!')