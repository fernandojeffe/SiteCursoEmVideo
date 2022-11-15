aluno = {}

aluno['Nome'] = str(input('Qual o nome do aluno: '))
aluno['Media'] = float(input('Qual a media do aluno: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

for chave, valores in aluno.items():
    print(f' - {chave} é igual a {valores}') 
