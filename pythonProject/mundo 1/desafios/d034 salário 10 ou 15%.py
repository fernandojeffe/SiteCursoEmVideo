sal = float(input('Digite o salário do funcionário R$:'))
if sal <= 1250:
    aumento = (sal * 15)/100 + sal
    print('O seu nuvo salário e de R$: {:.2f}'.format(aumento))
else:
    aumento1 = (sal * 10)/100 + sal
    print('O seu nuvo salário e de R$: {:.2f}'.format(aumento1))
