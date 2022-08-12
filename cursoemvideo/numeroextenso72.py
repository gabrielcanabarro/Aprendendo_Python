cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')
while True:
    n = int(input('Digite um número entre 0 e 5: '))
    if 0 <= n <=5:
        break
    print('Tente novamente', end='')
print(f'Você digitou o número {cont[n]}!')
a = str(input('Você quer continuar? [S/N] ')).lower()
