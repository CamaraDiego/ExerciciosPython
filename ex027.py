#LER UM NOME COMPLETO
#MOSTRAR O PRIMEIRO E ÚLTIMO NOME SEPARADAMENTE

nome = str(input('Informe seu nome completo:\n')).strip()
nome = nome.split()
print('Seu primeiro nome é: {}.'.format(nome[0]))
print('E seu último nome é: {}.'.format(nome[len(nome) - 1]))
