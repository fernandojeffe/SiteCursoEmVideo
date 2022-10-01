frase = str(input('Digite algo: ')).upper().strip()
print('A letra A aparece {} vezes na frase! '.format(frase.count('A')))
#count e pra localizar
print('A Primeira letra A Aparece na posição {}'.format(frase.find('A')+1))
#find para achar possição e +1 e para comesar do 1 não do 0
print('A última letra A pararece na posição {}'.format(frase.rfind('A')+1))
#rfind e pra achar a posição da esquerda pra direita