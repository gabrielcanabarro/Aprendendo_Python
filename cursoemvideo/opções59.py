opçao = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while opçao != 5:
    print('[ 1 ] somar'
      ' \n[ 2 ] multiplicar'
      ' \n[ 3 ] maior'
      ' \n[ 4 ] novos números'
      ' \n[ 5 ] sair do programa')
    opçao = int(input('Qual sua opção? '))
    if opçao == 1:
        soma = n1 + n2
        print('A soma dos dois números é {}'.format(soma))
    elif opçao == 2:
        multi = n1*n2
        print('A multiplicação entre os dois números é {}'.format(multi))
    elif opçao == 3:
        if n1 > n2:
            print('O maior número é o {}'.format(n1))
        if n2 > n1:
            print('O maior número é {}'.format(n2))
    elif opçao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('Finalizando o programa...')
    else:
        print('Opção inválida. Tente novamente!')