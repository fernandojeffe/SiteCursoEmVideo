print ('Gerador de PA')
print ('-='*10)
primeiro = int(input('Informe o termo: '))
razão = int(input('Informe a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print ('{} ->'.format(termo),end='')
    termo += razão
    cont +=1
print ('Fim')