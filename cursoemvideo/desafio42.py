r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Estes 3 segmentos formam um triângulo! ', end='')
    if r1 == r2 == r3:
        print('E este é um triângulo EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('E este é um triângulo ESCALENO!')
    else:
        print('Este é um triângulo ISÓSCELES!')
else:
    print('Estes 3 segmentos não formam um triângulo!')
