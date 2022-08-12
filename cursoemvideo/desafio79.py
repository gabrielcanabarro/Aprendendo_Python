lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor já registrado')
    esc = str(input('Quer continuar [S/N]: '))
    if esc in 'Nn':
        break
lista.sort()
print(lista)