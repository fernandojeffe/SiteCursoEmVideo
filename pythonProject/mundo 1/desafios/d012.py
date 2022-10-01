n = float (input("Dígite o preço do produto: R$"))
p = n * 5/100
pn = n-p
print("o preço com desconto e de: R${:.2f}".format(pn))