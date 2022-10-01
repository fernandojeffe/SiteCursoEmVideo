n1 = int(input('Digite tres número:'))
n2 = int(input('Digite outro número'))
n3 = int(input('Digite outro número'))

#verififanco o menor número
menor = n1

if n2 < n1 and n2 <n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print("Qual é o valor menor: {}".format(menor))
print('Qual é o maior valor {}'.format(maior))