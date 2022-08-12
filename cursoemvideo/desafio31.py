km = int(input('Qual a distância da sua viagem? '))
if km < 200:
    preço1 = km*0.50
    print('A sua passagem custará R${}'.format(preço1))
else:
    preço2 = km*0.45
    print('A sua passagem custará R${}'.format(preço2))