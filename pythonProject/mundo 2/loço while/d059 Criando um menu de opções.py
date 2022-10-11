from time import sleep
saida = ''

while saida != 'S':
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))

    print('''Menu de opções 
    [1] Somar
    [2] Multiplicar
    [3] Maior número
    [4] Novos números
    [5] Sair ''') 

    menu = int(input('Digite a opção desejada: '))
    
    if menu == 1:
        soma = n1 + n2
        print ('A soma dos número e de: {}'.format(soma))
    elif menu == 2:
        mult = n1 * n2
        print ('A multiplicação dos números e de {}'.format(mult))
    elif menu == 3:
        if n1 == n2:
            print ('Os números são iguais!')
        elif n1 > n2:
            print ('Os primeiro número é maior')
        else:
            print ('O segundo numero e maior')
    elif menu == 4:
        print ('Limpando dados')
        sleep(1)
    elif menu == 5:
        saida = str (input('Deseja realmente sair [S/N].')).upper()
        if saida == "S":
            print ('Saindo do Menu')
            sleep(1)
        else:
            print('Voltado ao menu')
    else:
        print('Opção errada tente novamente!')