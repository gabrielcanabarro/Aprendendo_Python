teste = list()
teste.append('Gabriel')
teste.append('27')
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['joão', 18], ['maria', 22], ['marcelo', 30]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

