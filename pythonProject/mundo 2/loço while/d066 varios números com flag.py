contador = soma = num = 0
while num != 999:
    num = int(input('digite um número (999 para parar):  '))
    contador += 1
    if num == 999:        
        break
    soma += num 

print(f'A soma dos {contador-1} e foi de {soma}')