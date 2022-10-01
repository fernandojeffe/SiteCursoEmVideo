from datetime import date #para ver data da maquina
ano = int(input('Se quiser saber o ano atual e so digitar 0 ou \n Qual ano você quer saber se e bissexto:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano e {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))