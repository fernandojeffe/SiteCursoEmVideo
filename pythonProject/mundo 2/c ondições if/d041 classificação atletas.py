from datetime import date
print('\033[1;30m<>\033[m'*12)
print('Classificação de atletas')
print('\033[1;30m<>\033[m'*12)
idade = int(input('Qual o ano de nascimento do nadador: '))
ano = date.today().year
categoria = ano - idade
if categoria <= 13:
    print('\033[31;43mVocê esta com {} anos e esta na categoria MIRIM\033[m'.format(categoria))
elif categoria <= 14 or categoria <= 19:
    print('\033[33;44mVocê esta com {} anos e esta na categoria JÚNIOR\033[m'.format(categoria))
elif categoria <= 20 or categoria <= 24:
    print('\033[34;45mVocê esta com {} anos e esta na categoria SÊNIOR\033[m'.format(categoria))
else:
    print('\033[35;40mVocê esta com {} anos e esta na categoria MASTER\033[m'.format(categoria))
