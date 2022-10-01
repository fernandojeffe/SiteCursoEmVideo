#Maneira tradicional
'''co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adijacente: '))
hi = (co**2 + ca**2) ** (1/2)
print('A hipotenusa vai medir {}'.format(hi))'''
#importando modulo
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adijacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {}'.format(hi))
