from math import factorial
n = str(input('Informe um número inteiro para calculo de fatorial: ')).strip()
while n.isnumeric() == False:
    n = str(input('Valor inválido, informe um número inteiro para cálculo de fatorial: ')).strip()
n = int(n)
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))
