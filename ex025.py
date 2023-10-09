#PEDIR UM NOME COMPLETO
#DIZER SE TEM SILVA NO NOME
nome = str(input('Informe seu nome:\n'))
nome = nome.upper()
if ('SILVA' in nome) == True:
    print('Você tem Silva no seu nome!')
else:
    print('Você não tem Silva no seu nome.')
