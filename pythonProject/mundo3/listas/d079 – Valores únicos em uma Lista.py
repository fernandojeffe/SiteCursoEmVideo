lista = [ ]
saida =' '
while True:
    n = int(input('Informe um valor para a lista: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Não será adicionao ')
    saida = str(input('Deseja continuar [S/N]')).strip().upper()
    if saida in 'N': 
        if saida == 'N':
         break
print('-='*30)
lista.sort()
print(f'{lista}')
