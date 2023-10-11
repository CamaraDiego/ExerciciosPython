#MOSTRAR EM TELA TODOS OS NÚMEROS PARES ENTRE 1 E 50

from time import sleep
print('Os números pares entre 1 e 50 são:')
sleep(1)
for c in range(0, 51, 2):
    if c != 0:
        print(c, end=' ')
