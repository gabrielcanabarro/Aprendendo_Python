wage = float(input('Qual o seu salário? R$'))
if wage > 1250:
    aumento = (wage * 0.10) + wage
if wage <= 1250:
    aumento = (wage * 0.15) + wage
print('\033[4;30mParabéns!\033[m Você ganhou um aumento, seu novo salário será de R${:.2f}'.format(aumento))