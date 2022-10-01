n = int(input("Dígite um numero: "))
cont = 1
print("-"*12)
for cont in range (10):
    print("{} x {:2} = {}".format(n,cont+1,n*(cont+1)))
print("-"*12)