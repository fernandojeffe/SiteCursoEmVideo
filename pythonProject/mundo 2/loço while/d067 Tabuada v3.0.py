cont = 1 
num = mult = 0

while True:
    num = int(input('Quer ver tabuada de qual valor: '))
    if num <= -1:
        break
    for cont in range (10):
        cont += 1
        mult = num * cont
        print(f'{cont}  x  {num}  = {mult}')
print('tabuada encerrada ')

    
    

