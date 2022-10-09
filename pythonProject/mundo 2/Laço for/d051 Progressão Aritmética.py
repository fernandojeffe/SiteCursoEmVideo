from unicodedata import decimal


primeiro = int(input('Digite o termo: '))
razão = int(input('Digite a razão: '))
#formala para quantas casas quer que conte 
décimo = primeiro+(10-1)*razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c),end='→ ')
print('Acabou')