resposta = 'S'
mascolino = 0
feminino = 0

while resposta =='S':
    resposta=str(input('Quer cadastrar qual e o sexo [S/N] ')).upper()
    if resposta == 'S':
        sexo = str(input('Qual e o sexo [M/F]')).upper()
        if sexo == 'M':
            mascolino += 1
        if sexo == 'F':
            feminino += 1
        else:
            print('Opção invalida tente novamente! ')
print('Foram registrados {} do sexo mascolino!'.format(mascolino))
print('foram registrados {} do sexo feminino!'.format(feminino))
print('Fim')