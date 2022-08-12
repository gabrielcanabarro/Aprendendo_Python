n1 = float(input('Qual sua primeira nota: '))
n2 = float(input('Qual a sua segunda nota: '))
m = (n1 + n2)/2
print('A sua média é {:.1f}.'.format(m))
if m>=6:
    print('Parabéns!! A sua média é boa!')
else:
    print('Você tem que estudar mais!')