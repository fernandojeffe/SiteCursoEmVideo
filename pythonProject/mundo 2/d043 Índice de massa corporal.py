peso = float(input('qual o seu peso (Kg): '))
altura = float(input('Qual a sua altura(m): '))
imc = peso/(altura**2)
if imc < 18.5:
    print('\033[30;43mIMC {:.2f} abaixo do peso\033[m'.format(imc))
#elif imc >= 18.6 and imc < 25:
elif 18.5 <= imc < 25: #maneira mais pratica  
    print('\033[30;42mIMC {:.2f} com pose ideal\033[m'.format(imc))
#elif imc >=26.1 and imc < 30:
elif 25 <= imc < 30:
    print('\033[30;41mIMC {:.2f} sobrepeso\033[m'.format(imc))
else:
    print('\033[31;43mvish IMC de {:.2f} Deu merda chapa\033[m'.format(imc))