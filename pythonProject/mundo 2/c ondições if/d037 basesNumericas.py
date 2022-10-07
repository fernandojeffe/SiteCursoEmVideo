
num = int(input('Digite um número inteiro: '))
print('\033[31m<>\033[m'*15)
base = int(input('Digite [1] para binario!\nDigite [2] para octa\nDigite [3] para hexadecimal: '))
print('\033[31m<>\033[m'*15)
if base == 1:
    print('O número \033[36m{}\033[m convertido para \033[33mBINARIO\033[m é \033[35m{}\033[m'.format(num,bin(num)[2:]))

elif base == 2:
    print('O número \033[36m{}\033[m convertido para \033[33mOCTAL\033[m é \033[35m{}\033[m'.format(num,oct(num)[2:]))
elif base == 3:
    print('O número \033[36m{}\033[m convertido para \033[33mHEXADECIMAL\033[m é \033[35m{}\033[m'.format(num,oct(num)[2:]))
else:
    print('Número invalido! "Tente novamente"')
