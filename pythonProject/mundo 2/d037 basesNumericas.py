num = int(input('Digite um número inteiro: '))
print('\033[31m<>\033[m'*15)
base = int(input('Digite [1] para binario!\nDigite [2] para octa\nDigite [3] para hexadecimal'))
print('\033[31m<>\033[m'*15)
if base == 1:
    conversao = bin(num) [2 :]
    nome = "Binario"
elif base == 2:
    conversao = oct(num) [2 :]
    nome = "Octa"
elif base == 3:
    conversao = hex(num) [2 :]
    nome = 'Hexadecimal'
else:
    print('Número invalido! "Tente novamente"')

print('O número \033[36m{}\033[m convertido para base \033[33m{}\033[m é \033[35m{}\033[m'.format(num,nome,conversao))