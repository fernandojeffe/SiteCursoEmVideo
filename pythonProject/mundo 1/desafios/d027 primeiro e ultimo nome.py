import ntpath

n = str(input('Digite o seu nome completo: ')).lower().strip()
nome = n.split()
print('muito prazer em ti conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]).title())
print('Seu último nome é {}'.format(nome[len(nome)-1].title()))

