from random import sample
n1 = str(input('Informe o primeiro nome: '))
n2 = str(input('Informe o segundo nome: '))
n3 = str(input('Informe o terceiro nome: '))
n4 = str(input('Informe o quarto nome: '))
lista1 = [n1, n2, n3, n4]
lista2 = sample(lista1, k = 2)
print('A ordem de apresentação será:\n{}'.format(lista2))
