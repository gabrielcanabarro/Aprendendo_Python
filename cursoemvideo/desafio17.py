import math
a = float(input('Qual o valor do cateto oposto em centímetros: '))
b = float(input('Qual o valor do cateto adjascente em centímetros: '))
h = math.hypot(a,b)
print('A hipotenusa mede {:.2f}cm'.format(h))