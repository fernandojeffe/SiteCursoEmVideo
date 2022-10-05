print('-='*12)
print('Analisandor de triangulo')
print('-='*12)

r1 = int(input('Digite o valor do primeiro segmento: '))
r2 = int(input('Digite o valor do segundo segmento: '))
r3 = int(input('Digite o valor do terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCÉLES')
else:
    print('Os segmentos acima NÃO PODE FORMAR triângulo!')
