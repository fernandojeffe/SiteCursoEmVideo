nome = (input('Digite o seu nome completo: '))
#conta quantos caracteres tem contando com os espaços
print("O nome digitado tem {} caracteres com espaços".format(len(nome)))
#conta quantos caracteres tem sem espaços
print("O nome digitado tem {} caracteres sem espaços".format(len(nome) - nome.count(' ')))
#deixa as letras em maiusculos
print(nome.upper())
#deixa as etras em menusculo
print(nome.lower())
#deixa as primeiras letras da frases em maiuculo
print(nome.title())
#para separa os caracteres
separa = nome.split()
print("seu primeiro nome e {} e tem {} letras".format(separa[0], len(separa[0])))
