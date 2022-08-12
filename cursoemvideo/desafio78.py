lista = []
maior = menor = 0

for l in range(0,5):
    lista.append(int(input('Digite um valor: ')))
    if l == 0:
        maior = menor = lista[l]
    else:
        if lista[l] > maior:
            maior = lista[l]
        if lista[l] < menor:
            menor = lista[l]
print(lista)
print(f'O maior número digitado foi {maior} na posição ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor número digitado foi {menor} na posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()