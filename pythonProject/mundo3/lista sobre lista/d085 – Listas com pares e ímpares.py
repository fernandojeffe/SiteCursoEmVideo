lista = [[],[]]

for contador in range (1,8):
    num = int(input(f'Informe o {contador}° número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print(f'Os valores paras: {lista[0]}')
print(f'Os valores ímpare: {lista[1]}')