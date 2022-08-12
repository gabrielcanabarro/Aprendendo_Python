'''a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
# Verificando o menor número
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor  = b
if c<a  and c<b:
    menor = c
# Verificando o maior número
if a>b and a>c:
    maior=a
if b>a and b<c:
    maior = b
if c>a and c>b:
    maior = c
    print('O maior número é {}'.format(maior))
    print('O menor número é {}'.format(menor))'''

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
list = [a, b, c]
print('Você digitou os seguintes números {}'.format(list))
print('O menor número digitado foi {}'.format(min(list)))
print('O maior número difitado foi {}'.format(max(list)))