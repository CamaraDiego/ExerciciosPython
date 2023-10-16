#GERAR 5 VALORES ALEATÓRIOS E COLOCAR EM UMA TUPLA
#MOSTRAR A LISTAGEM DOS NÚMEROS GERADOS
#MOSTRAR QUAL O MAIOR E QUAL O MENOR NA TUPLA
from random import randint
from time import sleep
maior = menor = 0
tupla = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print('-=-' * 13)
print('Os valores dentro desta tupla aleatória são:')
sleep(0.5)
print(tupla)
for posicao, valor in enumerate(tupla):
    if posicao == 0:
        menor = valor
        maior = valor
    elif posicao != 0:
        if valor < menor:
            menor = valor
        if valor > maior:
            maior = valor
print('-=-' * 13)
sleep(0.5)
print(f'O menor valor dentro desta tupla é {menor}.')
print('-=-' * 13)
sleep(0.5)
print(f'E o maior valor dentro desta tupla é {maior}.')
print('-=-' * 13)
