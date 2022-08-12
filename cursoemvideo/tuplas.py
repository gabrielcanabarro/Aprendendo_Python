lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

#for comida in lanche:
 #  print(f'eu vou comer {lanche[2]}')

#for cont in range(0, len(lanche)):
#    print(lanche[cont])

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

# os dois formatos são iguais, mas as vezes só o de baixo funciona
# no terceiro formato, revela a posição