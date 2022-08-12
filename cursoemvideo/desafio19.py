import random74
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno '))
d = str(input('Quarto aluno: '))
e = str(input('Quinto aluno: '))
lista = [a,b,c,d,e]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))