Contador = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte' )
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    print()
    if 0 <=  num <= 20:
        break
    print('Tente de novo! ', end=' ')
print(f'Você digitou o número {Contador[num]}')
