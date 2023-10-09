#LER UM NUMERO INTEIRO
#DIZER SE É PAR OU ÍMPAR
num = str(input('Informe um número inteiro:\n')).strip()
num = int(num)
if num % 2 == 0 and num != 0:
    print('O número {} é um número PAR.'.format(num))
elif num == 0:
    print('Você digitou 0 que é um número neutro, nem PAR nem ÍMPAR.')
else:
    print('O número {} é um número ÍMPAR.'.format(num))
