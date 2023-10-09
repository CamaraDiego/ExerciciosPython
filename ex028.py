#ESCOLHER UM NUMERO ALEATÓRIO ENTRE 0 E 5
#PEDIR PARA O USUARIO TENTAR ADIVINHAR
#ESCREVER SE O USUARIO VENCEU OU NAO

from random import randint
from time import sleep
num = str(input('Vou pensar em um número inteiro de 0 a 5\nTente adivinhar em qual número eu pensei!\n')).strip()
num = int(num)
ran = randint(0, 5)
print('PENSANDO...')
sleep(2)
if num == ran:
    print('PARABÉNS! EU REALMENTE PENSEI NO NÚMERO {}.'.format(num))
else:
    print('Sinto muito, eu pensei no número {} e não no número {}.'.format(ran, num))
