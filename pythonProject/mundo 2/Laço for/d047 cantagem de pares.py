print ('\033[42m(;\033[m\033[43m:)\033[4m\033[m'*4)
print ('Contagem de pares')
print ('\033[43m(;\033[m\033[42m:)\033[4m\033[m'*4)
# O do quanabara 
for n in range (2,51,2):
    print(n, end=' ')
print('Acabou')

#O jeito que eu fiz 
'''
for contador in range (1 , 50):
    resto = 1   
    if contador % 2 == 1:
        resto = contador + 1
        print(resto, end=", ") #end=", " para manter na mesma linha!'''