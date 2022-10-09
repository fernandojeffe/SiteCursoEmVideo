from datetime import date, datetime 
ano = date.today().year #para tirar o ano da maquina
contadorMenor = 0
contadorMaior = 0

for c in range (1,8):    
    c = int(input('Quais as datas de nascimento: '))
    qanos = ano - c
    if qanos <= 21:
        contadorMenor += 1
    else: 
        contadorMaior += 1
    
print('tem {} pessoas com menos de 21 anos'.format(contadorMenor))
print('tem {} pessoas com mais de 21 anos'.format(contadorMaior))