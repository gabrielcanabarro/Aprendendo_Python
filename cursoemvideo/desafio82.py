lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    esc = str(input('Quer continuar? [S/N] '))
    if esc in 'Nn':
        break
print('=-' *30)
print(f'A lista completa é {lista}.')
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista dos pares é {pares}')
print(f'A lista dos ímpares é {impares}')
