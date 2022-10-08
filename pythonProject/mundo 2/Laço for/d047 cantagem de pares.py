print ('(:;)'*5)
print ('Contagem de pares')
print ('(;:)'*5)
for contador in range (1 , 50):
    resto = 1   
    if contador % 2 == 1:
        resto = contador + 1
        print(resto, end=", ") #end=", " para manter na mesma linha!