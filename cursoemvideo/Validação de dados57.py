sexo = str(input('Qual seu sexo [M/F]: ')).upper()
while sexo not in 'MF':
    sexo = str(input('Dado inválido, tente novamente. Qual seu sexo [M/F]: ')).upper()
print('Dado registrado com sucesso')