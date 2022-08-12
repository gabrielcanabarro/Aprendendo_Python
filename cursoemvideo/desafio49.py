while True:
    n = int(input('Diga um número para ver sua tabuada: '))
    if n < 0:
        print('PROGRAMA DE TABUADA ENCERRADA!')
        break
    for c in range(1, 11):
        print('{} x'.format(n), c, '= {}'.format(n*c))

