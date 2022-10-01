dias = float(input("Quantos dias Você ficou com o carro?: "))
km = float(input("E qual foi o total da colimetragem percorrida?: "))
aluguel = (dias*60) + (km*0.15)
print("{:.0f} dias com o carro, e com a distancia percorrida de {:.0f}km\n O valor total e de R${:.2f} ".format(dias,km,aluguel))

