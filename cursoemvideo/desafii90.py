aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('-='*30)
for k, v in aluno.items():
    print(f'-  {k} é igual a {v}.')
if aluno["media"] <= 7:
    print('- Situação é de recuperação')
else:
    print('- O aluno está aprovado')