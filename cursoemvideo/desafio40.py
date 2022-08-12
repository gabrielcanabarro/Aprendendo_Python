n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Sua média é {:.1f}'.format(media))
if 7 > media  >=5:
    print('Você está em recuperação!')
elif media < 5:
        print('Vocé foi reprovado!')
elif media >= 7:
    print('Você foi aprovado!')