casa  = float(input('Valor da casa: R$'))
salario = float(input('Salario? R$'))
fin = int(input('Quantos anos de financiamento? '))
parcela = casa/ (fin*12)
if parcela <  salario*0.30:
    print('Para pagar uma casa de R${:.2f} em {}, a prestação será de R${:.2f}'.format(casa, fin, parcela))
    print('Empréstimo APROVADO')
else:
    print('Empréstimo NEGADO')