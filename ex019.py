from random import choice
n1 = str(input('Informe o primeiro nome: '))
n2 = str(input('Informe o segundo nome: '))
n3 = str(input('Informe o terceiro nome: '))
n4 = str(input('Informe o quarto nome: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O nome escolhido é {}.'.format(escolhido))
