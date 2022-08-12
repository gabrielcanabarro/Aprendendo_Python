km = float(input('Quantos km você percorreu com o carro?'))
d = int(input('Quantos dias você usou o carro?'))
r1 = (km * 0.15) + (d * 60)
print('O valor total que você deverá pagar é R${:.2f}.'.format(r1))
