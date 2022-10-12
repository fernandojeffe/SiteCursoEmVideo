'''resposta = 'S'
mascolino = 0
feminino = 0

while resposta == 'S':
    resposta=str(input('Quer cadastrar qual e o sexo [S/N] ')).strip().upper()[0]
    if resposta == 'S':
        sexo = str(input('Qual e o sexo [M/F]')).strip().upper()[0]
        if sexo == 'M':
            mascolino += 1
        if sexo == 'F':
            feminino += 1
        else:
            print('Opção invalida tente novamente! ')
    elif resposta == 'n':
        print('Foram registrados {} do sexo mascolino!'.format(mascolino))
        print('foram registrados {} do sexo feminino!'.format(feminino))
        print('Fim')
    else:
        print('Opção invalida')'''

        # guanabara 
sexo = str(input('informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo + str(input('Dados inválidos. Por favor, informe sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))