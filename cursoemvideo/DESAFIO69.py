tot18 = 0
tothom = 0
totmul = 0
while True:
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual seu sexo [M/F]: '))
    choice = str(input('Você quer continuar: [S/N] '))
    if choice in 'Nn':
        break
    if idade > 18:
        tot18 += 1
    elif sexo in 'Mm':
        tothom += 1
    elif sexo in 'Ff' and idade < 20:
        totmul += 1
print('Foram cadastradas {} pessoas maiores de 18 anos'.format(tot18))
print('Foram cadastrados {} homens'.format(tothom))
print('Foram cadastras {} mulheres com menos de 20 anos'.format(totmul))