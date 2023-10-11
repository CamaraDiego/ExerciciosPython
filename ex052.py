#LER UM NÚMERO INTEIRO E DIZER SE É OU NÃO PRIMO
numero = str(input('Informe um número inteiro: ')).strip()
numero = int(numero)
cont = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        cont = cont + 1
        print('\033[1:33m{}\033[m'.format(c), end= ' ')
    else:
        print('\033[1:31m{}\033[m'.format(c), end = ' ')
if cont == 2:
    print('\nO número {} é um número primo.'.format(numero))
else:
    print('\nO número {} não é um número primo!'.format(numero))
