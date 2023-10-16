#LER 4 VALORES DIGITADOS E GUARDAR EM UMA TUPLA
#MOSTRAR QUANTAS VEZES APARECEU O NÚMERO 9
#MOSTRAR EM QUE POSIÇÃO APARECEU O PRIMEIRO VALOR 3
#MOSTRAR QUAIS FORAM OS NÚMEROS PARES
from time import sleep
print('-=-' * 13)
n1 = str(input('Digite o primeiro número inteiro entre 0 e 10: ')).strip()
print('-=-' * 13)
while (n1.isnumeric() == False) or ((int(n1) < 0) or (int(n1) > 10) ):
    n1 = str(input('Digite o primeiro número inteiro entre 0 e 10: ')).strip()
    print('-=-' * 13)
n1 = int(n1)
n2 = str(input('Digite o segundo número inteiro entre 0 e 10: ')).strip()
print('-=-' * 13)
while (n2.isnumeric() == False) or ((int(n2) < 0) or (int(n2) > 10) ):
    n2 = str(input('Digite o segundo número inteiro entre 0 e 10: ')).strip()
    print('-=-' * 13)
n2 = int(n2)
n3 = str(input('Digite o primeiro número inteiro entre 0 e 10: ')).strip()
print('-=-' * 13)
while (n3.isnumeric() == False) or ((int(n3) < 0) or (int(n3) > 10) ):
    n3 = str(input('Digite o primeiro número inteiro entre 0 e 10: ')).strip()
    print('-=-' * 13)
n3 = int(n3)
n4 = str(input('Digite o primeiro número inteiro entre 0 e 10: ')).strip()
print('-=-' * 13)
while (n4.isnumeric() == False) or ((int(n4) < 0) or (int(n4) > 10) ):
    n4 = str(input('Digite o primeiro número inteiro entre 0 e 10: ')).strip()
    print('-=-' * 13)
n4 = int(n4)
tupla = (n1, n2, n3, n4)
print(tupla)
print('-=-' * 13)
sleep(1)
if tupla.count(9) != 0:
    print(f'O número 9 foi digitado {tupla.count(9)} vezes.')
    print('-=-' * 13)
else:
    print(f'O número 9 não foi digitado nenhuma vez.')
    print('-=-' * 13)
sleep(1)
if tupla.count(3) != 0:
    print(f'O número 3 aparece primeiro na posição {tupla.index(3) + 1}')
    print('-=-' * 13)
else:
    print('O número 3 não foi digitado nenhuma vez.')
    print('-=-' * 13)
cont = 0
for valor in tupla:
    if valor % 2 == 0:
        cont += 1
sleep(1)
if cont >= 1:
    print('Os valores pares digitados foram:')
    for c in tupla:
        if c % 2 == 0:
            sleep(0.5)
            print(c, end = ' ')
else:
    print('Não foram digitados números pares.')
print('\n', end = '')
print('-=-' * 13)
