lista = [[], []]
valor = 0
for c in range(0,7):
    valor = int(input(f'Digite o {c+1}º número: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
print(f'Os valores pares são: {lista[0]}')
lista[1].sort()
print(f'Os valores ímpares são: {lista[1]}')