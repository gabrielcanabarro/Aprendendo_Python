import random74
computador = random.randint(0,10)
print('*=*' * 8)
print('JOGO DA ADIVINHAÇÃO!!')
print('*=*' * 8)
jogador = int(input('Que número estou pensando entre 0 e 10? '))
palpites = 1
while computador != jogador:
    jogador = int(input('Você errou! Tente novamente. Qual número estou pensando?'))
    palpites += 1
    if computador == jogador:
        print('VOCÊ ACERTOU O NÚMERO!!!')
    else:
        if jogador < computador:
            print('Dica: MAIS')
        elif jogador > computador:
            print('Dica: MENOS')
print('Você precisou de {} tentativas para acertar!'.format(palpites))

