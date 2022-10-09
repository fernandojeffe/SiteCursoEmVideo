#guanabara
frase = str(input('Digite uma frase: ')).strip().upper() #deixando a frase em maiuscula para comparação
palavras = frase.split() #split para gerar uma lista 
juntos = ''.join(palavras) #juntou a lista sem espaços 

inverso = juntos[::-1] #modo fatiamento

#sem o for
'''inverso = '' 
for letra in range(len(juntos) -1,-1,-1):
    inverso += juntos[letra]'''

print('O inverso de {} é {}'.format(juntos, inverso))

if inverso == juntos:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não e um palídromo!')