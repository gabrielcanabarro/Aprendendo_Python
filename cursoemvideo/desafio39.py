from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você deveria ter se alistado há {} anos'.format(saldo))
    print('Seu alistamento foi no ano de {}'.format(ano))
elif idade < 18:
    saldo = 18 - idade
    ano = saldo + atual
    print('Seu alistamento será daqui há {} anos'.format(saldo))
    print('Dirija a um quartel no ano de {}'.format(ano))