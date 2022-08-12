valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    esc = str(input('Quer continuar? [S/N] '))
    if esc in 'nN':
        break
print('-=' * 30)
print(f'Foram digitados {len(valores)} números.')
valores.sort(reverse=True)
print(valores)
if 5 in valores:
    print('O número 5 foi digitado.')
else:
    print('O número 5 não foi digitado.')