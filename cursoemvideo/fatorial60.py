'''from math import factorial
n = int(input('Digite um valor para \ncalcular seu fatorial:  '))
fat = factorial(n)
print('O fatorial de {} é {}'.format(n, fat))'''


n = int(input('Digite um valor para \ncalcular seu fatorial: '))
c = n
f = 1
print('Calculando {}!'.format(n), end='')
while c > 0:
    print('{} = {} x '.format(n, c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1