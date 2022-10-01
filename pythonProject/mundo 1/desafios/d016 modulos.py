#Como eu faria
'''n = float(input('Digite um valor: '))
print('O valor digitado foi de {} e sua porção inteira é {:.0f}'.format(n,n))'''
#outra forma de fazer
''''n = float(input('Digite um valor: '))
print('O valor digitado foi de {} e sua porção inteira é {}'.format(n,int(n)))'''
#importando do modulo
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi de {} e a sua porção inteira é {}'.format(num, trunc(num)))