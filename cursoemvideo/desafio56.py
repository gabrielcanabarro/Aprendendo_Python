somaidade = 0
maior = 0
nomevelho = ''
qmulher = 0
for c in range(1,5):
    print('-'*7, '{}ª PESSOA'.format(c), '-'*7)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))

    #médias da idades
    somaidade += idade
    mediaidade = somaidade/4


    #homem mais velho
    if c == 1 and sexo in 'mM':
        maior = idade
        nomevelho = nome
    else:
        if idade > maior and sexo in 'mM':
            maior = idade
            nomevelho = nome

    #mulher menos de 20
    if sexo in 'fF' and idade < 20:
        qmulher += 1

print('O homem mais velho é {} e ele tem {} anos'.format(nomevelho, maior))
print('A média das idades é {:.0f}'.format(mediaidade))
print('Tem {} mulheres com menos de 20 anos'.format(qmulher))
