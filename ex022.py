#LER UM NOME COMPLETP
#NOME COM TUDO MAIUSCULO
#NOME COM TUDO MINUSCULO
#QUANTAS LETRAS NO TOTAL SEM ESPAÇO
#QUANTAS LETRAS TEM SO O PRIMEIRO NOME

nome = str(input('Digite seu nome:\n')).strip()
print('Seu nome em maiúsculo é:')
print(nome.upper())
print('Seu nome em minúsculo é:')
print(nome.lower())
nome2 = nome.split()
nome2 = ''.join(nome2)
print('O total de letras no seu nome é {}.'.format(len(nome2)))
nome3 = nome.split()
print('Seu primeiro nome tem {} letras.'.format(len(nome3[0])))
