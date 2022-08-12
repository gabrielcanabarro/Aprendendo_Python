from datetime import date
ano = int(input('Que ano você nasceu: '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('Você tem {} anos e pertence a categoria MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e pertente a categoria INFANTIL.'.format(idade))
elif idade > 14 and idade <= 19:

    print('Você tem {} anos e pertence a categoria JÚNIOR.'.format(idade))
elif idade > 19 and idade <= 25:
    print('Você tem {} anos e pertence a categoria SÊNIOR.'.format(idade))
else:
    print('Você tem {} anos e pertence a categoria MASTER.'.format(idade))