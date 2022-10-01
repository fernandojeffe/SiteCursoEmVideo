from math import radians, sin, cos, tan
an = int (input('Digite o ânculo que você deseja: '))
seno = sin(radians(an))
print('O ânculo de {:.0f}° tem o seno de {:.2f}'.format(an, seno))
cosseno = cos(radians(an))
print('O ãncolu de {:.0f}° tem o cosseno de {:.2f}'.format(an, cosseno))
tangente = tan(radians(an))
print('O ânculo de {:.0f}° tem a tangente de {:.2f}'.format(an, tangente))

print("")
