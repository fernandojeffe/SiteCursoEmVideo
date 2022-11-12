lista = []
while True:
        
    nome = str(input('nome: ')).title()
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2)/ 2
    lista.append([nome, [nota1, nota2], media])

    saida = ' '
    while saida not in 'SN':
        saida = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if saida == 'N':
        break
print('-='*30)
print(f'{"N°.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)

for indice, aluno in enumerate(lista):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-'*35)
    opção = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if opção == 999:
        print('Finalizando...')
        break
    if opção <= len(lista) -1:
        print(f'Notas de {lista[opção][0]} são {lista[opção][1]}')
print('<<< Volte sempre >>>')