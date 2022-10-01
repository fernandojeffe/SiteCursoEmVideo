peso = float(input('qual o seu peso: '))
altura = float(input('Qual a sua altura: '))
imc = peso/(altura*altura)
if imc < 18.5:
    print('\033[30;43mIMC {:.2f} abaixo do peso\033[m'.format(imc))
elif imc >= 18.6 and imc < 25:
    print('\033[30;42mIMC {:.2f} com pose ideal\033[m'.format(imc))
elif imc >=26.1 and imc < 30:
    print('\033[30;41mIMC {:.2f} sobrepeso\033[m'.format(imc))
else:
    print('\033[31;43mvish IMC de {:.2f} Deu merda chapa\033[m'.format(imc))