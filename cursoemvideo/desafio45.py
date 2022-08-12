import random74
from time import sleep
lista = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
n = int(input('Qual sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('O computador escolheu {}.'.format(lista[computador]))
print('Você escolheu {}'.format(lista[n]))
print('-=' * 10)
if computador == 0:  # computador jogou pedra
    if n == 0:
        print('EMPATOU, jogue novamente!')
    elif n == 1:
        print('Você GANHOU!')
    elif n == 2:
        print('O computador GANHOU!')

elif computador == 1: # computador jogou papel
    if n == 0:
        print('O computador GANHOU!')
    elif n == 1:
        print('EMPATOU, jogue novamente!')
    elif n == 2:
        print('Você GANHOU!')
elif computador == 2: # computador jogou tesoura
    if n == 0:
        print('Você GANHOU!')
    elif n == 1:
        print('O computador GANHOU!')
    elif n == 2:
        print('EMPATOU, jogue novamente!')