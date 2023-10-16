from random import randint
from time import sleep
maior = menor = 0
tupla = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print('-=-' * 13)
print('Os valores dentro desta tupla aleatória são:')
sleep(0.5)
print(tupla)
print('-=-' * 13)
sleep(0.5)
print(f'O menor valor dentro desta tupla é {min(tupla)}.')
print('-=-' * 13)
sleep(0.5)
print(f'E o maior valor dentro desta tupla é {max(tupla)}.')
print('-=-' * 13)
