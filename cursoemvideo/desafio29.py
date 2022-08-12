velocidade = float(input('Qual a velocidade do carro? '))
multa = (velocidade - 60) * 7
if velocidade > 60:
    print('MULTADO!! Você deve pagar uma multa de R${:.2f}!'.format(multa))

else:
    print('Tenha uma boa viagem!')