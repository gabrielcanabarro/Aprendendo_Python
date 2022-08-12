print('='*8, 'LOJAS GABRIEL', '='*8)
compras = float(input('Qual o valor total das compras? R$'))
print('''Qual seria a forma de pagamento:
[ 1 ] à vista/dinheiro ou cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão ou mais''')
forma = int(input('Escolha a forma de pagamento: '))
if forma == 1:
    valor = compras - (compras*0.1)
    print('Suas compras de R${:.2f}, vão custar R${:.2f} no final.'.format(compras, valor))
elif forma == 2:
    valor = compras - (compras*0.05)
    print('Suas compras de R${:.2f}, vão custar R${:.2f} no final.'.format(compras, valor))
elif forma == 3:
    print('Suas compras vão custar R${:.2f}.'.format(compras))
elif forma == 4:
    parcela = int(input('Quantas parcelas: '))
    valor = compras + (compras*0.2)
    valorparcela = valor / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(parcela, valorparcela))
    print('Suas compras de R${:.2f}, vão custar R${:.2f} no final.'.format(compras, valor))

