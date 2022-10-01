velocidade = float(input('Qual a velocidade do carro? '))
if(velocidade > 80):
        multa = (velocidade-80) * 7
        print('Voce foi multado e valor sera R$7,00 por km!\nVoce tera que pagar este valor R$:{:.2f}'.format(multa))
if(velocidade <= 80):
        print("Parabens você não foi multado")
