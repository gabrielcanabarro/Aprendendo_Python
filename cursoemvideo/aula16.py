valores = []

for cont in range(0,3):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c+1} encontrei o valor {v-2}!')
print('Cheguei ao fim da lista.')