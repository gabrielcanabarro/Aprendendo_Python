frase = str(input('Escreva uma frase: ')).strip().upper()   #eliminei os espaços de antes e depois

palavras = frase.split()   #eliminei os espaços entre as strings, dividi em lista e juntei
junto = ''.join(palavras)
print('A frase {}'.format(junto))


#Palindromos muito foda, não terminei