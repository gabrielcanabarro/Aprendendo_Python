first = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
decimo = first +(10 - 1) * reason #calcular o décimo termo de uma PA
for c in range(first, decimo, reason):
    print('{} '.format(c), end='-> ')
print('FIM')