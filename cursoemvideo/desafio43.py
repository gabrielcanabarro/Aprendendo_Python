peso = float(input('Qual o seu peso em kg: '))
altura = float(input('Qual sua altura em metros: '))
imc = peso / altura**2
if imc <= 18.5:
    print('Seu IMC é {:.1f}, portanto você está abaixo do peso!'.format(imc))
elif imc <= 25:
    print('Seu IMC é {:.1f}, portanto você está no peso ideal!'.format(imc))
elif imc <= 30:
    print('Seu IMC é {:.1f}, portanto você está com sobrepeso!'.format(imc))
elif imc <= 40:
    print('Seu IMC é {:.1f}, portanto você está com obesidade!'.format(imc))
else:
    print('Seu IMC é {:.1f}, portanto você está com obesidade mórbida!'.format(imc))
