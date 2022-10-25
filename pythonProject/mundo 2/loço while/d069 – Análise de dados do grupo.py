total18 = homens = mulherm = 0

while True:
    idade = int(input('Informa a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo [M/F]')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 20:
            mulherm += 1
    saida = ' '
    while saida not in 'SN':    
        saida = str(input('Quer continuar a cadastrar [S/N]')).strip().upper()[0]
    if saida == 'N':
        break

print(f'Foram cadastrados {total18} pessas com mais de 18 anos. ')
print(f'Foram cadastrados {homens} homens. ')
print(f'Foram cadastrados {mulherm} mulher com menos de 20 anos. ')




            

