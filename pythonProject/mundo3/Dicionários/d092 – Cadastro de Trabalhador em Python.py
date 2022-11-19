from datetime import datetime

dados = {}
dados ['nome'] = str(input('Nome: '))
nascimento = int(input('Qual o ano de nascimento: '))
dados ['idade'] = datetime.now().year - nascimento
dados ['ctps'] = int(input('Carteira de trabalho (Digite 0 se não tiver)'))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k,v in dados.items():
    print(f' - {k}: tem os valores: {v}')