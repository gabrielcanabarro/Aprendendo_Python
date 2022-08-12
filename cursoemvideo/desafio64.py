n = int(input('Digite um número [999 para parar]: '))
soma = 0
cont = 0
while True:
    cont += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont,soma))
