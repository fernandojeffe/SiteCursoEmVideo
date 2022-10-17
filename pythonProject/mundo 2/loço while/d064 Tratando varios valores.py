num = cont = soma = 0

while num != 999:
    num = int(input('Informe um valor: '))
    if num != 999:
        cont += 1
        soma += num
        print('Para sair a qualqer momento digite 999')
print ('Você digitol {} número e a soma deles é de {}.'.format(cont,soma))

