#LER UM NUMERO N INTEIRO
#MOSTRAR OS N PRIMEIROS NUMEROS DA SEQUENCIA FIBONACCI
n = str(input("""SEQUÊNCIA FIBONACCI
Informe uma quantidade, em número inteiro, de valores
da sequência Fibonacci que deseja que seja mostrado: """)).strip()
while n.isnumeric() == False:
    n = str(input('Informe a quantidade em valor inteiro: ')).strip()
n = int(n)
t1 = 0
t2 = 1
cont = 3
print('-=-' * 10)
print('{:>2}º termo: 0'.format('1'))
print('{:>2}º termo: 1'.format('2'))
while cont <= n:
    t3 = t1 + t2
    print('{:>2}º termo: {}'.format(cont, t3))
    t1 = t2
    t2 = t3
    cont += 1
print('-=-' * 10)
print('Obrigado por usar nosso APP.')

