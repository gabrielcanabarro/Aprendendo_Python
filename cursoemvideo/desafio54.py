from datetime import date
atual = date.today().year
maior = 0
menor = 0
for n in range(1,8):
    ano = int(input('{}ª pessoa. Ano de nascimento: '.format(n)))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('No total, são {} pessoas maiores de idade'.format(maior))
print('No total, são {} pessoas menores de idade'.format(menor))
