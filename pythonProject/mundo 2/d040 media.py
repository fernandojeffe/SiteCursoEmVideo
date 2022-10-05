print('\033[33m°°\033[m'*9)
print('Calculo de média ')
print('\033[33m°°\033[m'*9)
nota = float(input('Digite a primeira nota: '))
nota1 = float(input('Digite a segunda nota: '))
nota2 = float(input('Digite a terceira nota: '))
media = (nota+nota1+nota2)/3
if media < 5:
    print('\033[7;31;40mAluno REPROVADO sua media foi de {} \033[m'.format(media))
elif media > 7:
    print('\033[7;32;40mAluno APROVADO sua media foi de {} \033[m'.format(media))
else:
    print('\033[7;33;40m Aluno em RECUPERAÇÃO sua media foi de {} \033[m'.format(media))